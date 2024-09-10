from turtle import *
from random import randrange, choice
from freegames import square, vector

# Definir colores permitidos (excepto rojo)
colors = ['blue', 'yellow', 'green', 'purple', 'orange']

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Asignar colores aleatorios a la comida y la víbora
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Mover la comida aleatoriamente
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    new_food = food + choice(directions)
    if inside(new_food):
        food.x = new_food.x
        food.y = new_food.y

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
