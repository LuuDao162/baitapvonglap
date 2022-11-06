import turtle

turtle.bgcolor("black")
turtle.speed(0)
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
for x in range(37):
    for val in range (2):
        turtle.circle(100,90)
        turtle.circle(50,90)
        
    turtle.pencolor(colors[x%6])
    turtle.right(10)    
turtle.done()