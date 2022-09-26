#1. import modules
import turtle
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART pP A code goes here
print('PART A')

# RACE 1
print('Race 1 - Best single jump')
jump_michelangelo = random.randrange(0,100)
michelangelo.forward(jump_michelangelo)

jump_leonardo = random.randrange(0,100)
leonardo.forward(jump_leonardo)

print('Michelangelo = ' + str(jump_michelangelo))
print('Leonardo = ' + str(jump_leonardo))

if jump_michelangelo > jump_leonardo:
  print("Michelangelo Won!")
elif jump_michelangelo == jump_leonardo:
  print("They tied!")
else:
  print("Leonardo Won!")

print('_____________')
print('PART A')
  
#RACE 2

def InitializeRace2():
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)
  pos_michelangelo  = 0
  pos_leonardo = 0

print('Race 2 - Best of 10 jumps')
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
pos_michelangelo  = 0
pos_leonardo = 0

count = 0
while count < 10:
  jump_michelangelo = random.randrange(0,100)
  pos_michelangelo = pos_michelangelo + jump_michelangelo
  michelangelo.forward(jump_michelangelo)
  
  jump_leonardo = random.randrange(0,100)
  pos_leonardo = pos_leonardo + jump_leonardo
  leonardo.forward(jump_leonardo)

  count = count + 1
  
print('Michelangelo = ' + str(pos_michelangelo))
print('Leonardo = ' + str(pos_leonardo))

if pos_michelangelo > pos_leonardo:
  print("Michelangelo Won!")
elif pos_michelangelo == pos_leonardo:
  print("They tied!")
else:
  print("Leonardo Won!")

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
print('_____________')

# window.exitonclick()


# PART B - complete part B here
print('PART B')
pygame.init()
surface = pygame.display.set_mode((500,500))
pygame.display.set_caption('Part B')

def draw_shape(num_sides):
    side_length = 30
    offset = 50
    coordinates = []
    for i in range(num_sides):
        theta = (2.0 * math.pi * (i)) / num_sides
        x = side_length * math.cos(theta) + offset
        y = side_length * math.sin(theta) + offset
        coordinates.append((x,y))

    pygame.draw.polygon(surface, 'red', coordinates)
    pygame.display.flip()

wait_time = 1200

shapes_sides = [3,4,6,9,360]

for sides in shapes_sides:
    draw_shape(sides)
    pygame.time.wait(wait_time)
    surface.fill('black')


print('The End!')
surface.fill("black")
    
    

