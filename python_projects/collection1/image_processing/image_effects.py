import os.path

import image

img_path = r'python_projects\collection1\image_effects\inputs\flower.jpg'

img = image.Image(img_path)
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

def red_wash():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(pixel.getRed(), 0, 0)

            img.setPixel(col, row, new_pixel)
        if animation:
            img.draw(win)    
def green_wash():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(0, pixel.getGreen(), 0)

            img.setPixel(col, row, new_pixel)
        if animation:
            img.draw(win)
def blue_wash():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(0, 0, pixel.getBlue())

            img.setPixel(col, row, new_pixel)
        if animation:
            img.draw(win)
def grey_scale():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)
            average = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) // 3
            new_pixel = image.Pixel(average, average, average)

            img.setPixel(col, row, new_pixel)
        if animation:
            img.draw(win)
def invert():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(255 - pixel.getRed(), 255 - pixel.getGreen(), 255 - pixel.getBlue())

            img.setPixel(col, row, new_pixel)
        if animation:
            img.draw(win)
def mirror():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()//2):
            pixel1 = img.getPixel(col, row)
            pixel2 = img.getPixel(img.getWidth() - col - 1, row)

            img.setPixel(col, row, pixel2)
            img.setPixel(img.getWidth() - col - 1, row, pixel1)
        if animation:
            img.draw(win)
def blur():
    for row in range(1, img.getHeight() - 1):
        for col in range(1, img.getWidth() - 1):
            red = green = blue = 0
            
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    pixel = img.getPixel(j, i)
                    red += pixel.getRed()
                    green += pixel.getGreen()
                    blue += pixel.getBlue()
            
            new_pixel = image.Pixel(red // 9, green // 9, blue // 9)
                
            img.setPixel(col, row, new_pixel)
        if animation:
            img.draw(win)
def sepia():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            tr = int(0.393 * pixel.getRed() + 0.769 * pixel.getGreen() + 0.189 * pixel.getBlue())
            tg = int(0.349 * pixel.getRed() + 0.686 * pixel.getGreen() + 0.168 * pixel.getBlue())
            tb = int(0.272 * pixel.getRed() + 0.534 * pixel.getGreen() + 0.131 * pixel.getBlue())
            
            new_pixel = image.Pixel(min(tr, 255), min(tg, 255), min(tb, 255))

            img.setPixel(col, row, new_pixel)
        if animation:
            img.draw(win)

animation = True if input('Do you want animations? Yes to enable, anything to disable: ') else False
while 1:
    choice = input('Type the function you want to run on the image: ')
    match choice:
        case 'red_wash':
            red_wash() # Set the green and blue values to 0 while keeping red value
            break
        case 'green_wash':
            green_wash() # Set the red and blue values to 0 while keeping green value
            break
        case 'blue_wash':
            blue_wash() # Set the red and green values to 0 while keeping blue value
            break
        case 'grey_scale':
            grey_scale() # Average all color values
            break
        case 'invert':
            invert() # Subtract the color value from 255 for every color
            break
        case 'mirror':
            mirror() # Switch places of corresponding pixels
            break
        case 'blur':
            blur() # Average every pixel with its neighbors
            break
        case 'sepia':
            sepia() # Formula to get specific colors value
            break
        case _:
            print('Invalid input, try again.')
img.draw(win)

img_name = os.path.splitext(os.path.basename(img_path))
output_path = 'python_projects\\collection1\\image_effects\\outputs\\' + img_name[0] + '_{}' + img_name[1]

order = 0
while (os.path.exists(output_path.format(order))):
    print(output_path.format(order))
    input()
    order += 1
else:
    img.save(output_path.format(order))

win.exit_on_click()