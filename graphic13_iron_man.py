from turtle import *
import time
wn = Screen()

def show_pos(x,y):
    print(x,y)

wn.listen()
wn.onclick(show_pos)

ak = Turtle()
ak.speed(0)
ak.up()
ak.goto(0,-250)
ak.down()

ak.color("black")
ak.width(2)
ak.begin_fill()
ak.fillcolor("red")
ak.left(18)
ak.forward(75)
ak.left(20)
ak.forward(20)
ak.left(20)
ak.forward(60)
ak.left(15)
ak.forward(100)
ak.left(15)
ak.forward(160)
ak.backward(100)
ak.right(40)
ak.forward(15)
ak.left(44)
ak.forward(70)
ak.left(30)
ak.forward(11)
ak.right(36)
ak.forward(30)
ak.left(30)
ak.forward(45)
ak.circle(150,142)
ak.end_fill()
ak.hideturtle()

bk = Turtle()
bk.speed(0)
bk.up()
bk.goto(0,-250)
bk.down()

bk.color("black")
bk.width(2)
bk.begin_fill()
bk.fillcolor("red")
bk.setheading(180)

bk.right(18)
bk.forward(75)
bk.right(20)
bk.forward(20)
bk.right(20)
bk.forward(60)
bk.right(15)
bk.forward(100)
bk.right(15)
bk.forward(160)
bk.backward(100)
bk.left(40)
bk.forward(15)
bk.right(44)
bk.forward(70)
bk.right(30)
bk.forward(11)
bk.left(36)
bk.forward(30)
bk.right(30)
bk.forward(45)

bk.hideturtle()

bk.end_fill()

ck = Turtle()

ck.up()
ck.goto(0,-170)
ck.down()

ck.speed(0)
ck.begin_fill()
ck.fillcolor("yellow")
ck.forward(60)
ck.right(25)
ck.forward(40)
ck.left(100)
ck.forward(40)
ck.left(60)
ck.forward(35)
ck.right(60)
ck.forward(40)
ck.right(25)
ck.forward(80)
ck.left(65)
ck.forward(50)
ck.right(30)
ck.forward(80)
ck.left(90)
ck.forward(5)
ck.right(80)
ck.circle(100,70)

ck.left(100)
ck.forward(100)
ck.right(80)
ck.forward(50)
ck.end_fill()
ck.hideturtle()


dk = Turtle()

dk.up()
dk.goto(0,-170)
dk.down()

dk.speed(0)
dk.begin_fill()
dk.fillcolor("yellow")
dk.setheading(180)
dk.forward(60)
dk.left(25)
dk.forward(40)
dk.right(100)
dk.forward(40)
dk.right(60)
dk.forward(35)
dk.left(60)
dk.forward(40)
dk.left(25)
dk.forward(80)
dk.right(65)
dk.forward(50)
dk.left(30)
dk.forward(80)
dk.right(90)
dk.forward(5)

dk.left(80)
dk.circle(-100,70)

dk.right(100)
dk.forward(100)
dk.left(80)
dk.forward(50)
dk.end_fill()
dk.hideturtle()


ek = Turtle()

ek.speed(0)
ek.up()
ek.goto(0,-130)
ek.down()

ek.begin_fill()
ek.fillcolor("black")
ek.forward(60)
ek.right(50)
ek.forward(35)
ek.left(120)
ek.forward(26)
ek.left(70)
ek.forward(12)
ek.left(112)
ek.forward(17)
ek.right(130)
ek.forward(32)
ek.left(58)
ek.forward(65)
ek.end_fill()

ek.hideturtle()

fk = Turtle()

fk.speed(0)
fk.up()
fk.goto(0,-130)
fk.down()

fk.begin_fill()
fk.fillcolor("black")

fk.setheading(180)

fk.forward(60)
fk.left(50)
fk.forward(35)
fk.right(120)
fk.forward(26)
fk.right(70)
fk.forward(12)
fk.right(112)
fk.forward(17)
fk.left(130)
fk.forward(32)
fk.right(58)
fk.forward(65)
fk.end_fill()

fk.hideturtle()


