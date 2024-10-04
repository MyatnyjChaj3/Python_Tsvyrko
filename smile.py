# Задание

"""
Нужно нарисовать смайлик. Выбор смайлика по номеру из списка группы. 10. Файл прикреплён к заданию.

Условия:
Изображение формируется несколькими источниками (первые два обязательны):
- генератор позиций, который рассчитывать точки на основе криволинейной функции.
- готовый список позиций
- другие источники, которые помогут нарисовать.

Нельзя использовать готовые примитивы из движка.
Если используется парабола из шаблона, то следует добавить ещё одну криволинейную функцию.

Изображение должно быть в центре холста и по высоте/ширине быть больше половин размеров холста.
Не обязательно повторять чётко смайлик - нужно передать эмоцию. "Я художник - я так вижу" ))

Можно (иногда нужно) к смайлику добавить атрибут, например, бабочку или волосики. Чтобы соблюсти условия задания.
"""

import math
import turtle
from collections import namedtuple

# Константы
STEP = 2
Point = namedtuple('Point', ['x', 'y'])

def angle_two_point(p1, p2):
    dy = p2.y - p1.y
    dx = p2.x - p1.x
    if dx == 0:
        return 180.
    return math.atan2(dy, dx) * 180. / math.pi

def draw_parabola(x0, x1, a=1, b=0, c=0):
    angle = 0
    p_old = Point(x0, 0)
    p_new = p_old
    for x in range(x0, x1 + 1):
        p_new = Point(x, a * x ** 2 + b * x + c)
        yield (angle, p_new)
        angle = angle_two_point(p_old, p_new)
        p_old = p_new

def draw_circle(radius, x_offset=0, y_offset=0):
    angle = 0
    p_old = Point(radius + x_offset, y_offset)  # Начальная точка
    for deg in range(0, 361, STEP):
        x = radius * math.cos(math.radians(deg)) + x_offset
        y = radius * math.sin(math.radians(deg)) + y_offset
        
        p_new = Point(x, y)
        yield (angle, p_new)
        angle = angle_two_point(p_old, p_new)
        p_old = p_new

def draw_teardrop(x, y):

    bob.penup()
    bob.goto(x, y)
    bob.pendown()
    bob.setheading(240)
    bob.forward(31.5)

    bob.penup()
    bob.goto(x, y)
    bob.pendown()
    bob.setheading(300)
    bob.forward(31)
    
    # Рисуем нижнюю часть капли (параболу)
    teardrop_bottom_parabola = dict(x0=-15, x1=15, a=0.05, b=0, c=-20)  # Параметры параболы
    bob.penup()
    for i, (angle, position) in enumerate(draw_parabola(**teardrop_bottom_parabola)):
        bob.setheading(angle)
        if i == 0:
            bob.setpos(position.x + x, position.y + y - 20)  # Смещение вниз
            bob.pendown()
        bob.setpos(position.x + x, position.y + y - 20)

# Настройки черепахи
bob = turtle.Turtle()
bob.screen.setup(400, 300)
bob.screen.bgcolor("lightblue")
bob.screen.bgpic("rain.png")
bob.screen.delay(20)

bob.shape("turtle")
bob.pencolor("orange")
bob.fillcolor("orange")
bob.pensize(3)

# Контур лица
bob.penup()
for i, (angle, position) in enumerate(draw_circle(100, 0, 0)):
    if i == 0:
        bob.setpos(position.x, position.y)
        bob.pendown()
    bob.setpos(position.x, position.y)
    bob.setheading(angle)

bob.penup()
bob.goto(-40, 50)
bob.pendown()
bob.setheading(0)
bob.forward(20)

bob.penup()
bob.goto(40, 50)
bob.pendown()
bob.setheading(0)
bob.forward(20)

sad_smile_parabola = dict(x0=-50, x1=50, a=-0.01, b=0, c=-30)
bob.penup()
for i, (angle, position) in enumerate(draw_parabola(**sad_smile_parabola)):
    bob.setheading(angle)
    if i == 0:
        bob.setpos(position.x, position.y)
        bob.pendown()
    bob.setpos(position.x, position.y)


draw_teardrop(-30, 40) 

bob.hideturtle()
bob.screen.mainloop()
