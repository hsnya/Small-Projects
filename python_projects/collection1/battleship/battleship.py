"""Battleship game inside the terminal.

Rules:
- 2 Players.
- Every Player has a set of 5 ships, 1 long, 1 mid, 2 short and 1 tiny ,that they place on a 10x10 grade, 5x10 for each player.
- Each Player try to guess the other's ships location and destroy all of its ships.


Example:
    $ example(x)

Todo:
    * Lookup for improvements and apply them.

ToInclude:
    * Dictionaries methods
        * keys()
        * values()
        * items()
    * Lambda functions
    * Json
        * loads()
        * dumps()
            * indent
            * sort_keys
    * Deep and shallow copying
        * copy module
            * copy()
            * deepcopy()
    * Filtering
    * Sorting
        * Breaking ties
        * Sort dictionaries keys
    * Classes and objects
        * Constructors
        * String representation
        * Methods
        * Dunderscore methods
        * Sorting objects
        * Inheritance and multiple inheritance
            * Overriding
            * Modifications
    * Decorators
        * Decorators with arguments
        * Built-in decorators
            * property
            * staticmethod
            * classmethod
            * functools
                * cache
                * wraps
    * *Args and **Kwargs
"""

import json
import sys
from collections.abc import Iterable

import ascii_formatter as af


class Ship:
    def __init__(self, name: str, size: Iterable[int], color: Iterable[int], body: str, head: Iterable[int], tail: Iterable[int]):
            
        self.name = name
        self.size = size
        self.color = color
        self.body = body
        self.head = head
        self.tail = tail
        
        self.intact = [True]*size
    
    
    def damage(self, part):
        self.intact[part-1] = False
    
    
    def build(self, orientation: int):
        orientation %= 4
        color = af.sgr(foreground = self.color)
        damaged_color = af.sgr(foreground = (10, 10, 10))
        
        colors = [color if state else damaged_color for state in self.intact]
        parts = []
        parts.insert(0, colors.pop(0) + self.tail[orientation])
        parts.append(colors.pop(-1) + self.head[orientation])
        return parts
    
    
    def __str__(self):
        return f'Ship object:{self.name = }, {self.size = }, {self.color = }, {self.body = }, {self.head = }, {self.tail = }, {self.intact = }'


class Board:
    settings = json.load(open(__file__+'/../assets/settings.json'))
    
    def __init__(self, board_char: str = None,
                 miss_char: str = None,
                 board_size: Iterable[int] = None,
                 char_color: Iterable[int] = None,
                 bg_color: Iterable[int] = None,
                 miss_color: Iterable[int] = None,
                 hit_color: Iterable[int] = None):
        
        if board_char == None:
            board_char = self.settings['default']['board_char']
        if miss_char == None:
            board_char = self.settings['default']['miss_char']
        if board_size == None:
            board_size = self.settings['default']['board_size']
        if char_color == None:
            char_color = self.settings['default']['char_color']
        if bg_color == None:
            bg_color = self.settings['default']['bg_color']
        if miss_color == None:
            miss_color = self.settings['default']['miss_color']
        if hit_color == None:
            hit_color = self.settings['default']['hit_color']
            
        self.char = board_char
        self.miss_char = miss_char
        self.size = board_size
        self.char_color = char_color
        self.bg_color = bg_color
        self.miss_color = miss_color
        self.hit_color = hit_color
        
        self.ships = {}
    
    
    def print_board(self, mode=0):
        match mode:
            case 0:
                bg_color = af.sgr(background = self.bg_color)
                sea_color = af.sgr(foreground = self.char_color)
                reset = af.sgr(reset = True)
                
                board = [[sea_color + self.char for i in range(self.size[0])] for j in range(self.size[1])]
                
                board_str = bg_color + (reset + '\n' + bg_color).join([' '.join(s) for s in board]) + reset
                sys.stdout.write(board_str)
                sys.stdout.flush
            case _:
                raise ValueError(f'Mode {mode} isn\' valid.')

    
    def place_ship(self, ship: Ship):
        self.ships[ship.name]
    
    
    def __str__(self):
        return f'Board object: {self.char = }, {self.size = }, {self.bg_color = }, {self.miss_color = }, {self.hit_color = }'


if __name__ == '__main__':
    board = Board()
    
    data = {
    "carrier": {
        "size": 5,
        "color": [
            0,
            105,
            148
        ],
        "body": "▮▮",
        "head": ["◢◣", "▮▶", "◥◤", "◀▮"],
        "tail": ["◖◗", "●▮", "◖◗", "▮●"]
    },
    "battleship": {
        "size": 4,
        "color": [
            112,
            128,
            144
        ],
        "body": "▮▮",
        "head": ["◘◘", "▮◘", "◘◘", "◘▮"],
        "tail": ["◈◈", "◈▮", "◈◈", "▮◈"]
    },
    "cruiser": {
        "size": 3,
        "color": [
            139,
            69,
            19
        ],
        "body": "▮▮",
        "head": ["◢◣", "◩▶", "◥◤", "◀◪"],
        "tail": ["◄►", "◆◩", "◄►", "◩◆"]
    },
    "submarine": {
        "size": 3,
        "color": [
            46,
            139,
            87
        ],
        "body": "▯▯◁",
        "head": ["◿◺", "▯▷", "◹◸", "◁▯"],
        "tail": ["◶◴", "◵▯", "◴◶", "▯◷"]
    },
    "destroyer": {
        "size": 2,
        "color": [
            255,
            99,
            71
        ],
        "body": "▮▮",
        "head": ["↿↾", "=⇒", "⇃⇂", "⇐="],
        "tail": ["||", "==", "||", "=="]
    }
}
    
    carrier = Ship('carrier', **(data['carrier']))
    battleship = Ship('battleship', **(data['battleship']))
    cruiser = Ship('cruiser', **(data['cruiser']))
    submarine = Ship('submarine', **(data['submarine']))
    destroyer = Ship('destroyer', **(data['destroyer']))
    
    print(''.join(carrier.build(0)))
    print(''.join(carrier.build(1)))
    print(''.join(carrier.build(2)))
    print(''.join(carrier.build(3)))
    print()
    print(af.sgr(reset=True))