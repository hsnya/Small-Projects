"""Print some normal ASCII's characters.

Example:
    $ tab(9)

Todo:
    * Lookup for improvements and apply them.
"""


def ring():
    """Ring the terminal's bell."""
    print('\a', end='')


def backspace(n: int = 1):
    """Return the cursor back n times.

    Args:
        n (int): Times to return the cursor back.
    """
    print('\b'*n, end='')


def carriage_return():
    """Return cursor to the start of the line."""
    print('\r', end='')


def tab(n: int = 1):
    """Insert a tab (4 spaces) n times.

    Args:
        n (int): Times to insert tabs.
    """
    print('\t'*n, end='')