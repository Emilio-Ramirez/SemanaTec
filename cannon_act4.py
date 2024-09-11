from random import randrange
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
        # Aumentado la velocidad inicial del proyectil
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Aumentado la velocidad de los balones
        target.x -= 1

    if inside(ball):
        # Aumentado la gravedad para un movimiento más rápido
        speed.y -= 0.5
        ball.move(speed)
    else:
        # Reposiciona el balón en la ubicación inicial si sale de la pantalla
        ball.x = -199
        ball.y = -199
        speed.x = 0
        speed.y = 0

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            # Reposicionar el target a la derecha cuando salga de la pantalla
            target.x = 200
            target.y = randrange(-150, 150)


    # Reducido el intervalo de tiempo para un movimiento más rápido
    ontimer(move, 25)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
