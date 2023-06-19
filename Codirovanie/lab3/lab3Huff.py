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

