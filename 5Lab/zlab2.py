import cv2

#разрешение картинки 1600x1080

img = cv2.imread("c:/EmilyVolkova/2kurs/OPLabs/MyLabs/5Lab/foto.png", cv2.IMREAD_COLOR)

img = img[0:1080, 0:1100]

scale_percent = 60 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.putText(img, 'Hello World', (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0))

cv2.imwrite('c:/EmilyVolkova/2kurs/OPLabs/MyLabs/5Lab/fotoCV.png', img)
cv2.imshow('c:/EmilyVolkova/2kurs/OPLabs/MyLabs/5Lab/fotoCV.png', img)
cv2.waitKey(0)

img2 = img[400:648, 0:660]
img2 = cv2.blur(img2, (3, 3))

cv2.imshow('c:/EmilyVolkova/2kurs/OPLabs/MyLabs/5Lab/fotoCV.png', img2)
cv2.waitKey(0)

