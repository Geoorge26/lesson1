from turtle import *
#house

width(7)
color("green")
speed(15)
forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)



forward(200)
left(90)

#door


forward(70)
left(90)
color("yellow")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(200, 200)
pendown()
#roof 
color("red")
left(180)

begin_fill()
left(60)
forward(120)
left(60)
forward(115)
end_fill()
#windows
penup()
goto(200, 100)
pendown()
color("brown")
right(30)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
color("green")
penup()
goto(200,200)
pendown()

left(180)
forward(200)
left(90)

forward(60)
color("brown")

left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
penup()

exitonclick()






