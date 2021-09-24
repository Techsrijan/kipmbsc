from numpy import *
arr=array([
    [1,2,3],
    [3,5,6],
    [7,8,9],
    [8,8,6]
])

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)
print(arr.flatten())
print(arr.reshape(3,4))
print(arr.reshape(2,2,3))

arr2=array([
    [1,2,3,1],
    [3,5,6,1],
    [7,8,9,1],

])

#arr3=arr+arr2
#print(arr3)

arr4=dot(arr,arr2)
print(arr4)

arr5=arr@arr2
print(arr5)