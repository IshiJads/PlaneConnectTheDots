import pgzrun
import random

WIDTH = 750
HEIGHT = 550
max = 10
plane = []
next = 0
lines = []

for i in range(max):
    airplane = Actor("plane")
    airplane.x = random.randint(50, 700)
    airplane.y = random.randint(50, 500)
    plane.append(airplane)

def draw():
    screen.blit("sky", (0, 0))
    num = 1
    for i in plane:
        i.draw()
        screen.draw.text(str(num), (i.x + 20, i.y + 20), color="black")
        num += 1
    for line in lines:
        screen.draw.line(line[0], line[1], color="black")

def on_mouse_down(pos):
    global next, lines

    if next < max:
        if plane[next].collidepoint(pos):  
            if next: 
                lines.append((plane[next - 1].pos, plane[next].pos)) 
            next += 1
            print(lines)

pgzrun.go()