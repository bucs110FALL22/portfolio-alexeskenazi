class Rectangle:
    # constructor
    def __init__(self, x, y, h, w):
        '''
        constructor
        x: (int) the x coordinate of its upper left position
        y: (int) the y coordinate of its upper left position
        h: (int) the height of the rectangle
        w: (int) the width of the rectangle
        '''

        if x > 0:
            self.x = x
        else:
            self.x = 0
         
        if y > 0:
            self.y = y
        else:
            self.y = 0

        if h > 0:
            self.height = h
        else:
            self.height = 0

        if w > 0:
            self.width = w
        else:
            self.width = 0    

    def __str__(self):
        '''
        convert to string
        return (str) a string representation of the object.
        '''
        return '(x: ' + str(self.x) + ', y: ' + str(self.y) + '), width: ' + str(self.height) + ', height: ' + str(self.width) + ')'


r1 = Rectangle(10, 20, 100, 200)
print(r1)

r2 = Rectangle(-10, -20, -100, -200)
print(r2)