from functools import *
l=[33,55,22,77,12,8,56,57]

f=lambda a:a%2==0

#print(f(4))
#even=list(filter(f,l))
even=list(filter(lambda a:a%2==0,l))
print(even)

val=list(map(lambda a:a+5,even))
print(val)

output=reduce(lambda a,b:a+b,val)
print(output)