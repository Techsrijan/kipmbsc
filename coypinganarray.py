from numpy import *
arr=array([1,2,3,4,5])
#aliasing
arr2=arr
print(arr,id(arr))
print(arr2,id(arr2))
# change in one affects another
arr[0]=100
print(arr,id(arr))
print(arr2,id(arr2))

# what if u want 2 different address
#shallow copy
# view
arr3=array([4,5,6,7])
arr4=arr3.view()
print(arr3,id(arr3))
print(arr4,id(arr4))
arr4[0]=500
print(arr3,id(arr3))
print(arr4,id(arr4))

# what if u want 2 different address and change of one does not affext other
#deep copy
#copy
arr5=array([33,4,6,7])
arr6=arr5.copy()
print(arr5,id(arr5))
print(arr6,id(arr6))
arr5[0]=900
print(arr5,id(arr5))
print(arr6,id(arr6))