#import array
from array import *
import time
arr=array('i',[1,2,3,4,5])
print(arr)

'''
for i in arr:
    print(i)
    time.sleep(1)
    
'''

print(arr[0])
print(len(arr))
print(arr.buffer_info())
print(arr.typecode)

for i in range(len(arr)):
    print(arr[i])


arr1=array('u',['a','n','t'])
print(arr1)

for i in arr1:
    print(i)

print(sum(arr))
print(max(arr))
print(min(arr))