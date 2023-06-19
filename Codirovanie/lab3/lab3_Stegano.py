import os
import sys
import base64

# Проходим по битам каждого байта каждой картинки и скрываем один в другой
# Берем биты из байта обоих картинок и объединяем

BMP_HEADER_SIZE = 54

def encode_image(input_img_name, output_img_name, spy_file, degree = 4):

    spy_len = len(spy_file)
    img_len = os.stat(input_img_name).st_size

    spy = open(spy_file, 'r')
    input_image = open(input_img_name, 'rb')
    output_image = open(output_img_name, 'wb')

    bmp_header = input_image.read(BMP_HEADER_SIZE)
    output_image.write(bmp_header)

    spy_mask, img_mask = create_masks(degree)

    while True:
        symbol = spy.read(1)
        if not symbol:
            break
        symbol = ord(symbol)

        for byte_amount in range(0, 8, degree):
            img_byte = int.from_bytes(input_image.read(1), sys.byteorder) & img_mask
            bits = symbol & spy_mask
            bits >>= (8 - degree)
            img_byte |= bits

            output_image.write(img_byte.to_bytes(1, sys.byteorder))
            symbol <<= degree

    output_image.write(input_image.read())

    spy.close()
    input_image.close()
    output_image.close()

    return True


def decode_image(encoded_img, output_spy, pixels_to_read, degree = 4):
    img_len = os.stat(encoded_img).st_size

    spy = open(output_spy, 'w', encoding='utf-8')
    encoded_bmp = open(encoded_img, 'rb')

    encoded_bmp.seek(BMP_HEADER_SIZE)

    _, img_mask = create_masks(degree)
    img_mask = ~img_mask

    read = 0
    while read < pixels_to_read:
        symbol = 0

        for bits_read in range(0, 8, degree):
            img_byte = int.from_bytes(encoded_bmp.read(1), sys.byteorder) & img_mask
            symbol <<= degree
            symbol |= img_byte

        if chr(symbol) == '\n' and len(os.linesep) == 2:
            read += 1

        read += 1
        spy.write(chr(symbol))

    spy.close()
    encoded_bmp.close()
    return True


def create_masks(degree):
    spy_mask = 0b11111111
    img_mask = 0b11111111

    spy_mask <<= (8 - degree)
    spy_mask %= 256
    img_mask >>= degree
    img_mask <<= degree

    return spy_mask, img_mask

ch = input("1. Скрыть\n2. Раскрыть\nКоманда: ")
path = "C:/EmilyVolkova/Codirovanie/lab3/sample5.bmp"
spy = "C:/EmilyVolkova/Codirovanie/lab3/sample3.bmp"
encrypted = "C:/EmilyVolkova/Codirovanie/lab3/encrypted.bmp"
decrypted = "C:/EmilyVolkova/Codirovanie/lab3/decrypted.bmp"
if ch == "1":
    with open(spy, "rb") as f, open("spy.txt", "w") as f2:
        to_encode_head = str(base64.b64encode(f.read(54)))[2:]
        to_encode_bmp = str(base64.b64encode(f.read()))[2:] 
        f2.write(to_encode_head+to_encode_bmp)   
    encode_image(path, encrypted, "spy.txt")
elif ch == "2":
    decode_image(encrypted, "ss.txt", os.stat("spy.txt").st_size)
    with open("ss.txt", "r") as f:
        decoded = b"" + base64.b64decode(f.read())
    with open(decrypted, "wb") as f:
        f.write(decoded)
else:
    print("Такой команды нет")
