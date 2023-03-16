from PIL import Image, ImageDraw, ImageFont, ImageFilter

#разрешение картинки 1600x1080

img = Image.open("c:/EmilyVolkova/2kurs/OPLabs/MyLabs/5Lab/foto.png")

img = img.crop((0, 0, 1100, 1080))

draw = ImageDraw.Draw(img)
draw.ellipse((100, 200, 500, 500), outline=(255, 255, 255))
font = ImageFont.truetype("arial.ttf", 30)
draw.text((500, 300), 'test', (0, 255, 255), font)

img2 = img.crop((0, 800, 1100, 1080))
img2 = img2.filter(ImageFilter.BoxBlur(4))

img.paste(img2, (0, 800))

img.save('c:/EmilyVolkova/2kurs/OPLabs/MyLabs/5Lab/fotoDraw.png')
img.show('c:/EmilyVolkova/2kurs/OPLabs/MyLabs/5Lab/fotoDraw.png')








