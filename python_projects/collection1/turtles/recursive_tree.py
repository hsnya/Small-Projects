"""This program draw a tree by recursive functions"""

import turtle

canvas = turtle.Screen()
tor = turtle.Turtle()

def draw_half_leaf(size: int | float):
    """Draw half a leaf with current color"""
    tor.penup()
    tor.begin_fill()
    for _ in range(5):
        tor.forward(size)
        tor.left(90 / 5)
    tor.end_fill()
    tor.pendown()
    
def leaf(size: int | float = 10, color: str = 'green', prev_color: str = None):
    """A function to draw a leaf with specified size, color, and color to switch to after executing"""
    if prev_color == None:
        prev_color = color
    
    tor.color(color)
    
    tor.right(35)
    draw_half_leaf(size)
    tor.left(90)
    draw_half_leaf(size)
    
    tor.color(prev_color)
    tor.left(90+35)

def fast_leaf(size: int | float = 10, color: str = 'green', prev_color: str = None):
    """A function to draw a leaf with specified size, color, and color to switch to after executing"""
    if prev_color == None:
        prev_color = color
    
    tor.color(color)
    
    tor.dot(size)
    
    tor.color(prev_color)

def tree_log(current_depth: int = 3, current_length: int | float = 60, current_width: int | float = 5, current_arc: int | float = 50, current_splits: int | float = 2,
            length_change: int | float = 0, width_change: int | float = 0, arc_change: int | float = 0, splits_change: int | float = 0,
            do_draw_leaf: bool = True, do_fast_leaf: bool = False, leaf_size: int | float = 10, leaf_color: str = 'green', wood_color: str = 'brown'):
    """A function to draw a log/stick. Starts with initial values that change as it goes."""
    # Draw a leaf at the maximum depth
    if current_depth == 0 and (do_draw_leaf == True):
        if do_fast_leaf == True:
            fast_leaf(leaf_size, leaf_color, wood_color)
        else:
            leaf(leaf_size, leaf_color, wood_color)
        return
    
    # splits count can't be a float, although it is essential to leave it as it is for passing it to the next call.
    floored_splits = int(current_splits)
    half_an_arc = (current_arc * (floored_splits + 1)) / 2
    tor.left(half_an_arc)
    for _ in range(floored_splits):
        tor.width(current_width)
        tor.color(wood_color)
        
        tor.right(current_arc)
        tor.forward(current_length)
        
        # Going deeper, applying the change while keeping some of the settings.
        tree_log(current_depth - 1, current_length + length_change, current_width + width_change, current_arc + arc_change,
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
    """A function to draw a tree at certain position with specified angle"""
    tor.speed(speed)
    tor.penup()
    tor.goto(start_x, start_y)
    tor.setheading(angle)
    tor.color(wood_color)
    tor.pendown()

    # Initializing with 0
    length_change = width_change = arc_change = splits_change = 0

    # Change for every depth
    if tree_depth - 1 != 0:
        tree_depth -= 1
        length_change = (end_length - start_length) / tree_depth 
        width_change = (end_width - start_width) / tree_depth 
        arc_change = (end_arc - start_arc) / tree_depth 
        splits_change = (end_splits - start_splits) / tree_depth 
        tree_depth += 1 # Increasing by 1 for the leafs
    
    tree_log(current_depth = tree_depth, current_length = start_length, current_width = start_width, current_arc = start_arc, current_splits = start_splits,
        length_change = length_change, width_change = width_change, arc_change = arc_change, splits_change = splits_change,
        do_draw_leaf = do_draw_leaf, do_fast_leaf = do_fast_leaf, leaf_size = leaf_size, leaf_color = leaf_color, wood_color = wood_color)

def pack_inputs() -> tuple:
    """A function that asks for user's input for the tree settings. Then, pack the inputs into a tuple.
    To use, just unpack the tuple before passing it into the draw_tree() function."""
    
    print('-- Type two numbers separated with space for the next prompts: --')

    start_length, end_length = map(float, input('Enter the starting and ending sticks length: ').split())
    start_width, end_width = map(float, input('Enter the starting and ending sticks width: ').split())
    start_arc, end_arc = map(float, input('Enter the starting and ending angles between sticks: ').split())
    start_splits, end_splits = map(float, input('Enter the starting and ending sticks splits: ').split())

    print('-- Type a single number for the next prompts --')

    tree_depth = float(input('Enter the depth of the tree (how many times the stick will split): '))
    speed = float(input('Enter how fast do you want the turtle (I recommended 0): '))
    wood_color = input('Enter the color of the wood: ')
    if input('Enter Y or N for if you want to draw leafs: ') == 'Y':
        do_draw_leaf = True
        if input('Enter Y or N for if you want the leaf to be fast or not: ') == 'Y':
            do_fast_leaf = True
        leaf_size = float(input('Enter the leaf size: '))
        leaf_color = input('Enter the color of the leafs: ')
    start_x, start_y, angle = map(float, input('Enter x, y and the angle of the tree seperated by spaces: ').split())
    return (start_length, start_width, start_arc, start_splits,
            end_length, end_width, end_arc, end_splits,
            tree_depth, leaf_size, speed, do_draw_leaf, do_fast_leaf,
            wood_color, leaf_color, start_x, start_y, angle)

# draw_tree(*pack_inputs())
draw_tree(start_length = 120, start_width = 30, start_arc = 50, start_splits = 2,
            end_length = 10, end_width = 3, end_arc = 360/7, end_splits = 3,
            tree_depth = 5, leaf_size = 25, speed = 0, do_draw_leaf = True, do_fast_leaf = False,
            wood_color = 'brown', leaf_color = 'pink', start_x = 0, start_y = -320, angle = 90)

canvas.exitonclick()