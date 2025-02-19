
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()  
 


tina.forward(200)
tina.left(90)
tina.color('green')
tina.circle(100)
tina.circle(90)
tina.color('blue')
tina.circle(80)
tina.circle(70)
tina.color('yellow')
tina.circle(60)
tina.circle(50)
tina.color('green')
tina.circle(40)
tina.circle(30)

tina.circle(20)
tina.circle(10)

tina.circle(5)
tina.circle(4)

tina.circle(3)
tina.circle(2)

tina.circle(1)
tina.circle(0)








turtle.exitonclick()