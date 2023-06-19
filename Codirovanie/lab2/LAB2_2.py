with open("C:\EmilyVolkova\Codirovanie\lab2/sample.bmp", "rb") as f:
    # Считываем заголовок файла BMP (54 байта)
    header = f.read(54)

    # Считываем оставшуюся часть файла (данные пикселей в 24 битном формате)
    pixel_data = f.read()

# Создаем переменные для каждой RGB-компоненты
red_data = b""
green_data = b""
blue_data = b""

# Цикл, в котором мы проходим каждые 3 байта последовательности и сохраняем их в соответствующей переменной цвета
for i in range(0, len(pixel_data), 3):
    blue_data += bytes([pixel_data[i], 0, 0])
    green_data += bytes([0, pixel_data[i+1], 0])
    red_data += bytes([0, 0, pixel_data[i+2]])

# Функция, которая сохраняет данные RGB-компоненты в bmp-файл
def save_bmp(filename, header, data):
    with open(filename, "wb") as f:
        f.write(header)
        f.write(data)

# Сохраняем каждую RGB-компоненту в отдельный файл
save_bmp("C:\EmilyVolkova\Codirovanie\lab2/red.bmp", header, red_data)
save_bmp("C:\EmilyVolkova\Codirovanie\lab2/green.bmp", header, green_data)
save_bmp("C:\EmilyVolkova\Codirovanie\lab2/blue.bmp", header, blue_data)