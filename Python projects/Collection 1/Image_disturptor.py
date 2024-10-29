import image

img = image.Image(r'C:\Users\Lenovo\Personal Files\Scripts\Small-Projects\Python projects\Samples\Photos\Flower.jpg')
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

def red_wash():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(pixel.getRed(), 0, 0)

            img.setPixel(col, row, new_pixel)
        img.draw(win)    
def green_wash():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(0, pixel.getGreen(), 0)

            img.setPixel(col, row, new_pixel)
        img.draw(win)
def blue_wash():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(0, 0, pixel.getBlue())

            img.setPixel(col, row, new_pixel)
        img.draw(win)
def grey_scale():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)
            average = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) // 3
            new_pixel = image.Pixel(average, average, average)

            img.setPixel(col, row, new_pixel)
        img.draw(win)
def invert():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(255 - pixel.getRed(), 255 - pixel.getGreen(), 255 - pixel.getBlue())

            img.setPixel(col, row, new_pixel)
        img.draw(win)
def mirror():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()//2):
            pixel1 = img.getPixel(col, row)
            pixel2 = img.getPixel(img.getWidth() - col - 1, row)

            img.setPixel(col, row, pixel2)
            img.setPixel(img.getWidth() - col - 1, row, pixel1)
        img.draw(win)
def blur():
    pass
def sepia():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            tr = int(0.393 * pixel.getRed() + 0.769 * pixel.getGreen() + 0.189 * pixel.getBlue())
            tg = int(0.349 * pixel.getRed() + 0.686 * pixel.getGreen() + 0.168 * pixel.getBlue())
            tb = int(0.272 * pixel.getRed() + 0.534 * pixel.getGreen() + 0.131 * pixel.getBlue())
            
            new_pixel = image.Pixel(min(tr, 255), min(tg, 255), min(tb, 255))

            img.setPixel(col, row, new_pixel)
        img.draw(win)
def shift():
    pass

choice = input('Type the function you want to run on the image: ')
ran = False

while (not ran):
    if (choice == 'red_wash'):
        ran = True
        red_wash()
    elif (choice == 'green_wash'):
        ran = True
        green_wash()
    elif (choice == 'blue_wash'):
        ran = True
        blue_wash()
    elif (choice == 'grey_scale'):
        ran = True
        grey_scale()
    elif (choice == 'invert'):
        ran = True
        invert()
    elif (choice == 'mirror'):
        ran = True
        mirror()
    elif (choice == 'blur'):
        ran = True
        blur()
    elif (choice == 'sepia'):
        ran = True
        sepia()
    elif (choice == 'shift'):
        ran = True
        shift()
    else:
        choice = input('Invalid input, try again: ')

win.exitonclick()