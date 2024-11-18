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
    

def introDataFrames():
    students = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]
    
    df = pd.DataFrame((students),
                      index=['school1', 'school2', 'school1'])
    
    print(df.head())
    print(df.loc['school1', 'Name'])
    print(df['Name'])
    
    print(df.T)
    print(df.T.loc['Name'])
    
    print(df.drop('Name', axis=1, inplace=True))
    del df['Class']
    print(df)
    
    df['Class'] = None
    print(df)


def dataFramesIndexLoad():
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\Admission_Predict.csv', index_col=0)
    df = df.rename(mapper=str.strip, axis='columns')
    df = df.rename(columns={'SOP': 'Statement of Purpose',
                            'LOR': 'Letter of Recommendation'})
    print(df.head())
    
    df.columns = [x.upper() for x in list(df.columns)]
    print(df.head())


def dataFramesQuerying():
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\Admission_Predict.csv', index_col=0)
    df = df.rename(mapper=lambda x: x.strip().lower(), axis='columns')
    
    print(df.head())
    
    mask = (df['chance of admit'] > 0.8) | (df['gre score'] < 320) # |
    mask = df['chance of admit'].gt(0.8, ) & df['gre score'].lt(320)
    print(df.where(mask).dropna().head())


def dataFramesIndexing():
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\Admission_Predict.csv', index_col=0)
    df = df.rename(mapper=lambda x: x.strip().lower(), axis='columns')
    
    print(df.head())
    
    df['serial number'] = df.index
    df = df.set_index('chance of admit')
    print(df.head())
    
    df = df.reset_index()
    print(df.head())
    
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\census.csv')
    print(df.head())
    
    print(df['SUMLEV'].unique())
    
    df = df.set_index(['STNAME', 'CTYNAME'])
    print(df.head())

    print(df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ])


def dataFramesManipulation():
    pass


def missingValues():
    pass


if __name__ == '__main__':
    # series()
    # querying()
    # introDataFrames()
    # dataFramesIndexLoad()
    # dataFramesQuerying()
    # dataFramesIndexing()
    dataFramesManipulation()
    missingValues()