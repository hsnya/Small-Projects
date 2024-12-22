"""Print some normal ASCII's characters to control the terminal.

ASCII codes can control some of the terminal's features and format its output, like controlling the cursor's position, changing text color, etc.

Example:
    $ ring()
    
    $ print(move_cursor('up', 9))

    $ print(sgr(bold=True, italic=True, underline=True))

Attributes:
    flow_mode (int): How the functions values should be treated,
- 0: Return their value.
- 1: Print their value.
- 2: Accumulate, then leash.
    accum (str): Where the commands accumulated. Decode before printing to see how it looks.
"""

import functools
import select
import sys
import time
from collections.abc import Iterable

flow_mode: int = 0
"""How the functions values should be treated,
- 0: Return their value.
- 1: Print their value.
- 2: Accumulate, then leash.
"""
accum: str = ''
"""Where the commands accumulated. Decode before printing to see how it looks.
"""

def ring():
    """Ring the terminal's bell."""
    sys.stdout.write('\a')
    sys.stdout.flush()


def flow(func):
    """Decorator that wraps the functions to control their return values.

    Args:
        func (function): Function to wrap.

    Raises:
        ValueError: When the flow mode is out of range (0-2).

    Returns:
        _wrapped: The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args: any, **kwargs: any) -> str:
        """Control the return value of the function.

        Raises:
            ValueError: When the flow mode is out of range (0-2).

        Returns:
            str: If the flow mode is 1, return the value of the functions.
        """
        result: str = func(*args, **kwargs)
        
        match flow_mode:
            case 0:
                return result
            case 1:
                sys.stdout.write(result)
                sys.stdout.flush()
            case 2:
                accumulate(result)
            case _:
                raise ValueError('Flow mode is out of range (0-2)')
        
    return wrapper


def accumulate(*args: str):
    """Accumulate strings / commands.

    Args:
        *args (str): Strings to accumulate.
    """
    global accum
    accum += ''.join(args)


def leash():
    """Print the accumulated strings / commands and clear the accumulator."""
    
    global accum
    sys.stdout.write(accum)
    sys.stdout.flush()
    accum = ''


@flow
def move_cursor(direction: str, n: int = 1) -> str:
    """Moves terminal's cursor `n` cells in the given `direction`. If the cursor is already at the edge of the screen, this has no effect.
    Directions (judged based on the first letter):
    - up
    - down
    - right / forward
    - left / back
    - next line  # The start of the next `n` lines .
    - previous line  # The start of the `n` previous lines.
    - horizontal absolute  # Move cursor to column `n`.

    Args:
        direction (str): The direction to move the cursor into.
        n (int, optional): How many times to move the cursor. Defaults to 1.

    Raises:
        ValueError: If the `direction`'s first letter is not valid.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    direction = str(direction)
    n = int(n)
    
    l: str = direction[0].lower()
    match l:
        case 'u':
            l = 'A'
        case 'd':
            l = 'B'
        case 'r' | 'f':
            l = 'C'
        case 'l' | 'b':
            l = 'D'
        case 'n':
            l = 'E'
        case 'p':
            l = 'F'
        case 'h':
            l = 'G'
        case _:
            raise ValueError(f'({direction}) is not a valid direction.')
    
    return f'\033[{n}{l}'


@flow
def set_cursor(n: int = 1, m: int = 1) -> str:
    """Moves the cursor to row `n`, column `m`. The values are 1-based.

    Args:
        n (int, optional): Row. Defaults to 1.
        m (int, optional): Column. Defaults to 1.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    n = int(n)
    m = int(m)
    
    return f'\033[{n};{m}H'


def get_cursor() -> Iterable[int]:
    """Get the cursor's position in the terminal.

    Returns:
        Iterable[int]: x, y. the cursor's position.
    """
    sys.stdout.write("\033[6n")
    sys.stdout.flush()
    
    response = ""
    start_time = time.time()
    timeout = 1.0

    if sys.platform.startswith('win'):
        # Windows-specific implementation
        import msvcrt
        while time.time() - start_time < timeout:
            if msvcrt.kbhit():
                char = msvcrt.getch()
                response += char.decode("utf-8")
                if char == b'R':
                    break
    else:
        # UNIX-based implementation
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            while time.time() - start_time < timeout:
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    char = sys.stdin.read(1)
                    response += char
                    if char == 'R':
                        break
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if response.startswith("\033[") and response.endswith("R"):
        try:
            pos = response[2:-1]
            row, col = map(int, pos.split(";"))
            return row, col
        except ValueError:
            pass


@flow
def erase(space: str = 'Screen', n: int = 2) -> str:
    """Erase text in terminal based on modes.
    Modes:
    - 0: Clear from cursor to end of the screen.
    - 1: Clear from cursor to start of the screen.
    - 2: Clear The entire screen.
    Space (judged based on the first letter):
    - screen / display / terminal / window
    - line / row

    Args:
        space (str, optional): The range to erase in. Defaults to 'Screen'.
        n (int, optional): Erasion mode (from 0 to 2). Defaults to 2.

    Raises:
        ValueError: If passed an integer not in the specified range to the parameter `n`.
        ValueError: If passed an invalid space to the parameter `space`.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    space = str(space)
    n = int(n)
 
    if not 0 <= n <= 2:
        raise ValueError('n is not in the specified range (0-2)')
    
    l: str = space[0].lower()
    match l:
        case 's' | 't' | 'd' | 'w':
            l = 'J'
        case 'l' | 'r':
            l = 'K'
        case _:
            raise ValueError(f'({space}) is not a valid space.')
    
    
    return f'\033[{n}{l}'


