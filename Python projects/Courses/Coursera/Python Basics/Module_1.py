import turtle

# Options
start_length = 120
start_width = 30
start_arc = 50
start_splits = 2

end_length = 10
end_width = 3
end_arc = 360/7
end_splits = 3

tree_depth = 5
leaf_size = 25
speed = 0

# Preparing to draw
canvas = turtle.Screen()
tor = turtle.Turtle()
tor.speed(0)
tor.penup()
tor.left(90)
tor.back(300)
tor.speed(speed)
tor.color("brown")
tor.pendown()

length_change = width_change = arc_change = splits_change = 0

if tree_depth - 1 != 0:
    tree_depth -= 1
    length_change = (end_length - start_length) / tree_depth 
    width_change = (end_width - start_width) / tree_depth 
    arc_change = (end_arc - start_arc) / tree_depth 
    splits_change = (end_splits - start_splits) / tree_depth 
    tree_depth += 1

# The function to draw a leaf
def leaf():
    def draw_half():
        for _ in range(5):
            tor.forward(leaf_size)
            tor.left(90 / 5)
    tor.speed(0)
    tor.penup()
    tor.color("pink")
    
    tor.begin_fill()
    
    tor.right(35)
    draw_half()
    
    tor.left(90)
    draw_half()
    
    tor.end_fill()
    
    tor.color("brown")
    tor.left(90+35)
    tor.pendown()
    tor.speed(speed)

# The function to draw a log/stick. Starts with initial values that change as it goes
def tree_log(current_depth = tree_depth, current_length = start_length, current_width = start_width, current_arc = start_arc, current_splits = start_splits):
    if current_depth == 0:
        leaf()
        return
    
    floored_splits = int(current_splits)
    
    tor.left(current_arc * ((floored_splits + 1) / 2))
    for _ in range(floored_splits):
        tor.width(current_width)
        
        tor.right(current_arc)
        tor.forward(current_length)
        
        tree_log(current_depth - 1, current_length + length_change, current_width + width_change, current_arc + arc_change, current_splits + splits_change)
        
        tor.width(current_width)
        tor.forward(-current_length)
    tor.left(current_arc * ((floored_splits - 1) / 2))

# Start the show!
tree_log()

canvas.exitonclick()