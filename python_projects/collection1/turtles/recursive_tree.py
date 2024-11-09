"""Draw a tree by recursive functions.

Use recursion to draw a tree, with specified settings.

Examples:
    $ draw_tree(start_length = 120, start_width = 30, start_arc = 50, start_splits = 2,
    $     end_length = 10, end_width = 3, end_arc = 360/7, end_splits = 3,
    $     tree_depth = 5, leaf_size = 25, speed = 0, do_draw_leaf = True, do_fast_leaf = False,
    $     wood_color = 'brown', leaf_color = 'pink', start_x = 0, start_y = -320, angle = 90)

    $ draw_tree(*pack_inputs())

Attributes:
    canvas (_Screen): The window used to draw trees on, can be used to clear the broad for example.
    tor (Turtle): The turtle that draws the trees.

Todo:
    * Lookup for improvements and apply them.
"""
import turtle

canvas = turtle.Screen()
tor = turtle.Turtle()


def draw_half_leaf(size: int | float = 10):
    """Draw half a leaf with the current color.

    Args:
        size (int | float, optional): The length of each segment. Defaults to 10.
    """
    tor.penup()
    tor.begin_fill()
    for _ in range(5):
        tor.forward(size)
        tor.left(90 / 5)
    tor.end_fill()
    tor.pendown()


def draw_leaf(size: int | float = 10, color: str = 'green', prev_color: str = None):
    """Draw a full leaf.

    Args:
        size (int | float, optional): The length of each segment. Defaults to 10.
        color (str, optional): The color of the leaf. Defaults to 'green'.
        prev_color (str, optional): A color to switch to after executing (usually the wood/tree color). Defaults to None.
    """
    if prev_color == None:
        prev_color = color
    
    tor.color(color)
    
    tor.right(35)
    draw_half_leaf(size)
    tor.left(90)
    draw_half_leaf(size)
    
    tor.color(prev_color)
    tor.left(90+35) # Fix rotation.


def draw_fast_leaf(size: int | float = 10, color: str = 'green', prev_color: str = None):
    """Instead of drawing a detailed leaf with `draw_leaf()` function, just put a dot.

    Args:
        size (int | float, optional): The diameter of the dot. Defaults to 10.
        color (str, optional): The color of the dot. Defaults to 'green'.
        prev_color (str, optional): A color to switch to after executing (usually the wood/tree color). Defaults to None.
    """
    if prev_color == None:
        prev_color = color
    
    tor.color(color)
    tor.dot(size)
    tor.color(prev_color)


def draw_branch(current_depth: int = 3, current_length: int | float = 60, current_width: int | float = 5, current_arc: int | float = 50, current_splits: int | float = 2,
            length_change: int | float = 0, width_change: int | float = 0, arc_change: int | float = 0, splits_change: int | float = 0,
            do_draw_leaf: bool = True, do_fast_leaf: bool = False, leaf_size: int | float = 10, leaf_color: str = 'green', wood_color: str = 'brown'):
    """Draw the tree log and keep call itself with different parameters to draw branches.

    Args:
        current_depth (int, optional): The depth of the function. It stops calling itself when it reaches 0. Defaults to 3.
        current_length (int | float, optional): The length of the branch. Defaults to 60.
        current_width (int | float, optional): The width of the branch. Defaults to 5.
        current_arc (int | float, optional): The angle between each branch. Defaults to 50.
        current_splits (int | float, optional): How many times the single branch splits. Defaults to 2.
        length_change (int | float, optional): The change of the branch length when the function call itself again. Defaults to 0.
        width_change (int | float, optional): The change of the branch width when the function call itself again. Defaults to 0.
        arc_change (int | float, optional): The change of the arc when the function call itself again. Defaults to 0.
        splits_change (int | float, optional): The change of the branch splits when the function call itself again. Defaults to 0.
        do_draw_leaf (bool, optional): If true, it will draw a leaf at the depth 0. Defaults to True.
        do_fast_leaf (bool, optional): If true, and `do_draw_leaf` true, it will put a dot instead of drawing a detailed leaf. Defaults to False.
        leaf_size (int | float, optional): The leafs segments length, or the diameter length of the dot if it a fast leaf. Defaults to 10.
        leaf_color (str, optional): The color of the leaf. Defaults to 'green'.
        wood_color (str, optional): The color of the wood, branches and log. Defaults to 'brown'.
    """
    # Draw a leaf at depth = 0 if do_draw_leaf is true and make it fast if do_fast_leaf is true.
    if current_depth == 0:
        if do_draw_leaf == True:
            if do_fast_leaf == True:
                draw_fast_leaf(leaf_size, leaf_color, wood_color)
            else:
                draw_leaf(leaf_size, leaf_color, wood_color)
        return
    
    # Splits count can't be a float, although it is essential to leave it as it is to pass it to the next call.
    floored_splits = int(current_splits)
    half_an_arc = (current_arc * (floored_splits + 1)) / 2
    tor.left(half_an_arc)
    
    # How many times it will split.
    for _ in range(floored_splits):
        tor.width(current_width)
        tor.color(wood_color)
        
        tor.right(current_arc)
        tor.forward(current_length)
        
        # Going deeper while applying some changes.
        draw_branch(current_depth - 1, current_length + length_change, current_width + width_change, current_arc + arc_change,
                 current_splits + splits_change, length_change, width_change, arc_change, splits_change,
                 do_draw_leaf, do_fast_leaf, leaf_size, leaf_color, wood_color)
        
        tor.width(current_width)
        tor.color(wood_color)
        tor.backward(current_length)
        
    tor.right(current_arc)
    tor.left(half_an_arc)


