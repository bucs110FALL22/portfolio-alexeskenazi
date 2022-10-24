
from Rectangle import Rectangle


class Surface:
    # constructor
    def __init__(self, filename: str, x, y, h, w):
        '''
        constructor
        filename: (str) image file name
        x: (int) the x coordinate of its upper left position
        y: (int) the y coordinate of its upper left position
        h: (int) the height of the rectangle
        w: (int) the width of the rectangle
        '''
        self.image = filename
        self.rect = Rectangle(x, y, h, w)

    def getRect(self):
        '''
        getter for the rect
        return: (Rectangle) rect for the surface
        '''
        return self.rect


r1 = Rectangle(10, 20, 100, 200)
print(r1)

r2 = Rectangle(-10, -20, -100, -200)
print(r2)