from random import randrange
from random import choice # Se agrega esta librería
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    # Lista de formas posibles
    shapes = ['circle', 'square', 'triangle']

    for target in targets:
        goto(target.x, target.y)
        shape = choice(shapes)  # Seleccionar una forma aleatoria

        # Dibujar una forma dependiendo de la selección aleatoria
        if shape == 'circle':
            dot(20, 'blue')
        elif shape == 'square':
            begin_fill()
            for _ in range(4):
                forward(20)
                left(90)
            end_fill()
        elif shape == 'triangle':
            begin_fill()
            for _ in range(3):
                forward(20)
                left(120)
            end_fill()

    if inside(ball):
        goto(ball.x, ball.y - 3)  # Ajuste leve para centrar mejor la pelota
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()