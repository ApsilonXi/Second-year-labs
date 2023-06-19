import lab3Huff as H, lab3LZ_77 as LZ
import pickle
import base64

req = input("Команда: ")
if req == "encode huf":
        to_encode = ""
        try:
            with open("C:\EmilyVolkova\Codirovanie\lab3\sample.bmp", "rb") as h:
                to_encode_head = str(base64.b64encode(h.read(54)))[2:]
                to_encode_bmp = str(base64.b64encode(h.read()))[2:]

            print("Wait please...")
            encoded_head, codes_table_head = H.huff_encode(to_encode_head)
            encoded_bmp, codes_table_bmp = H.huff_encode(to_encode_bmp)
            with open("C:\EmilyVolkova\Codirovanie\lab3\compressed_by_Huff" + ".huf", "wb") as file:
                pickle.dump(codes_table_head, file)
                pickle.dump(encoded_head, file)
                pickle.dump(codes_table_bmp, file)
                pickle.dump(encoded_bmp, file)
            print("output file: " + "C:\EmilyVolkova\Codirovanie\lab3\compressed_by_Huff" + ".huf")
        except IOError:
            print("Oops! File error. Check it, please.")
elif req == "decode huf":
        try:
            with open("C:\EmilyVolkova\Codirovanie\lab3\decompressed_by_LZ77" + ".huf", "rb") as file:
                codes_table_head = eval(pickle.load(file))
                to_decode_head = pickle.load(file)
                codes_table_bmp = eval(pickle.load(file))
                to_decode_bmp = pickle.load(file)
            print("Wait please...")
            decoded_head = b"" + base64.b64decode(H.huff_decode(to_decode_head, codes_table_head))
            decoded_bmp = b"" + base64.b64decode(H.huff_decode(to_decode_bmp, codes_table_bmp))
            with open("C:\EmilyVolkova\Codirovanie\lab3\decompressed_by_Huff.bmp", "wb") as h:
                h.write(decoded_head)
                h.write(decoded_bmp)
            print('output file: C:\EmilyVolkova\Codirovanie\lab3\decompressed_by_Huff.bmp')
        except IOError:
            print("Oops! File error. Check it, please.")
elif req == 'encode lz':
    LZ.compress_file("C:\EmilyVolkova\Codirovanie\lab3\compressed_by_Huff.huf", "C:\EmilyVolkova\Codirovanie\lab3\compressed_by_LZ77.huf")
elif req == 'decode lz':
    LZ.decompress_file("C:\EmilyVolkova\Codirovanie\lab3\compressed_by_LZ77.huf", "C:\EmilyVolkova\Codirovanie\lab3\decompressed_by_LZ77.huf")
else:
    print("Unknown command")           