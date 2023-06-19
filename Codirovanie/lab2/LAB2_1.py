import struct

with open("C:\EmilyVolkova\Codirovanie\lab2\sample.bmp", "rb") as f:
    print('Тип:', f.read(2).decode())
    print('Размер: %s' % struct.unpack('I', f.read(4)))
    print('Резервное поле: %s' % struct.unpack('H', f.read(2)))
    print('Резервное поле: %s' % struct.unpack('H', f.read(2)))
    print('Смещение: %s' % struct.unpack('I', f.read(4)))
    print('Размер заголовка: %s' % struct.unpack('I', f.read(4)))
    print('Ширина: %s' % struct.unpack('I', f.read(4)))
    print('Высота: %s' % struct.unpack('I', f.read(4)))
    print('Кол-во плоскостей: %s' % struct.unpack('H', f.read(2)))
    print('Бит/Пиксель: %s' % struct.unpack('H', f.read(2)))
    print('Тип сжатия: %s' % struct.unpack('I', f.read(4)))
    print('Размер сжатого изображения: %s' % struct.unpack('I', f.read(4)))
    print('Горизонатльное разрешение: %s' % struct.unpack('I', f.read(4)))
    print('Вертикальное разрешение: %s' % struct.unpack('I', f.read(4)))
    print('Количество цветов: %s' % struct.unpack('I', f.read(4)))
    print('Важные цвета: %s' % struct.unpack('I', f.read(4)))


