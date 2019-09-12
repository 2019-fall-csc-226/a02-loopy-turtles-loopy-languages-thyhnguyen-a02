######################################################################
# Author: Thy H. Nguyen
# Username: nguyent2

# Assignment: A02: Exploring Turtles in Python
# Purpose: Draws a 3D cube using turtles and nested for loops

#Citation:

# https://stackoverflow.com/questions/29441237/how-to-draw-a-semicircle-in-python-turtle-only
# https://stackoverflow.com/questions/46695126/how-to-draw-circle-using-turtle-in-python-3
# https://www.w3schools.com/colors/colors_picker.asp
# Getting color background from https://www.w3schools.com/colors/colors_picker.asp
# https://docs.python.org/3.3/library/turtle.html?
# http://cs.berea.edu/courses/csc226book/
######################################################################


import turtle
from math import pi
import random

wns = turtle.Screen()

def Set_up_shape(bichthuy):
    """
    This function just sets up the turtle ready to draw a lot of circles.
    :param bichthuy:
    :return:none
    """

    bichthuy.shape("circle")  # Set up the shape of the turtle
    bichthuy.shapesize(0.1, 0.1)  # Set up the pensize for the shapesize of the turtle
    bichthuy.speed(0)  # Set up turtle's speed
    bichthuy.pensize(6)  # Set up turtle's pensize



    def Draw_Circle(number, cao):
        """
        This function draws a full circle (which serves as a wheel in a car)
        :param number:
        :param cao:
        :return: none
        """
        for i in range(number):
            bichthuy.right(1) #Set up turtle turn right 1 degrees to draw a circle
            bichthuy.forward(cao) #Set up turtle to forward the number input

    def Complete_The_Circle_To_Put_Pen_Back(solieu, chieucao):
        """
        This function draws backward of a circle, to connect to the next step
        :param solieu:
        :param chieucao:
        :return: none
        """
        for i in range(solieu):
            bichthuy.left(1)  # Set up turtle turn left 1 degrees
            bichthuy.backward(chieucao)  # Set up turtle forward the number input

    # Call the function to draw wheels (inside another function)
    Draw_Circle(360, 0.5)
    Complete_The_Circle_To_Put_Pen_Back(90, 0.5)
    bichthuy.left(90)
    bichthuy.forward(40)
    bichthuy.right(90)
    Draw_Circle(180, 2.5)
    bichthuy.right(90)
    bichthuy.forward(40)
    bichthuy.right(-90)
    Draw_Circle(360, 0.5)
    Complete_The_Circle_To_Put_Pen_Back(180, 0.5)
    bichthuy.left(90)
    bichthuy.forward((900/pi)-80-(360/pi)) #Keep to the next car


def Draw_Car_And_Fill_Car(mauu, yuri,ngoc):
    """
    This function draws a whole car and fill it
    :param mauu:
    :param yuri:
    :return: none
    """
    ngoc.color("#000080")  # Set color for turtle
    ngoc.fillcolor(yuri)  # Set fill color for turtle
    ngoc.penup()  # Set penup
    ngoc.forward(mauu)  # Set turtle forward
    ngoc.pendown()
    ngoc.begin_fill()  # Set up turtle to begin fill the color
    Set_up_shape(ngoc)
    ngoc.end_fill()


#Create a list for color's random choice
lan_nay_1 = random.choice(["#00e600", "#00cc7a"])
lan_nay_2 = random.choice(["#00e600", "#00cc7a"])
lan_nay_3 = random.choice(["#00e600", "#00cc7a"])
lan_nay_4 = random.choice(["#00e600", "#00cc7a"])
lan_nay_5 = random.choice(["#00e600", "#00cc7a"])
lan_nay_6 = random.choice(["#00e600", "#00cc7a"])
lan_nay_7 = random.choice(["#00e600", "#00cc7a"])
lan_nay_8 = random.choice(["#00e600", "#00cc7a"])

