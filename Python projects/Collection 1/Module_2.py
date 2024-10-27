import image

img = image.EmptyImage(100,100)
img.save(r"Python projects\Samples\Photos\White.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = p.getRed()
        newgreen = 0
        newblue = 0

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)
    img.draw(win)

win.exitonclick()