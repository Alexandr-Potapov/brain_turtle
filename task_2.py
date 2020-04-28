import turtle


brain = turtle.Turtle()


def draw_branch(length, loops_count, branch_shift):
    # всего 4 ветви, для каждой нужен сдвиг относительно предыдущей
    brain.left(90 * (branch_shift - 1))

    cells_count = (loops_count + 1) * 2
    cell_length = length / cells_count

    for loop_number in range(0, loops_count + 1):
        # max с единицей - чтобы длина первой линии была != 0
        line_length = max(loop_number * 2, 1) * cell_length
        brain.fd(line_length)
        brain.left(90)

    brain.up()
    brain.home()
    brain.down()


def draw(length, loops_count):
    brain.up()
    brain.goto(-length / 2, -length / 2)
    brain.down()

    for _ in range(4):
        brain.fd(length)
        brain.left(90)

    brain.up()
    brain.home()
    brain.down()

    for branch_number in range(4):
        draw_branch(length, loops_count, branch_number)


draw(220, 5)
input()




