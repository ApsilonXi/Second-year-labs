import logging
import pickle
from typing import List, Tuple

def compress(input_string: str, max_offset: int = 2047, max_length: int = 31):
    """Сжимает входную строку в список значений длина, смещение, символ"""

    # Вход
    input_array = str(input_string[:])

    # Создайте строку из символов, которые были переданы
    window = ""

    ## Выход
    output = []

    while input_array != "":
        length, offset = best_length_offset(window, input_array, max_length, max_offset)
        output.append((offset, length, input_array[0]))
        window += input_array[:length]
        input_array = input_array[length:]

    return output


def to_bytes(
    compressed_representation,
    offset_bits: int = 11,
    length_bits: int = 5,
) -> bytearray:
    """Переделываем в байты"""
    output = bytearray()

    assert (
        offset_bits + length_bits
    ) % 8 == 0, f"Please provide offset_bits and length_bits which add up to a multiple of 8, so they can be efficiently packed. Received {offset_bits} and {length_bits}."
    offset_length_bytes = int((offset_bits + length_bits) / 8)

    for value in compressed_representation:
        offset, length, char = value
        assert (
            offset < 2 ** offset_bits
        ), f"Offset of {offset} is too large, only have {offset_bits} to store this value"
        assert (
            length < 2 ** length
        ), f"Length of {length} is too large, only have {length} to store this value"

        offset_length_value = (offset << length_bits) + length
        logging.debug(f"Offset: {offset}")
        logging.debug(f"Length: {length}")
        logging.debug(f"Offset and length: 0b{offset_length_value:b}")

        for count in range(offset_length_bytes):
            output.append(
                (offset_length_value >> (8 * (offset_length_bytes - count - 1)))
                & (0b11111111)
            )

        if char is not None:
            if offset == 0:
                output.append(ord(char))
        else:
            output.append(0)

    return output


def best_length_offset(
    window: str, input_string: str, max_length: int = 15, max_offset: int = 4095
):
    """Берёт окно и входную строку и возвращает смещение и длину
с наибольшей длиной входной строки в качестве подстроки"""

    if max_offset < len(window):
        cut_window = window[-max_offset:]
    else:
        cut_window = window

    # Возвращает (0, 0), если предоставленная строка пуста
    if input_string is None or input_string == "":
        return (0, 0)

    length, offset = (1, 0)

    # Это также должно привести к появлению пустого окна.
    if input_string[0] not in cut_window:
        best_length = repeating_length_from_start(input_string[0], input_string[1:])
        return (min((length + best_length), max_length), offset)

    # Наилучшая длина теперь равна нулю, чтобы события имели приоритет
    length = 0

    # сохранить смещение как можно меньшим
    # все окно целиком, либо максимальное смещение в сторону, в зависимости от того, что меньше
    for index in range(1, (len(cut_window) + 1)):
        # Get the character at this offset
        char = cut_window[-index]
        if char == input_string[0]:
            found_offset = index
            # Collect any further strings which can be found
            found_length = repeating_length_from_start(
                cut_window[-index:], input_string
            )
            if found_length > length:
                length = found_length
                offset = found_offset

    # позволитяет зафиксировать максимальное допустимое количество символов
    return (min(length, max_length), offset)

def repeating_length_from_start(window: str, input_string: str) -> int:
    """Получает максимальную повторяющуюся длину ввода с начала окна"""
    try:
        if window == "" or input_string == "":
            return 0
    except RecursionError:
        return 0

    if window[0] == input_string[0]:
        return 1 + repeating_length_from_start(
            window[1:] + input_string[0], input_string[1:]
        )
    else:
        return 0

def compress_file(input_file: str, output_file: str):
    """читает входной файл, сжимает его и записывает сжатые
значения в выходной файл"""
    try:
        with open(input_file, "rb") as f:
            input_codes_head = str(pickle.load(f))
            input_encoded_head = str(pickle.load(f))
            input_codes_bmp = str(pickle.load(f))
            input_encoded_bmp = str(pickle.load(f))
    except FileNotFoundError:
        print(f"Could not find input file at: {input_file}")
        raise
    except Exception:
        raise
    print("Wait, please...")
    compressed_input_head1 = compress(input_codes_head)
    compressed_input_head2 = compress(input_encoded_head)
    compressed_input_bmp1 = compress(input_codes_bmp)
    compressed_input_bmp2 = compress(input_encoded_bmp)

    with open(output_file, "wb") as f:
        pickle.dump(compressed_input_head1, f)
        pickle.dump(compressed_input_head2, f)
        pickle.dump(compressed_input_bmp1, f)
        pickle.dump(compressed_input_bmp2, f)

    print("output: " + output_file)

def decompress(compressed: List[Tuple[int, int, str]]) -> str:
    """Преобразует список (смещение, длина, символ) в выходную строку"""

    output = ""

    for value in compressed:
        offset, length, char = value

        if length == 0:
            if char is not None:
                output += char
        else:
            if offset == 0:
                if char is not None:
                    output += char
                    length -= 1
                    offset = 1
            start_index = len(output) - offset
            for i in range(length):
                output += output[start_index + i]

    return output

def from_bytes(
    compressed_bytes: bytearray, offset_bits: int = 11, length_bits: int = 5,
):

    assert (
        offset_bits + length_bits
    ) % 8 == 0, f"Please provide offset_bits and length_bits which add up to a multiple of 8, so they can be efficiently packed. Received {offset_bits} and {length_bits}."
    offset_length_bytes = int((offset_bits + length_bits) / 8)

    output = []

    while len(compressed_bytes) > 0:
        offset_length_value = 0
        for _ in range(offset_length_bytes):
            try:
                offset_length_value = (offset_length_value * 256) + int(compressed_bytes.pop(0))
            except IndexError:
                break

        offset = offset_length_value >> length_bits
        length = offset_length_value & ((2 ** length_bits) - 1)
        logging.debug(f"Offset: {offset}")
        logging.debug(f"Length: {length}")

        if offset > 0:
            char_out = None
        else:
            # Получает следующий символ и преобразует его в символ ascii
            char_out = str(chr(compressed_bytes.pop(0)))

        output.append((offset, length, char_out))

    return output

def decompress_file(input_file: str, output_file: str):
    """читает входной файл, распаковывает его и записывает сжатые
значения в выходной файл"""
    try:
        with open(input_file, "rb") as f:
            input_codes_head = pickle.load(f)
            input_encoded_head = pickle.load(f)
            input_codes_bmp = pickle.load(f)
            input_encoded_bmp = pickle.load(f)
    except FileNotFoundError:
        print(f"Could not find input file at: {input_file}")
        raise
    except Exception:
        raise
    
    print('Wait, please...')
    compressed_input_head1 = decompress(input_codes_head)
    compressed_input_head2 = decompress(input_encoded_head)
    compressed_input_bmp1 = decompress(input_codes_bmp)
    compressed_input_bmp2 = decompress(input_encoded_bmp)

    with open(output_file, "wb") as f:
        pickle.dump(compressed_input_head1, f)
        pickle.dump(compressed_input_head2, f)
        pickle.dump(compressed_input_bmp1, f)
        pickle.dump(compressed_input_bmp2, f)
    print("output: " + output_file)


