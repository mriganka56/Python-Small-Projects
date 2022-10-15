import qrcode

img = qrcode.make("https://github.com/mriganka56")
print(img)
img.save("Fun.jpg")