def draw_tree(start_length: int | float = 60, start_width: int | float = 5, start_arc: int | float = 50, start_splits: int | float = 2,
            end_length: int | float = 60, end_width: int | float = 5, end_arc: int | float = 50, end_splits: int | float = 2,
            tree_depth: int | float = 3, leaf_size: int | float = 10, speed: int | float = 0, do_draw_leaf: bool = True, do_fast_leaf: bool = False,
            wood_color: str = 'brown', leaf_color: str = 'green', start_x: int | float = 0, start_y: int | float = -canvas.screensize()[1], angle: int | float = 90):
    """Draw a full tree at specified coordinates.
 
    Args:
        start_length (int | float, optional): The length of the branch at the start. Defaults to 60.
        start_width (int | float, optional): The width of the branch at the start. Defaults to 5.
        start_arc (int | float, optional): The angle between each branch at the start. Defaults to 50.
        start_splits (int | float, optional): How many times the single branch splits at the start. Defaults to 2.
        end_length (int | float, optional): The length of the branch at the end. Defaults to 60.
        end_width (int | float, optional): The width of the branch at the end. Defaults to 5.
        end_arc (int | float, optional): The angle between each branch at the end. Defaults to 50.
        end_splits (int | float, optional): How many times the single branch splits at the end. Defaults to 2.
        tree_depth (int | float, optional): The max depth of the function. It will stop calling itself when it reaches 0. Defaults to 3.
        leaf_size (int | float, optional): The leafs segments length, or the diameter length of the dot if it a fast leaf. Defaults to 10.
        speed (int | float, optional): The speed of the drawing, 1 is slowest, 10 is fastest, 0 disable animations. Defaults to 0.
        do_draw_leaf (bool, optional): If true, it will draw a leaf at the depth 0. Defaults to True.
        do_fast_leaf (bool, optional): If true, and `do_draw_leaf` true, it will put a dot instead of drawing a detailed leaf. Defaults to False.
        wood_color (str, optional): The color of the wood, branches and log. Defaults to 'brown'.
        leaf_color (str, optional): The color of the leaf. Defaults to 'green'.
        start_x (int | float, optional): The x coordinate to start drawing from. Defaults to 0.
        start_y (int | float, optional): The y coordinate to start drawing from. Defaults to -canvas.screensize()[1].
        angle (int | float, optional): The angle of the whole tree. Defaults to 90.
    """
    tor.speed(speed)
    tor.penup()
    tor.goto(start_x, start_y)
    tor.setheading(angle)
    tor.color(wood_color)
    tor.pendown()

    # Initializing with 0.
    length_change = width_change = arc_change = splits_change = 0

    # The change for every depth.
    if tree_depth - 1 != 0:
        tree_depth -= 1
        length_change = (end_length - start_length) / tree_depth 
        width_change = (end_width - start_width) / tree_depth 
        arc_change = (end_arc - start_arc) / tree_depth 
        splits_change = (end_splits - start_splits) / tree_depth 
        tree_depth += 1 # Increasing by 1 for the leafs.
    
    draw_branch(current_depth = tree_depth, current_length = start_length, current_width = start_width, current_arc = start_arc, current_splits = start_splits,
        length_change = length_change, width_change = width_change, arc_change = arc_change, splits_change = splits_change,
        do_draw_leaf = do_draw_leaf, do_fast_leaf = do_fast_leaf, leaf_size = leaf_size, leaf_color = leaf_color, wood_color = wood_color)


