import turtle


brain = turtle.Turtle()


def draw():
    brain.left(90)
    brain.fd(400)
    line_length = 300

    for _ in range(20):
        brain.right(105)
        brain.fd(line_length)
        line_length *= 0.8


draw()
input()
