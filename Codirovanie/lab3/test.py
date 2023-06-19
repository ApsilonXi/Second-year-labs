path = "C:/EmilyVolkova/Codirovanie/lab3/cat2.bmp"
spy = "C:/EmilyVolkova/Codirovanie/lab3/sample3.bmp"

def encrypt():
    with open(path, "rb") as f1, open(spy, "rb") as f2:
        head1 = f1.read(54)
        pixels1 = f1.read()
        head2 = f2.read(54)
        pixels2 = f2.read()

    new_head = bytes(head1+head2)
    new_pixels = b""
    n, k = 0, 0
    print("Please, wait...")
    n, k = 0, 0
    for i in range(0, len(pixels1), 3):
        new_pixels += bytes([pixels1[i], pixels1[i+1], pixels1[i+2]])
        n += 1
        if n == 50:
            new_pixels += bytes([pixels2[k], pixels2[k+1], pixels2[k+2]])
            k += 1
            n = 0
    with open("C:/EmilyVolkova/Codirovanie/encrypted.bmp", "wb") as f:
        f.write(new_head)
        f.write(new_pixels)





encrypt()    
