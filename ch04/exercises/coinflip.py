import turtle
import time
import random
screensize = 200
turtle.screensize(150,150)
print(turtle.screensize())
turtle.shape("turtle")
turtle.color('red')
run = True
while run:
  coin=random.randrange(0,2)
  if coin==1:
    turtle.left (90)
  else: 
    turtle.right (90)
  screensize = turtle.screensize()[0]
  turtle.forward (50)
  if turtle.position() [0] >= (screensize/2):
    run = False 
  if turtle.position()[0] <= (screensize/-2):
    run = False
  if turtle.position()[1]>(screensize/2):
    run = False 
  if turtle.position()[1]<(screensize/-2):
    run = False
  print(turtle.position())
turtle.exitonclick()
