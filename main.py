import turtle
from turtle import Turtle, Screen
from random import randint, choice
import colorgram

######### EXTRACT COLORS FROM COLORGRAM ##############
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 32)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(219, 254, 237), (84, 254, 155), (173, 146, 118), (254, 250, 254), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (244, 248, 254), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]
turtle.colormode(255)
toe = Turtle()
toe.shape("turtle")
toe.pensize(10)
toe.speed("fastest")
toe.penup()
toe.hideturtle()
# toe.color("slate blue")


# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     color_scheme = (r, g, b)
#     return color_scheme

# for _ in range(4):
#     toe.fd(100)
#     toe.right(90)
#

######## DASHED LINE ######
# for _ in range(50):
#     toe.fd(10)
#     toe.penup()
#     toe.fd(10)
#     toe.pendown()


# turtle_power = {
#     3: "AntiqueWhite2",
#     4: "DarkSeaGreen3",
#     5: "DarkMagenta",
#     6: "brown1",
#     7: "DeepSkyBlue",
#     8: "gray60",
#     9: "pink1",
#     10: "LightSteelBlue1",
# }
#
# which_way = [0, 90, 180, 270]

################ PATTERN WALK (TRIANGLE, SQUARE...ETC) ##############
# for keys in turtle_power:
#     lines = keys
#     toe.color((turtle_power[keys]))
#     for _ in range(lines):
#         toe.forward(100)
#         toe.right(360/lines)


########### RANDOM WALK ############
# for _ in range(250):
#     toe.fd(25)
#     toe.seth(choice(which_way))
#     toe.color(random_color())

############# DRAW A SPIROGRAPH #############
# def draw_spirograph(size):
#     for _ in range(int(360/size)):
#         toe.color(random_color())
#         toe.circle(100)
#         toe.seth(toe.heading() + size)
#
#
# draw_spirograph(5)

toe.seth(225)
toe.fd(300)
toe.seth(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    toe.dot(20, choice(color_list))
    toe.fd(50)

    if dot_count % 10 == 0:
        toe.seth(90)
        toe.fd(50)
        toe.seth(180)
        toe.fd(500)
        toe.seth(0)




screen = Screen()
screen.exitonclick()