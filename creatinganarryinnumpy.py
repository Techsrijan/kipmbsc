from numpy import *

'''
There are six ways to create an array using numpy
1.array()
2.linspace
3.logspace
4.arange
5.zeros
6.ones
'''

arr=array([1,2,3,4])
print(arr)

arr2=linspace(1,15,15)  # bydefault 50 parts
print(arr2)

arr3=logspace(1,15,15)  # bydefault 50 parts
print(arr3)

arr4=arange(0,10,2)
print(arr4)

arr5=zeros(10,int)
print(arr5)

arr6=ones(100,int)
print(arr6)