@flow
def scroll(direction: str, n: int = 1) -> str:
    """Add new lines at the bottom or the top of the screen.
    Direction (judged based on the first letter):
    - up # Add lines to the bottom.
    - down # Add lines to the top.

    Args:
        direction (str, optional): Where to scroll.
        n (int, optional): The amount of times to scroll. Defaults to 1.

    Raises:
        ValueError: If the `direction`'s first letter is not valid.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    direction = str(direction)
    n = int(n)
    
    l: str = direction[0].lower()
    match l:
        case 'u':
            l = 'S'
        case 'd':
            l = 'T'
        case _:
            raise ValueError(f'({direction}) is not a valid direction.')
    
    
    return f'\033[{n}{l}'


@flow
def sgr(reset: bool = False, **kwargs) -> str:
    """Changes how the text looks. Enter a key-value of each format for the name as key and the value for how do want it to look.
    The_name_of_formation = False *to disable* / True *to enable* / int *for predefined colors from 0-255* / Iterable[int] *for rbg colors*
    - bold: bool
    - faint: bool
    - italic: bool
    - strike: bool
    - underline: bool
    - double_underline: bool
    - overline: bool
    - blink: bool
    - invert: bool
    - foreground: bool | int | Iterable[int]
    - background: bool | int | Iterable[int]

    Args:
        reset (bool, optional): If true, it will reset the formation before formatting. Defaults to False.
        **kwargs (dict, optional): Formats.

    Raises:
        ValueError: If passed an invalid format key to the parameter `**kwargs`.
        ValueError: If passed an invalid color format.

    Returns:
        str: Command to print, or combine with other commands.
    """
    
    reset = bool(reset)
    
    f = '\033[{}m'
    formats = {'bold': {True: 1, False: 22}, 'faint': {True: 2, False: 22}, 'italic': {True: 3, False: 23},
               'underline': {True: 4, False: 24}, 'double_underline': {True: 21, False: 24}, 'overline': {True: 53, False: 55},
               'blink': {True: '5', False: '25'}, 'invert': {True: '7', False: '27'}, 'strike': {True: '9', False: '29'},
               'foreground': {int: '38;5;{}', Iterable: '38;2;{};{};{}', False: 39}, 'background': {int: '48;5;{}', Iterable: '48;2;{};{};{}', False: 49}}
    
    foreground = 'foreground',kwargs.pop('foreground', None)
    background = 'background',kwargs.pop('background', None)
    
    
    formation = '\033[m' if reset else ''
    
    for key in kwargs:
        if key not in formats:
            raise ValueError(f'{key} is an invalid format')
        
        value = bool(kwargs[key])
        
        formation += f.format(formats[key][value])

    for color in foreground, background:
        
        value = color[1]
        name = color[0]
        if value != None:
            if value == False:
                formation += f.format(formats[name][False])
            elif isinstance(value, int):
                formation += f.format(formats[name][int].format(value))
            elif isinstance(value, Iterable) and all(type(x) == int and 0 <= x <= 255 for x in value) and len(value) == 3:
                formation += f.format(formats[name][Iterable].format(*value))
            else:
                raise ValueError(f'{value} for {name} is not valid.')
    

    return formation


if __name__ == '__main__':
    flow_mode = 2
    set_cursor(0,0)
    erase()
    leash()
    for i in range(20):
        set_cursor(i,0)
        for j in range(40):
            sgr(foreground=i+j+16)
            accumulate('■')
            sgr(reset=True)
    leash()
    