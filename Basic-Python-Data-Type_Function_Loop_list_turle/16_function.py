#use turle and function to make a same length of a triangle

import turtle

def draw_trianle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# counter = 0
# while counter<4:
#     draw_trianle(100)
#     turtle.left(120)
#     counter +=1
draw_trianle(100)
turtle.exitonclick()
