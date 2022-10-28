import turtle
import math
import random

MIN_NUMBER_OF_SIDES = 3


def calc_polygon_theta_angle(num_sides: int = MIN_NUMBER_OF_SIDES, num_vertex = 0) -> float: 
    '''
    Calculates the the angle of the given vertex for a polygon of with num_sides 
    num_sides: (int) Number of sides in the polygon
    num_vertex: (int) indicates which vertex of the polygon to use for the calculation
    return: (float) Vertex angle
    '''
    return (2.0 * math.pi * (num_vertex)) / num_sides


def set_initial_turtle_position(turtle_obj = None, x: int = 0, y: int = 0):
    '''
    Sets the initial position of the turtle without drawing a line.
    turtle_obj: (Turtle) Turtle object
    x: (int) initial horizontal coordinate
    y: (int) initial vertical coordinate
    '''
    turtle_obj.penup()
    turtle_obj.setposition(x, y)
    turtle_obj.pendown()


def set_pen_parameters(turtle_obj = None, color: str = 'red', pen_width: int = 1):
    '''
    Sets the color and line width of the turtle
    turtle_obj: (Turtle) Turtle object
    color: (str) Color of the lines.
    pen_width: (int) Width of the drawing pen
    '''
    turtle_obj.pencolor(color)
    turtle_obj.width(pen_width)


def draw_shape(turtle_obj = None, num_sides: int = MIN_NUMBER_OF_SIDES, side_length: int = 30, color: str = 'red'):
    '''
    Draws a regular polygon
    turtle_obj: (Turtle) Turtle object
    num_sides: (int) Number of sides of the polygon to draw
    side_length: (Turtle) Length of the polygon side
    color: (str) Color of the lines.
    '''
    offset = 50
    intial_x = side_length + offset
    intial_y = 0
    set_initial_turtle_position(turtle_obj, intial_x, intial_y)
    set_pen_parameters(turtle_obj, color, pen_width = 8)
    for i in range(num_sides + 1):
        theta = calc_polygon_theta_angle(num_sides, i)
        x = side_length * math.cos(theta) + offset
        y = side_length * math.sin(theta)
        turtle_obj.goto(x,y)


def draw_shape_rainbow(turtle_obj = None, color_offset: int  = 0): 
    '''
    Draws a set of polygons of increasing number of sides with increasing side
    lenght in different colors.
    turtle_obj: (Turtle) Turtle object
    '''
    colors = ['violet', 'indigo', 'blue', 'green', 'orange', 'pink', 'red']
    side_length = 0
    min_sides_in_polygon = 3
    max_sides_in_polygon = 15
    for n in range(min_sides_in_polygon, max_sides_in_polygon):
        side_length += 10
        number_of_sides = n
        color = colors[(number_of_sides + color_offset) % len(colors)]
        draw_shape(turtle_obj, number_of_sides, side_length, color)


def main():
    turtle_obj = turtle.Turtle()
    duration_cycles = 4
    for count in range(duration_cycles):
        color_offset =random.randrange(1,5)
        draw_shape_rainbow(turtle_obj, color_offset)
    turtle.exitonclick()


main()
