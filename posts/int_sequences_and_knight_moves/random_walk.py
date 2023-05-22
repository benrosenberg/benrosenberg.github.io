from matplotlib import pyplot as plt
import random, math

N = 100000
m = 1
d = 4

def apply(direction, point):
    dx, dy = direction
    x, y = point
    return (x + dx, y + dy)

def norm(point):
    x, y = point
    return (x**2 + y**2)**0.5

def next_dir(point):
    x, y = point
    if x == 0 and y == 0:
        return random.uniform(-m,m), random.uniform(-m,m)
    if math.floor(x) % d == 0 or math.floor(y) % d == 0:
        best_x = -x/((x**2+y**2)**0.5)
        best_y = -y/((x**2+y**2)**0.5)
    else:
        best_x = x/((x**2+y**2)**0.5)
        best_y = y/((x**2+y**2)**0.5)
    return random.triangular(-m,m,best_x), random.triangular(-m,m,best_y)

def next_point(current_point):
    return apply(next_dir(current_point), current_point)


start = (0,0)
progression = [start]
for _ in range(N):
    next = next_point(progression[-1])
    progression.append(next)

x = [x for x,_ in progression]
y = [y for _,y in progression]

plt.plot(x,y, ',')
plt.show()