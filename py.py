import turtle
r = int(input("give radious"))
c = input("give color")
turtle.speed(0)
turtle.color(c)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.color("black")
khatrofol = 3.1416*(r*r)
turtle.write(khatrofol)
turtle.exitonclick()
