from turtle import *
t=Turtle()
l=['red','green','yellow','blue','orange']
t.up()
t.goto(300,0)
t.down()
t.pensize(5)
for i in range(5):
    t.pencolor(l[i])
    t.circle(100)
    t.up()
    t.bk(200)
    t.down()
done()