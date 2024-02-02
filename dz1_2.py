import turtle

window = turtle.Screen()

# Створення Turtle
t = turtle.Turtle()
t.speed(0)

# Функція для малювання складної фігури
def draw_complex_shape():
    for i in range(36):
        draw_square(t)
        t.right(20)

# Функція для малювання квадрата
def draw_square(t):
    for j in range(4):
        t.forward(100)
        t.right(90)

draw_complex_shape()