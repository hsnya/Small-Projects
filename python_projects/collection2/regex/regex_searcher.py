"""This program reads txt files and search and replace words using regular expressions.

_Description_.

Example:
    $ python example_google.py

Section.

Attributes:
    _module_level_variable1_ (int): _Description_.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension
"""
import re

if __name__ == '__main__':
    pattern = r'(?P<number>\d+)\|(?P<date>.*)\|(?P<content>.*) (?P<url>http://nyti.ms/\w*)'
    # pattern = r'(?P<number>\d+)\|(?P<date>.*)\|(?P<content>.*[Kk]ill.*) (?P<url>http://nyti.ms/\w*)'
    # pattern = r'(?P<number>\d+)\|(?P<date>Mon Dec \d{2} \d{2}:\d{2}:\d{2} \+\d{4} \d{4})\|(?P<content>.*) (?P<url>http://nyti.ms/\w*)'
    file = r'python_projects\collection2\regex\inputs\nytimeshealth.txt'
    with open(file) as f:
        content = f.read()
    
    for match in re.finditer(pattern, content):
        print(match.groupdict()['content'])