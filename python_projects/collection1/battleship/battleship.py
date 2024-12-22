"""Battleship game inside the terminal.

Rules:
- 2 Players.
- Every Player has a set of 5 ships, 1 long, 1 mid, 2 short and 1 tiny, that they place on a 10x10 grade, 5x10 for each player.
- Each Player try to guess the other's ships location and destroy all of their ships.


Example:
    $ example(x)

Todo:
    * Board
        * Attack printing
            * Miss
            * Hit
            * Place Ship
    * Player
        * Attacking
        * Placing Ships
        * AI
            * RNG
        * Human
            * Entering Name
    * Game
        * Start
        * Roles
        * Prompting
        * Win and Lose
        * Retry
        * Save Result
        * Menu
    
    * Add typings
    * Add limits
    * Add documentation
"""

import copy
import functools
import json
import sys
from collections.abc import Iterable

import ascii_formatter as af


class Part:
    def __init__(self, name, char):
        self.name = name
        self.char = char
        
        self.damaged = False
    
    
    def __bool__(self):
        return self.damaged
    
    
    def __str__(self):
        return f'<name = {self.name}, damaged {self.damaged}>'


class Ship:
    def __init__(self, name, body, head, tail, length, rotation = 0):
        self.name = name
        self.body = body
        self.head = head
        self.tail = tail
        
        self.parts = [Part('body', body) for _ in range(length)]
        self.parts[0].name = 'tail'
        self.parts[-1].name = 'head'
        
        self.rotation = rotation
    
    
    @property
    def rotation(self):
        return self.__rotation
    
    
    @rotation.setter
    def rotation(self, value):
        self.__rotation = value % 4
        self.parts[0].char = self.tail[self.__rotation]
        self.parts[-1].char = self.head[self.__rotation]
    
    
    def __str__(self):
        return f'<Ship object, name = {self.name}, parts = {list(map(str, self.parts))}, rotation = {self.rotation}>'


class Board:
    def __init__(self, board_size, board_char, miss_char, hit_char,
                 bg_color, char_color, destroyed_color,
                 intact_color, miss_color, hit_color):
        self.__board_size = board_size
        self.board_char = board_char
        self.miss_char = miss_char
        self.hit_char = hit_char
        self.bg_color = bg_color
        self.char_color = char_color
        self.destroyed_color = destroyed_color
        self.intact_color = intact_color
        self.miss_color = miss_color
        self.hit_color = hit_color
        
        self.board = [[board_char for j in range(board_size[1])] for i in range(board_size[0])]
    
    
    def __len__(self):
        return self.__board_size
    
    
    def print_board(self, n, m):
        sys.stdout.write(af.erase())
        for i in range(self.__board_size[0]*2-1):
            sys.stdout.write(af.set_cursor(n+i, m))
            sys.stdout.write(af.sgr(background=self.bg_color, foreground=self.char_color))
            
            for j in range(self.__board_size[1]):
                if i % 2 == 0:
                    char = self.board_char
                    sep = '|'
                else:
                    char = '=='
                    sep = '='
                sys.stdout.write(char)
                
                if j < self.__board_size[1]-1:
                    sys.stdout.write(sep)
                    
            sys.stdout.write(af.sgr(reset=True))
                
        sys.stdout.flush()
        


class Player:
    pass    


class Bot(Player):
    pass


class Human(Player):
    pass


class Game:
    def __init__(self):
        pass
    
    @classmethod
    def reload_assets(cls):
        with open(f'{__file__}/../assets/ships.json', encoding='utf-8') as ships_f:
            cls.ships_components = json.load(ships_f)
        with open(f'{__file__}/../assets/boards.json', encoding='utf-8') as boards_f:
            cls.boards = json.load(boards_f)
        with open(f'{__file__}/../assets/history.json', encoding='utf-8') as history_f:
            cls.history = json.load(history_f)


if __name__ == '__main__':
    Game.reload_assets()
    
    board = Board(**Game.boards['default'])
    board.print_board(5, 5)