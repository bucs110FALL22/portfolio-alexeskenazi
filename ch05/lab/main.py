import pygame
import os

# Lab 5
# Part A  - no counter
print('Lab 5 - Part A - 3n+1 sequence no counter')
n_initial = 101
n = n_initial

while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    print('n = ' + str(n))


print('------------------')

# Part B  - with counter
print('Lab 5 - Part B - 3n+1 sequence with counter')

# Refactoring to Track a Range of Iterations


def get_next_n(n_current):
    if n_current % 2 == 0:
        n_new = n_current / 2
    else:
        n_new = 3 * n_current + 1
    return n_new

def text_objects(text, font):
    textSurface = font.render(text, True, 'white')
    return textSurface, textSurface.get_rect()


def display_text(text, size, center):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = center
    surface.blit(TextSurf, TextRect)


n_initial = 101
n = n_initial
count = 0
while n != 1:
    count = count + 1
    n = get_next_n(n)
    print('n(' + str(n_initial) + ', ' + str(count) + ') = ' + str(n))

print('count = ' + str(count))


print('------------------')

# Part B  - Checking a Range
print('Lab 5 - Part B - 3n+1 Checking a Range')

# Refactoring to Track a Range of Iterations

upper_limit = 20
iters = {}

start = 2
while start < upper_limit:
    n = start
    count = 0
    while n != 1:
        count = count + 1
        n = get_next_n(n)
        # print('n(' + str(start) + ', ' + str(count) + ') = ' + str(n))
    print('count = ' + str(count))
    iters[start] = count
    start = start + 1

print('threenplus1_iters_dict = ' + str(iters))


# PART C

print('Lab 5 - Part C - 3n+1 Checking a Range')

# Refactoring to Track a Range of Iterations

upper_limit = 20
iters = {}
max_so_far = 0

start = 2
while start < upper_limit:
    n = start
    count = 0
    while n != 1:
        count = count + 1
        n = get_next_n(n)
        # print('n(' + str(start) + ', ' + str(count) + ') = ' + str(n))
    print('count = ' + str(count))
    iters[start] = count
    if count > max_so_far:
        max_so_far = count
    start = start + 1


max_val = max_so_far
print('threenplus1_iters_dict = ' + str(iters))
print('max = ' + str(max_val))


def set_output_window_position():
    x = 100
    y = 0
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x, y)


pygame.init()
surface = pygame.display.set_mode((400, 200))
pygame.display.set_caption('3N+1 N vs Iteraction Count')

display_size = surface.get_size()
x_display = display_size[0]
y_display = display_size[1]
print('display_size: ' + str(x_display) + ',' + str(y_display))

axle_color = 'red'
graph_color = 'green'
axle_margin = x_display/10

y_horz_axle = y_display - axle_margin
left_horz_axle = (axle_margin, y_horz_axle)
right_horz_axle = (x_display - axle_margin, y_horz_axle)
top_vert_axle = (left_horz_axle[0], axle_margin)


def draw_axles():
    pygame.draw.line(
        surface,
        axle_color,
        left_horz_axle,
        right_horz_axle,
        width=2
    )
    pygame.draw.line(
        surface,
        axle_color, 
        left_horz_axle,
        top_vert_axle,
        width=2
    )


def display_max():
    text = 'Max: ' + str(max_val)
    display_text(text, 16, (axle_margin, axle_margin/2))

    
def draw_graph(points):
    x_scale = (x_display - 2 * axle_margin)/upper_limit
    y_scale = (y_display - 2 * axle_margin)/max_val
    print('x_scale = ' + str(x_scale))
    print('y_scale = ' + str(y_scale))
    points_tuple = []
   
    for point in points:
        p = (int(axle_margin + point[0] * x_scale), y_display - axle_margin - int(point[1] * y_scale))
        points_tuple.append(p)

    pygame.draw.lines(
        surface,
        graph_color,
        False,
        points_tuple
    )


draw_axles()
display_max()
draw_graph(iters.items())
pygame.display.flip()

wait_time = 5000
pygame.time.wait(wait_time)
print('The End!')
pygame.quit()
