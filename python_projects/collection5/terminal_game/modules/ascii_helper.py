"""Print some normal ASCII's characters to control the terminal.

ASCII codes can control some of the terminal's features and format its output, like controlling the cursor's position, changing text color, etc.

Example:
    $ ring()
    
    $ print(move_cursor('up', 9))

Attributes:
    flow_mode (int): How the functions values should be treated,
- 0: Return their value.
- 1: Print their value.
- 2: Accumulate, then leash.
    accum (str): Where the commands accumulated. Decode before printing to see how it looks.

Todo:
    * Lookup for improvements and apply them.
    
    * Complete control sequence introducer.
        * Find a way to get cursor's position.
        * Complete text control.
        * Complete text attributes.
    * Complete operating system command.
        * .
        * .
    * Complete Fs escape sequence.
    * Complete Fp escape sequence.
    * Complete nF escape sequence.
"""

import functools
import sys

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
    sys.stdin.write('\a')


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
    def wrapper(*args: any, **kwargs: any):
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
                sys.stdin.write(result)
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
    sys.stdin.write(accum)
    accum = ''


@flow
def move_cursor(direction: str, n: int = 1):
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
        ValueError: If passed a non-str type to the parameter `direction`.
        ValueError: If passed a non-int type to the parameter `n`.
        ValueError: If the `direction`'s first letter is not valid.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    if type(direction) != str:
        raise ValueError('`direction` is not a string')
    
    if type(n) != int:
        raise ValueError('`n` is not an integer')
    
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
def set_cursor(n: int = 1, m: int = 1):
    """Moves the cursor to row `n`, column `m`. The values are 1-based.

    Args:
        n (int, optional): Row. Defaults to 1.
        m (int, optional): Column. Defaults to 1.

    Raises:
        ValueError: If passed a non-int type to the parameter `n`.
        ValueError: If passed a non-int type to the parameter `m`.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    if type(n) != int:
        raise ValueError('n is not an integer')
    
    if type(m) != int:
        raise ValueError('m is not an integer')
    
    
    return f'\033[{n};{m}H'


def get_cursor():
    sys.stdout.write('\033[6n')
    a = ascii(input())
    a = a[6:-2]
    x,y = map(int, a.split(';'))
    return (x,y)


@flow
def erase(space: str = 'Screen', n: int = 2):
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
        ValueError: If passed a non-str type to the parameter `space`.
        ValueError: If passed a non-int type to the parameter `n`.
        ValueError: If passed an integer not in the specified range to the parameter `n`.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    if type(space) != str:
        raise ValueError('`space` is not a string')
    
    if type(n) != int:
        raise ValueError('`n` is not an integer')
 
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
def scroll(direction: str, n: int = 1):
    """Add new lines at the bottom or the top of the screen.
    Direction (judged based on the first letter):
    - up # Add lines to the bottom.
    - down # Add lines to the top.

    Args:
        direction (str, optional): Where to scroll.
        n (int, optional): The amount of times to scroll. Defaults to 1.

    Raises:
        ValueError: If passed a non-str type to the parameter `direction`.
        ValueError: If passed a non-int type to the parameter `n`.
        ValueError: If the `direction`'s first letter is not valid.
    
    Returns:
        str: Command to print, or combine with other commands.
    """
    
    if type(direction) != str:
        raise ValueError('`direction` is not a string')
    
    if type(n) != int:
        raise ValueError('`n` is not an integer')
    
    l: str = direction[0].lower()
    match l:
        case 'u':
            l = 'S'
        case 'd':
            l = 'T'
        case _:
            raise ValueError(f'({direction}) is not a valid direction.')
    
    
    return f'\033[{n}{l}'


if __name__ == '__main__':
    flow_mode = 1
    
    print(get_cursor())