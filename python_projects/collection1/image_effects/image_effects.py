"""Apply effects on images.

Apply effects on a selected image.

Example:
    $ input_effect()

This function will prompt the user to write the name of the image, and what effect to apply on it.

Attributes:
    win (image.ImageWin): Window to display the image.

Todo:
    * Lookup for improvements and apply them.
"""
import os.path

import image


def red_wash(img: image.Image, animate = True):
    """Set the green and blue values to 0 while keeping red value.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(pixel.getRed(), 0, 0)

            img.setPixel(col, row, new_pixel)
        if animate:
            img.draw(win) 
    img.draw(win) 

           
def green_wash(img: image.Image, animate = True):
    """Set the red and blue values to 0 while keeping green value.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(0, pixel.getGreen(), 0)

            img.setPixel(col, row, new_pixel)
        if animate:
            img.draw(win)


def blue_wash(img: image.Image, animate = True):
    """Set the red and green values to 0 while keeping blue value.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(0, 0, pixel.getBlue())

            img.setPixel(col, row, new_pixel)
        if animate:
            img.draw(win)


def grey_scale(img: image.Image, animate = True):
    """Average all color values.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)
            average = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) // 3
            new_pixel = image.Pixel(average, average, average)

            img.setPixel(col, row, new_pixel)
        if animate:
            img.draw(win)


def invert(img: image.Image, animate = True):
    """Subtract the color value from 255 for every color.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            new_pixel = image.Pixel(255 - pixel.getRed(), 255 - pixel.getGreen(), 255 - pixel.getBlue())

            img.setPixel(col, row, new_pixel)
        if animate:
            img.draw(win)


def mirror(img: image.Image, animate = True):
    """Switch places of corresponding pixels.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()//2):
            pixel1 = img.getPixel(col, row)
            pixel2 = img.getPixel(img.getWidth() - col - 1, row)

            img.setPixel(col, row, pixel2)
            img.setPixel(img.getWidth() - col - 1, row, pixel1)
        if animate:
            img.draw(win)


def blur(img: image.Image, animate = True):
    """Average every pixel with its neighbors.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
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
        if animate:
            img.draw(win)


def sepia(img: image.Image, animate = True):
    """Formula to get specific colors value.

    Args:
        img (image.Image): An image to apply the effects on.
        animate (bool, optional): Animate the process or not. Defaults to True.
    """
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pixel = img.getPixel(col, row)

            tr = int(0.393 * pixel.getRed() + 0.769 * pixel.getGreen() + 0.189 * pixel.getBlue())
            tg = int(0.349 * pixel.getRed() + 0.686 * pixel.getGreen() + 0.168 * pixel.getBlue())
            tb = int(0.272 * pixel.getRed() + 0.534 * pixel.getGreen() + 0.131 * pixel.getBlue())
            
            new_pixel = image.Pixel(min(tr, 255), min(tg, 255), min(tb, 255))

            img.setPixel(col, row, new_pixel)
        if animate:
            img.draw(win)


def input_image(prompt: str = '') -> tuple[str]:
    """Prompt the user for an image name.

    Args:
        prompt (str, optional): A text is going to print in the terminal that asks the user for input. Defaults to ''.

    Returns:
        tuple[str]: Return a tuple = (Image path, Image name, Image extension)
    """
    
    while True:
        image_name = os.path.splitext(input(prompt))
        image_path = f'{os.path.abspath(__file__)}/../inputs/{image_name[0]}{image_name[1]}'
        if os.path.isfile(image_path):
            break
        print("There is no image of that name, write another one.")
    
    return (image_path,) + image_name

    
def save(img: image.Image, img_data: tuple[str]):
    """Enumerate the image ,then save it.

    Args:
        img (image.Image): An image to save.
        img_data (tuple[str]): A tuple of three values, Image path, Image name, and Image extension.
    """
    
    output_path = f'{os.path.abspath(__file__)}/../outputs/{img_data[1]}_{'{}'}{img_data[2]}'

    order = 0
    while (os.path.exists(output_path.format(order))):
        order += 1
    else:
        img.save(output_path.format(order))


def input_effect(img_data: tuple[str] = None):
    """Prompt the user for the image name and the effect to apply on it.

    Args:
        img_data (tuple[str], optional): A tuple of three values, Image path, Image name, and Image extension. If not specified, the user will be prompted for it. Defaults to None.
    """
    
    if img_data == None:
        img_data = input_image('Enter image name including the extension (from the inputs folder): ')
        
    img = image.Image(img_data[0])
    win = image.ImageWin(img.getWidth(), img.getHeight())
    img.draw(win)

    animate = input('Do you want to animate effects? Yes to enable, anything to disable: ') == 'Yes'
    print('''Here are the functions' names:
    - red_wash
    - green_wash
    - blue_wash
    - grey_scale
    - invert
    - mirror
    - blur
    - sepia
    ''')

    while True:
        choice = input('Type the function you want to run on the image: ')
        match choice:
            case 'red_wash':
                red_wash(img, animate)
                break
            case 'green_wash':
                green_wash(img, animate)
                break
            case 'blue_wash':
                blue_wash(img, animate)
                break
            case 'grey_scale':
                grey_scale(img, animate)
                break
            case 'invert':
                invert(img, animate)
                break
            case 'mirror':
                mirror(img, animate)
                break
            case 'blur':
                blur(img, animate)
                break
            case 'sepia':
                sepia(img, animate)
                break
            case _:
                print('Invalid input, try again.')

    save(img, img_data)

    print('Click on the image to close.')
    
if __name__ == '__main__':
    win = image.ImageWin()
    input_effect()
    win.exit_on_click()