def pack_inputs() -> tuple:
    """A function that asks for user's input for the tree settings.Then, pack the inputs into a tuple.
    Just unpack the tuple before passing it into the draw_tree() function.

    Returns:
        tuple: Packed inputs.
    """
    
    print('-- Type two numbers separated with space for the next prompts: --')

    start_length, end_length = input_float('Enter the starting and ending sticks length: ', 2)
    start_width, end_width = input_float('Enter the starting and ending sticks width: ', 2)
    start_arc, end_arc = input_float('Enter the starting and ending angles between sticks: ', 2)
    start_splits, end_splits = input_float('Enter the starting and ending sticks splits: ', 2)

    print('-- Type a single number for the next prompts --')
    
    tree_depth = input_float('Enter the depth of the tree (how many times the stick will split): ')
    speed = input_float('Enter how fast do you want the turtle (I recommended 0): ')
    wood_color = input_tor_color('Enter the color of the wood: ')
    
    do_draw_leaf = input('Enter Y for if you want to draw leafs, or anything else if not: ') == 'Y'
    if do_draw_leaf:
        do_fast_leaf = input('Enter Y if you want the leaf to be fast, or anything else if not: ') == 'Y'
        leaf_size = input_float('Enter the leaf size: ')
        leaf_color = input_tor_color('Enter the color of the leafs: ')

    start_x, start_y, angle = input_float('Enter x, y and the angle of the tree separated by spaces: ', 3)

    return (start_length, start_width, start_arc, start_splits,
            end_length, end_width, end_arc, end_splits,
            tree_depth, leaf_size, speed, do_draw_leaf, do_fast_leaf,
            wood_color, leaf_color, start_x, start_y, angle)


def input_float(input_prompt: str = '', input_amount: int = 1) -> float | tuple[float]:
    """A function to prompt the user for a floating number only.

    Args:
        input_prompt (str, optional): A text is going to print in the terminal that asks the user for input. Defaults to ''.
        input_amount (int, optional): How many numbers separated by spaces should the user inputs? Useful to enter a list of floats. Defaults to 1.

    Returns:
        float | tuple[float]: What the user inputted.
    """
        
    while True:
        prompt = input(input_prompt)
        
        if input_amount == 1:
            try:
                return float(prompt)
            except:
                pass
        prompt = prompt.split()
        if len(prompt) == input_amount:
            try:
                return tuple(map(float, prompt))

            except:
                pass
        print('*Invalid input, please enter a number of the specified amount separated by spaces.')
        print(prompt)


def input_tor_color(input_prompt: str = '') -> str | tuple[float]:
    """A function to prompt the user for a valid color for the turtle.

    Args:
        input_prompt (str, optional): A text is going to print in the terminal that asks the user for input. Defaults to ''.

    Returns:
        str | tuple[float]: It will be a string if it was a color name or hexadecimal color, and a tuple of floats if it was rgb color, should be unpacked before use.
    """
    
    while True:
        
        prompt = input(input_prompt)
        prompt = prompt.split()
        if len(prompt) == 3:
            try:
                color_tup = (float(x)/100 for x in prompt)
                tor.color(*color_tup)
                return color_tup
            except Exception as x:
                pass
        
        try:
            tor.color(prompt[0])
            return prompt[0]
        except:
            pass
        print('*Invalid input, please enter a name of an color or numbers in rgb format in range 0-100 separated by spaces.')
        print(prompt)
                

if __name__ == '__main__':
    draw_tree(*pack_inputs())
    draw_tree(start_length = 120, start_width = 30, start_arc = 50, start_splits = 2,
                end_length = 10, end_width = 3, end_arc = 360/7, end_splits = 3,
                tree_depth = 5, leaf_size = 25, speed = 0, do_draw_leaf = True, do_fast_leaf = False,
                wood_color = 'brown', leaf_color = 'pink', start_x = 0, start_y = -320, angle = 90)
    canvas.exitonclick()