gk = Turtle()
gk.speed(0)
gk.up()
gk.goto(0,-10)
gk.down()

gk.begin_fill()
gk.fillcolor("black")

gk.left(8)
gk.forward(60)
gk.left(20)
gk.forward(50)
gk.right(90)
gk.forward(25)
gk.right(75)
gk.forward(40)
gk.right(40)
gk.forward(50)
gk.right(45)
gk.forward(15)
gk.left(47)
gk.forward(30)

gk.end_fill()
gk.hideturtle()


hk = Turtle()
hk.speed(0)
hk.up()
hk.goto(0,-10)
hk.down()

hk.begin_fill()
hk.fillcolor("black")

hk.setheading(180)
hk.right(8)
hk.forward(60)
hk.right(20)
hk.forward(50)
hk.left(90)
hk.forward(25)
hk.left(75)
hk.forward(40)
hk.left(40)
hk.forward(50)
hk.left(45)
hk.forward(15)
hk.right(47)
hk.forward(30)

hk.end_fill()

hk.hideturtle()


ik = Turtle()
ik.speed(0)
ik.up()
ik.goto(35,-15)
ik.down()

ik.color("blue")

ik.begin_fill()
ik.fillcolor("cyan")
ik.left(16)
ik.forward(68)
ik.right(70)
ik.forward(8)
ik.right(95)
ik.forward(30)
ik.right(30)
ik.forward(45)
ik.right(60)
ik.forward(4)
ik.end_fill()

ik.hideturtle()


jk = Turtle()
jk.speed(0)
jk.up()
jk.goto(-35,-15)
jk.down()

jk.color("blue")

jk.setheading(180)
jk.begin_fill()
jk.fillcolor("cyan")
jk.right(16)
jk.forward(68)
jk.left(70)
jk.forward(8)
jk.left(95)
jk.forward(30)
jk.left(30)
jk.forward(45)
jk.left(60)
jk.forward(4)
jk.end_fill()

jk.hideturtle()


lk = Turtle()
lk.speed(0)
lk.up()
lk.goto(152,100)
lk.down()

lk.setheading(180)
lk.forward(34)
lk.left(80)
lk.forward(80)
lk.left(40)
lk.forward(22)
lk.left(95)
lk.forward(18)

lk.hideturtle()


mk = Turtle()
mk.speed(0)
mk.up()
mk.goto(-152,100)
mk.down()

mk.forward(34)
mk.right(80)
mk.forward(80)
mk.right(40)
mk.forward(22)
mk.right(95)
mk.forward(18)

mk.hideturtle()


nk = Turtle()
nk.speed(0)
nk.up()
nk.goto(92,-84)
nk.down()

nk.setheading(223)
nk.forward(50)
nk.left(32)
nk.forward(110)
nk.left(90)
nk.forward(30)
nk.backward(30)
nk.setheading(180)
nk.forward(30)

nk.hideturtle()


ok = Turtle()
ok.speed(0)
ok.up()
ok.goto(-92,-84)
ok.down()

ok.setheading(317)
ok.forward(50)
ok.right(32)
ok.forward(110)
ok.right(90)
ok.forward(30)
ok.backward(30)
ok.setheading(360)
ok.forward(30)

ok.hideturtle()

pk = Turtle()

pk.up()
pk.goto(108,-149)
pk.down()

pk.left(32)
pk.forward(26)

pk.hideturtle()


qk = Turtle()

qk.up()
qk.goto(-108,-149)
qk.down()

qk.setheading(180)
qk.right(32)
qk.forward(26)

qk.hideturtle()

rk = Turtle()

rk.up()
rk.goto(-331,81)
rk.down()

rk.color("red")
rk.write("Thank You !", font="courier 20 italic")

rk.hideturtle()


sk = Turtle()

sk.up()
sk.goto(-331,65)
sk.down()

sk.color("red")
sk.write("@abhishek kanwasi", font="courier 10 italic")

sk.hideturtle()


time.sleep(0.5)

for i in range(0,40):
    if i%2==0:
        wn.bgcolor("black")
        time.sleep(0.1)

    else:
        wn.bgcolor("white")
        time.sleep(0.1)


time.sleep(2)




