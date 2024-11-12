"""Print ANSI's escape codes to gain even more control on the terminal.

ANSI escape codes can control some of the terminal's features, like controlling the cursor's position, changing text color, etc.

Example:
    $ example(x)

Todo:
    * Complete control sequence introducer.
        * Complete cursor control.
        * Complete text control.
        * Complete text attributes.
    * Complete operating system command.
        * .
        * .
    * Complete Fs escape sequence.
    * Complete Fp escape sequence.
    * Complete nF escape sequence.
"""


e = '\e'
"""Escape code in format"""
eo = '\033'
"""Escape code in octal format"""
eu = '\u001b'
"""Escape code in unicode format"""
eh = '\x1B'
"""Escape code in hexadecimal format"""