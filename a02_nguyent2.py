# Written by Thy H. Nguyen

#Citation:

# https://stackoverflow.com/questions/29441237/how-to-draw-a-semicircle-in-python-turtle-only
# https://stackoverflow.com/questions/46695126/how-to-draw-circle-using-turtle-in-python-3
# https://www.w3schools.com/colors/colors_picker.asp
# Getting color background from https://www.w3schools.com/colors/colors_picker.asp
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#



import turtle
from math import pi
import random

def main():

    wns = turtle.Screen()

    def banh_xe(bichthuy):
        bichthuy.shape("circle")
        bichthuy.shapesize(0.1,0.1)
        bichthuy.speed(10)
        bichthuy.pensize(6)

        def ve_hinh_tron(number,cao):
            for i in range(number):
                bichthuy.right(1)
                bichthuy.forward(cao)

        def ve_tron(solieu, chieucao):
            for i in range(solieu):
                bichthuy.left(1)
                bichthuy.backward(chieucao)

        ve_hinh_tron(360, 0.5)
        ve_tron(90, 0.5)
        bichthuy.left(90)
        bichthuy.forward(40)
        bichthuy.right(90)
        ve_hinh_tron(180,2.5)
        bichthuy.right(90)
        bichthuy.forward(40)
        bichthuy.right(-90)
        ve_hinh_tron(360, 0.5)
        ve_tron(180, 0.5)
        bichthuy.left(90)
        bichthuy.forward((900/pi)-80-(360/pi))

    wns.bgcolor("#e6ffff")

    def annyong(mauu, yuri):
        ngoc = turtle.Turtle()
        ngoc.color("#000080")
        ngoc.fillcolor(yuri)
        ngoc.penup()
        ngoc.forward(mauu)
        ngoc.pendown()
        ngoc.begin_fill()
        banh_xe(ngoc)
        ngoc.end_fill()

    lan_nay_1 = random.choice(["#00e600", "#00cc7a"])
    lan_nay_2 = random.choice(["#00e600", "#00cc7a"])
    lan_nay_3 = random.choice(["#00e600", "#00cc7a"])
    lan_nay_4 = random.choice(["#00e600", "#00cc7a"])
    lan_nay_5 = random.choice(["#00e600", "#00cc7a"])
    lan_nay_6 = random.choice(["#00e600", "#00cc7a"])
    lan_nay_7 = random.choice(["#00e600", "#00cc7a"])
    lan_nay_8 = random.choice(["#00e600", "#00cc7a"])

    annyong(3 * 150, lan_nay_1)
    annyong(1 * 150, lan_nay_2)
    annyong(-1 * 150, lan_nay_3)
    annyong(-3 * 150, lan_nay_4)
    annyong(-4 * 150, lan_nay_5)
    annyong(-2 * 150, lan_nay_6)
    annyong(0*150, lan_nay_7)
    annyong(2*150, lan_nay_8)

    def nut_that(brother):
        abcxyz = turtle.Turtle()
        abcxyz.color("#ffff00")
        abcxyz.shape("circle")
        abcxyz.shapesize(0.1, 0.1)
        abcxyz.pensize(6)
        abcxyz.penup()
        abcxyz.forward(brother)
        abcxyz.right(90)
        abcxyz.forward(90/pi)
        abcxyz.pendown()
        abcxyz.dot()

    nut_that(-4*150-90/pi)
    nut_that(3*150+90/pi+900/pi-180/pi-80)

    conrua = turtle.Turtle()
    conrua.color("#ffff00")
    conrua.shape("circle")
    conrua.shapesize(0.1, 0.1)
    conrua.pensize(6)
    conrua.penup()
    conrua.forward(-4*150-90/pi)
    conrua.right(90)
    conrua.forward(90/pi)
    conrua.left(90)
    conrua.pendown()
    conrua.forward(((900/pi)-(80+180/pi))*8+180/pi)

    def dau_cuoi_tuong_ung(chieu_rong, chu_cai):
        thy = turtle.Turtle()
        thy.color("#660066")
        thy.pensize(6)
        thy.penup()
        thy.forward(chieu_rong)
        thy.right(90)
        thy.forward(90)
        thy.pendown()
        thy.write(chu_cai, move=False, align="center", font=("TimesNewRoman", 40, "bold"))

    dau_cuoi_tuong_ung(-4*150-45,"A")
    dau_cuoi_tuong_ung(4*150+50, "B")

    answer = wns.numinput("Can you calculate the length of AB ?", "Your answer:  ", default=None, minval=0,
                          maxval=10000000)

    def written(soluong, vietchu):
        jordan = turtle.Turtle()
        jordan.color("#660066")
        jordan.pensize(6)
        jordan.penup()
        jordan.left(90)
        jordan.forward(soluong)
        jordan.right(90)
        jordan.forward(0)
        jordan.pendown()
        jordan.write(vietchu, move=False, align="center", font =("TimesNewRoman",40,"bold") )

    written(210, "Can you calculate the length of AB ?")
    written(150, answer)



    wns.exitonclick()

main()