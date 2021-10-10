from turtle import *
t=Turtle()

t.up()
#t.fd(100)
t.goto(100,50)
t.down()
t.circle(100)
#t.reset()
t.undo()
t.circle(-100)
t.pencolor("red")
t.circle(100,steps=10)
t.color("green")
t.begin_fill()

t.end_fill()
done()