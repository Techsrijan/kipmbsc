from turtle import *
t=Turtle()
wn=Screen()
def go():
    t.forward(100)

def test():
    t.backward(200)
    for i in range(5):
        #t.stamp()
        t.write("hi")


wn.listen()
wn.onkey(go,'Up')
wn.onkey(test,'D')


done()