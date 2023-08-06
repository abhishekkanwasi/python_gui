from turtle import *
import random
import time

wn = Screen()
wn.setup(600,700)

# position locator
pos = Turtle()
pos.hideturtle()
def show_pos(x,y):
    print(x,y)

wn.listen()
wn.onclick(show_pos)


ck = Turtle()
ck.hideturtle()
ck.pensize(5)
ck.up()
ck.goto(-200,-350)
ck.down()

ck.speed(0)
ck.pencolor("pink")
ck.setheading(110)
ck.forward(30) #leg1
ck.setheading(250)
ck.forward(30) #leg2
ck.backward(30)
ck.setheading(90)
ck.forward(20) #back
ck.left(150)
ck.forward(20) #arm1
ck.backward(20)
ck.right(300)
ck.forward(20) #arm2
ck.backward(20)
ck.setheading(90)
ck.forward(5) #neck
ck.circle(6) #head

bk = Turtle()
bk.hideturtle()
bk.speed(0)
bk.color("yellow")
for i in range(30):
    bk.up()
    bk.goto(random.randint(-300,300),random.randint(50,300))
    bk.down()
    for i in range(5):
        bk.forward(10)
        bk.left(216)
        
ak = Turtle()
ak.hideturtle()
a=["green","yellow","orange","pink","blue","cyan","magenta","brown","purple","violet","indigo"]

ak.speed(0)
ak.goto(0,-80)
c=-80
for i in range(10,0,-1):
    ak.goto(0,c)
    c-=10
    ak.begin_fill()
    ak.fillcolor(a[i])
    ak.circle(i*20)
    ak.end_fill()

ak.pensize(5)
ak.pencolor("blue")
ak.setheading(270)
ak.forward(20)

ak.pencolor("yellow")
ak.setheading(0)
ak.forward(20)
ak.right(90)
ak.forward(20)
ak.right(90)
ak.forward(40)
ak.right(90)
ak.forward(20)
ak.right(90)
ak.forward(20)

ak.color("yellow")

dk = Turtle()
dk.pensize(4)
dk.color("pink")
dk.hideturtle()
dk.up()
dk.goto(-20,-186)
dk.down()

dk.setheading(90)
dk.forward(10)
dk.circle(4)

dk.setheading(240)
dk.forward(14)

time.sleep(1)
wn.bgcolor("black")

time.sleep(5)
    
