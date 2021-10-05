def person(name,age):
    print("name=",name)
    age=age+10
    print("age=",age)
#postional arguments
person('ram',66)

#person(88,'abcd')

'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument 
4. keyword variable length argument 
'''

#keyword argument

person(name="Mohan",age=50)

person(age=52,name="rohan")

'''
def add(x,y):
    c=x+y
    print(c)

add(5,7)

def add2(x,y,z):
    c=x+y+z
    print(c)
    
add2(4,6,8)
'''

#variable length argument
def add(a,*b):
    print(a)
    print(b)
    sum=a
    for i in b:
        #print(i)
        sum=sum+i
    print(sum)


add(5,5,5,7,8,9,0,5,3,7,0,9)

def add1(*b):
    print(b)
    sum=0
    for i in b:
        #print(i)
        sum=sum+i
    print(sum)


add1(5,5,5,7,8,9,0,5,3,7,0,9)
#keyword variable length argument
def persondata(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,'=',j)

#persondata('ram','ayodhya',66,95965466,24852,'dashrath')

persondata(name='ram',age=100,city='ayodhya',pin=5656,contact=56636)