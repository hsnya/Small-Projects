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
import numpy


def reshaping():
    a = numpy.array([0,1,2,3,4,5])
    b = numpy.array([[0, 1],
                    [2, 3],
                    [4, 5]])
    c = numpy.array([[0,1,2],
                    [3,4,5]])
    
    print(a.ndim)
    print(b.ndim)
    print(c.ndim)
    print(a.shape)
    print(b.shape)
    print(c.shape)
    
    a = a.reshape(6, 1)
    b = b.reshape(2, 3)
    c = c.reshape(1, 6)

    print(a.shape)
    print(b.shape)
    print(c.shape)
    

def filling():
    a = numpy.ones((3,3))
    b = numpy.zeros((3,3))
    c = numpy.random.rand(3,3)
    d = numpy.arange(2,11,2)
    e = numpy.linspace(0, 11, 12, (4,3))
    f = numpy.full((10,10), 20)
    
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    

def operations():
    a = numpy.array([[1,2],
                        [3,4]])
    b = numpy.array([[4,3],
                        [2,1]])
    
    c = a + b
    print(c)
    
    c = a - b
    print(c)
    
    c = a * b
    print(c)
    
    c = a / b
    print(c)
    
    c = a % b
    print(c)
    
    c = a // b
    print(c)
    
    c = a ** b
    print(c)
    
    c = a @ b
    print(c)
    
    c = a > b
    print(c)
    
    c = a == b
    print(c)
    
    print(a.sum())
    print(a.mean())
    print(a.min())
    print(a.max())
    

def indexing():
    a = numpy.arange(100).reshape(10, 10)
    print(a)
    print(a[0])
    print(a[0,0])
    print(a[1,[0,2,5]])
    print(a[[5,2,0],[0,2,5]])
    print(a[a > 50])
    
    print(a[:3])
    print(a[:,5:7])
    print(a[[0, 4, 6],5:7])
    b = numpy.genfromtxt('python_projects/collection2/numpy/inputs/Admission_Predict.csv', delimiter=',', skip_header=1,
                            names=('Serial No.','GRE Score','TOEFL Score','University Rating','SOP','LOR','CGPA','Research','Chance of Admit'))
    print(b['CGPA'][:5])
    

def tself():
    a = numpy.arange(100).reshape(10, 10)
    print(a.T)


if __name__ == '__main__':
    # reshaping()
    # filling()
    operations()
    # indexing()
    # tself()    