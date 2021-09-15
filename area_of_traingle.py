from math import *
a=int(input("Enter First side of traingle"))
b=int(input("Enter second side of traingle"))
c=int(input("Enter third side of traingle"))
print("a=",a)
print("b=",b)
print("c=",c)

s=(a+b+c)/2
print("S=",s)
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("area=",area)