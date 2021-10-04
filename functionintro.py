
# function definition
def greet():
    print("Good Morning")


greet() # function call
greet()
print("dekho fuction kaise kaam karta hi")
greet()


a,b=5,6
c=a+b
print(c)

'''
def add():
    a, b = 5, 6
    c = a + b
    print(c)

add()

'''

def add(x,y):
    c=x+y
    print(c)

add(2,3)
add(8,10)
add(4,6)


def zod(x,y):
    c=x+y
    return c


a=zod(6,8)
print("Add=",a)



p=int(input("enter any number"))
q=int(input("enter any number"))
b=zod(p,q)
print("sum=",b)

print(zod(90,100))

def calci(c,d):
    x=c+d
    y=c-d
    return x,y

s,t=calci(44,6)

print("Sum=",s)
print("Sub=",t)