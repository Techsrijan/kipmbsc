x=10  #global
c=500
def msg():
    c=5
    global y   # local to global
    y=50
    a=globals()['c']
    print("Local c=",c) #local
    print(a)

msg()

print("x=",x)

print("c=",c)

print("Y=",y)