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

import numpy as np
import pandas as pd


def mergingDataFrames():
    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                             {'Name': 'Sally', 'Role': 'Course liasion'},
                             {'Name': 'James', 'Role': 'Grader'}])
    student_df = pd.DataFrame([{'Name': 'Mike', 'School': 'Law'},
                               {'Name': 'Sally', 'School': 'Engineering'},
                               {'Name': 'James', 'School': 'Business'}])
    
    print(staff_df)
    print(student_df)
    
    print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))

    print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))

    print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))

    print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))

    print(pd.merge(staff_df, student_df, how='right', on='Name'))
    
    staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 
                          'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 
                          'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 
                          'Role': 'Grader'}])
    student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 
                            'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 
                            'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 
                            'School': 'Engineering'}])
    
    print(pd.merge(staff_df, student_df, how='inner', on=['First Name','Last Name']))
    
    print(pd.concat([student_df, staff_df], keys=['students', 'staff']))


def groupBy():
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\census.csv')
    df = df[df['SUMLEV']==50]
    
    print(df.head())
    
    for group, frame in df.groupby('STNAME'):
        print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')
    
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\listings.csv')
    df.set_index(['cancellation_policy', 'review_scores_value'], inplace=True)
    
    for group, frame in df.groupby(level=(0,1)):
        print(group)
    
    for group, frame in df.groupby(by=lambda x: (x[0],'10' if x[1] == 10 else 'not 10')):
        print(group)
        
    df=df.reset_index()
    print(df.groupby("cancellation_policy").agg({"review_scores_value":('mean','std'),"reviews_per_month":'mean'}))
    print(df[['cancellation_policy', 'review_scores_value']].groupby("cancellation_policy").transform('mean').head())
    print(df.groupby("cancellation_policy").filter(lambda x: x['review_scores_value'].mean() > 9.2).head())
    
    def calc_mean_review_scores(group):
        avg=np.nanmean(group["review_scores_value"])
        group["review_scores_mean"]=np.abs(avg-group["review_scores_value"])
        return group

    print(df.groupby('cancellation_policy').apply(calc_mean_review_scores, include_groups=False).head())
    

def scales():
    df=pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 
                       'ok', 'ok', 'ok', 'poor', 'poor'],
               columns=["Grades"])
    
    print(df['Grades'].astype('category').head())
    
    my_categories=pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], 
                           ordered=True)
    grades=df["Grades"].astype(my_categories)
    print(grades)
    print(grades[grades>"C"])
    
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\census.csv')
    df=df[df['SUMLEV']==50]
    df=df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg('mean')
    
    print(print(df.head()))
    print(pd.cut(df,10))


def pivotTable():
    df = pd.read_csv(r'python_projects\collection2\pandas\inputs\cwurData.csv')
    
    def create_category(ranking):
        if (ranking >= 1) & (ranking <= 100):
            return "First Tier Top Unversity"
        elif (ranking >= 101) & (ranking <= 200):
            return "Second Tier Top Unversity"
        elif (ranking >= 201) & (ranking <= 300):
            return "Third Tier Top Unversity"
        return "Other Top Unversity"
    
    df['Rank_Level'] = df['world_rank'].apply(lambda x: create_category(x))
    
    pivot=df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max], 
               margins=True)
    print(pivot)
    print(pivot['mean', 'First Tier Top Unversity'].max())
    print(pivot['mean', 'First Tier Top Unversity'].idxmax())
    print(pivot.head())
    print(pivot.stack().head())
    print(pivot.unstack().head())


def datetimeFunctionality():
    print(pd.Timestamp('9/1/2019 10:05AM'))
    print(pd.Timestamp(2019, 12, 20, 0, 0))
    print(pd.Timestamp(2019, 12, 20, 0, 0).isoweekday())
    print(pd.Timestamp(2019, 12, 20, 0, 0).year)
    
    print(pd.Period('3/5/2016'))
    print(pd.Period('1/2016') + 5)
    
    d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
    ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
    ts3.index = pd.to_datetime(ts3.index, format='mixed')
    print(ts3)
    print(pd.to_datetime('4.7.12', dayfirst=True))
    
    print(pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016'))
    print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3h'))

    print(pd.Timestamp('9/4/2016').weekday())
    print(pd.Timestamp('9/4/2016') + pd.offsets.Week())
    print(pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd())
    
    print(pd.date_range('10-01-2016', periods=9, freq='2W-SUN'))
    print(pd.date_range('10-01-2016', periods=9, freq='B'))
    print(pd.date_range('10-01-2016', periods=9, freq='QS-JUN'))

    dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
    df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
    
    print(df.diff())
    print(df.resample('ME').mean())
    print(df['2016-12':])
    

if __name__ == '__main__':
    # mergingDataFrames()
    # groupBy()
    # scales()
    # pivotTable()
    datetimeFunctionality()