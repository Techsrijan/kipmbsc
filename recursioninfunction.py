import sys
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(sys.getrecursionlimit()+990))
'''
when a function calls itself it is called recursion
'''
i=0
def msg():
    global i
    print('good morning=',i)
    i=i+1
    msg()

msg()
