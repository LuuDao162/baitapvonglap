import turtle
 
t = turtle.Turtle()
t.pensize(2)
t.pencolor("brown")
t.penup()
t.goto(0,0)
t.pendown()

d = int(input("Nhập vào giá trị d: "))
step = 0
while (t.distance(0,0) < d):
    step += 0.1
    t.forward(step)
    t.left(15)

