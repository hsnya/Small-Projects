"""Analyze`data with numpy.

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

import numpy as np
import pandas as pd


def series():
    print(pd.Series(['Alice', None, 'Molly']))
    print(pd.Series([1, None, 3]))
    print(pd.Series([('Alice','Brown'),('Jack','White'),('Molly','Green')]))
    
    print(None == np.nan)
    print(np.isnan(np.nan))

    d = {'Alice':'Physics', 'Jack':'Chemistry', 'Molly':'English'}
    s = pd.Series(d)
    print(s)
    print(s.index)
    print(pd.Series(d,index=['Alice','Jack','Sam']))


def querying():
    d = {'Alice':'Physics', 'Jack':'Chemistry', 'Molly':'English', 'Sam':'History'}
    s = pd.Series(d)
    print(s.iloc[3])
    print(s.loc['Molly'])
    print(s['Molly'])
    
    n = pd.Series(np.random.randint(0, 10000, 10000))
    print(n.head())
    
    n += 2
    print(n.head())
    
    print(s._append(pd.Series(['Philosophy', 'Arts', 'Math'],index=['Kelly','Kelly','Kelly'])))
    print([pd.__version__])
    


if __name__ == '__main__':
    querying()