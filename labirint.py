import turtle 

wn = turtle.Screen()
wn.bgpic('labirint.gif')
mouse = turtle.Turtle()
mouse.up()
mouse.color('red')
mouse.width(2)
mouse.goto(-300, 30)

mouse.down()
mouse.fd(40)

wn.exitonclick()



