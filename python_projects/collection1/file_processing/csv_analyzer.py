"""This program reads csv files and create them"""

import csv

with open(r'Python projects\Samples\Texts\Input.txt', 'r') as fr:
    with open(r'Python projects\Samples\Texts\Output.txt', 'w') as fw:
        for line in fr:
            fw.write(str(len(line)) + '\n')