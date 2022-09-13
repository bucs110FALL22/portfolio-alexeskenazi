import turtle
number_of_sides = int( input("Please input the # of sides: ") )
lenght_of_side = int( input("Please input the length of sides: ") )
turtle.shape("turtle")
turtle.color ("Red")
count = 0
while (count < number_of_sides):   
    count = count + 1
    turtle.forward (lenght_of_side)
    turtle.right (360/number_of_sides)
    
turtle.exitonclick()