def Draw_The_Two_Points(brother,abcxyz):
    """
    This function draws a two point, of a line to ask for calculating the length
    :param brother:
    :return: none
    """

    abcxyz.color("#ffff00")  # Set up color for turtle
    abcxyz.shape("circle")  # Set up shape for turtle
    abcxyz.shapesize(0.1, 0.1)  # Set up shapesize for turtle
    abcxyz.pensize(6)  # Set up pensize for turtle
    abcxyz.penup()  # Set turtle's pen up
    abcxyz.forward(brother)  # Set up forward
    abcxyz.right(90)  # Turtle turn right
    abcxyz.forward(90 / pi)  # Turtle go forward
    abcxyz.pendown()
    abcxyz.dot()




def Name_The_Two_Points(chieu_rong, chu_cai,thy):
    """
    This function appears the point A and B
    :param chieu_rong:
    :param chu_cai:
    :return:
    """

    thy.color("#660066")
    thy.pensize(6)
    thy.penup()
    thy.forward(chieu_rong)
    thy.right(90)
    thy.forward(90)
    thy.pendown()
    thy.write(chu_cai, move=False, align="center", font=("TimesNewRoman", 40, "bold"))



def Ask_Question_And_Reply(soluong, vietchu, jordan):
    """
    This function asks questions, and appears user's answer
    :param soluong:
    :param vietchu:
    :return: none
    """

    jordan.color("#660066")
    jordan.pensize(6)
    jordan.penup()
    jordan.left(90)
    jordan.forward(soluong)
    jordan.right(90)
    jordan.forward(0)
    jordan.pendown()
    jordan.write(vietchu, move=False, align="center", font =("TimesNewRoman",40,"bold") )



def main():
    """
    This function calls all other functions
    :return:
    """
    wns.bgcolor("#e6ffff")
    ngoc = turtle.Turtle()

    Draw_Car_And_Fill_Car(3 * 150, lan_nay_1,ngoc) #The distance of each car
    Draw_Car_And_Fill_Car(1 * 150, lan_nay_2,ngoc)
    Draw_Car_And_Fill_Car(-1 * 150, lan_nay_3,ngoc)
    Draw_Car_And_Fill_Car(-3 * 150, lan_nay_4,ngoc)
    Draw_Car_And_Fill_Car(-4 * 150, lan_nay_5,ngoc)
    Draw_Car_And_Fill_Car(-2 * 150, lan_nay_6,ngoc)
    Draw_Car_And_Fill_Car(0 * 150, lan_nay_7,ngoc)
    Draw_Car_And_Fill_Car(2 * 150, lan_nay_,8,ngoc)

    abcxyz = turtle.Turtle()
    Draw_The_Two_Points(-4 * 150 - 90 / pi, abcxyz)
    Draw_The_Two_Points(3 * 150 + 90 / pi + 900 / pi - 180 / pi - 80, abcxyz)

    conrua = turtle.Turtle()
    conrua.color("#ffff00")
    conrua.shape("circle")
    conrua.shapesize(0.1, 0.1)
    conrua.pensize(6)
    conrua.penup()
    conrua.forward(-4 * 150 - 90 / pi)  # Set up the pen to the starting point
    conrua.right(90)
    conrua.forward(90 / pi)
    conrua.left(90)
    conrua.pendown()
    conrua.forward(((900 / pi) - (80 + 180 / pi)) * 8 + 180 / pi)  # Draw the line needed

    #Call the name the two points to name them
    Name_The_Two_Points(-4 * 150 - 45, "A", thy)
    Name_The_Two_Points(4 * 150 + 50, "B", thy)


    Ask_Question_And_Reply(210, "What do you want the length of AB to be ?", jordan)

    # This answer variable asks for the user's input
    answer = wns.numinput("Can you give me any number of the length of AB ?", "Your answer:  ", default=None, minval=0,
                          maxval=10000000)

    Ask_Question_And_Reply(150, answer, jordan)

main()

wns.exitonclick()