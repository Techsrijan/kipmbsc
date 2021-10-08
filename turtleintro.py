from turtle import *
def shape():
    t.forward(100)
    t.left(90)
t=Turtle() # creating turtlr class object
'''
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''
'''
t.pencolor('red')
t.fillcolor('green')
'''
t.pensize(10)
t.speed(6)
t.shape('turtle')
t.hideturtle()
t.color('blue','yellow')
t.begin_fill()
for i in range(4):
    shape()
t.end_fill()

t.penup()
t.right(90)
t.forward(100)
t.pendown()
for i in range(4):
    shape()

t.reset()

for i in range(5):
    t.forward(100)
    t.left(216)
t.pencolor('red')
t.write("Mera Program",font=("Comic Sans Ms",25,"bold"))
done()