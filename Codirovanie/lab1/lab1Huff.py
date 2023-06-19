import pickle

def create_table(s):
    table_dict, codes_table, table_list = {}, {}, []
    for i in s:
        table_dict[i] = (table_dict[i] + 1) if i in table_dict else 1
    for i in table_dict:
        table_list.append([i, table_dict[i]])
    while len(table_list) > 1:
        (min1, min2) = (0, 1) if table_list[0][1] > table_list[1][1] else (1, 0)
        for i in range(2, len(table_list)):
            if table_list[i][1] < table_list[min1][1]:
                b = min1
                min1 = i
                if table_list[b][1] < table_list[min2][1]:
                    min2 = b
            elif table_list[i][1] < table_list[min2][1]:
                min2 = i
        for key in list(table_list[min1][0]):
            codes_table[key] = ("0" + codes_table[key]) if key in codes_table else "0"
        for key in list(table_list[min2][0]):
            codes_table[key] = ("1" + codes_table[key]) if key in codes_table else "1"
        table_list[min1][0] += table_list[min2][0]
        table_list[min1][1] += table_list[min2][1]
        table_list.pop(min2)
    return codes_table

def str2bin(s):
    num = 0
    for i in range(0, len(s)):
        num |= (lambda x: 1 if s[i] == "1" else 0)(s[i]) << (len(s) - 1 - i)
    return num

def bin2str(b):
    tmp = ""
    while b > 0:
        tmp += str(b & 1)
        b >>= 1
    return tmp[::-1]

def huff_encode(s):
    encoded_bin = ""
    encoded = ""
    codes_table = create_table(s)
    for i in s:
        encoded_bin = encoded_bin + codes_table[i]
    while len(encoded_bin) >= 8:
        encoded += chr(str2bin(encoded_bin[:8]))
        encoded_bin = encoded_bin[8:]
    return encoded, codes_table

def huff_decode(s, enc_table):
    to_decode = ""
    for ch in s:
        tmp = bin2str(ord(ch))
        if len(tmp) < 8:
            for i in range(0, 8 - len(tmp)):
                tmp = "0" + tmp
        to_decode += tmp
    decoded = enc_ch = ""
    for ch in to_decode:
        enc_ch += ch
        for dec_ch in enc_table:
            if enc_table[dec_ch] == enc_ch:
                decoded += dec_ch
                enc_ch = ""
    return decoded

def ct2str(ct):
    tmp = ""
    for i in ct:
        tmp += i + ct[i] + " "
    return str(len(tmp)) + " " + tmp

req = input("Команда: ")
if req == "encode":
        to_encode = ""
        try:
            h = open("C:\EmilyVolkova\Codirovanie\lab1\mumu.txt", "r")
            to_encode = h.read()
            h.close()
            if len(to_encode) > 0:
                print("Wait please...")
                encoded, codes_table = huff_encode(to_encode)
                with open("C:\EmilyVolkova\Codirovanie\lab1\compressed_by_Huff" + ".huf", "wb") as file:
                    pickle.dump(codes_table, file)
                    pickle.dump(encoded, file)
                print("output file: " + "C:\EmilyVolkova\Codirovanie\lab1\compressed_by_Huff" + ".huf")
                h.close()
            else:
                print("Input is empty.")
        except IOError:
            print("Oops! File error. Check it, please.")
elif req == "decode":
        to_decode = ""
        try:
            with open("C:\EmilyVolkova\Codirovanie\lab1\decompressed_by_LZ77" + ".huf", "rb") as file:
                codes_table = eval(pickle.load(file))
                to_decode = pickle.load(file)
            if len(to_decode) > 0:
                print("Wait please...")
                decoded = huff_decode(to_decode, codes_table)
                h = open("C:\EmilyVolkova\Codirovanie\lab1\decompressed_by_Huff.txt", "w")
                h.write(decoded)
                h.close()
                print('output path: C:\EmilyVolkova\Codirovanie\lab1\decompressed_by_Huff.txt')
            else:
                print("Input is empty.")
        except IOError:
            print("Oops! File error. Check it, please.")
else:
    print('Unknown command')            