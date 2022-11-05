from Surface import Surface
from Rectangle import Rectangle

print('Testing Rectangle')
r = Rectangle(10, 10, 10, 10)
assert ((r.x, r.y, r.width, r.height) == (10, 10, 10, 10))
r = Rectangle(-1, 1, 1, 1)
assert ((r.x, r.y, r.width, r.height) == (0, 1, 1, 1))
r = Rectangle(1, -1, 1, 1)
assert ((r.x, r.y, r.width, r.height) == (1, 0, 1, 1))
r = Rectangle(1, 1, -1, 1)
assert ((r.x, r.y, r.width, r.height) == (1, 1, 0, 1))
r = Rectangle(1, 1, 1, -1)
assert ((r.x, r.y, r.width, r.height) == (1, 1, 1, 0))


print('Testing Surface')
s = Surface("myimage.png", 10, 10, 10, 10)
assert ((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10, 10, 10, 10))
srect = s.getRect()
assert (srect.x, s.getRect().y, srect.height, srect.width) == (10, 10, 10, 10)
assert s.image
print("Test Complete!")
