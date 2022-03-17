# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # call the draw methods here
    midpoint_analysis(100, 150, 101, 380)
    midpoint_analysis(101, 380, 221, 381)
    midpoint_analysis(100, 150, 220, 151)
    midpoint_analysis(220, 151, 221, 265)
    midpoint_analysis(100, 266, 220, 265)

    midpoint_analysis(240, 150, 101, 380)
    midpoint_analysis(241, 380, 361, 381)
    midpoint_analysis(240, 150, 360, 151)
    midpoint_analysis(360, 151, 361, 265)
    midpoint_analysis(240, 266, 360, 265)

    glutSwapBuffers()


def calcultion(x_0, y_0, x_1, y_1):
    dx = x_1 - x_0
    dy = y_0 - y_1
    d = 2 * dy - dx
    E = 2 * dy
    NE = 2 * (dy - dx)
    return dx, dy, d, E, NE


def draw(x, y):
    glPointSize(2)
    glColor3d(1, 0, 0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


# put your drawing codes inside this 'draw' function
def midpoint_analysis(x_0, y_0, x_1, y_1):
    dx = x_1 - x_0
    dy = y_1 - y_0
    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            x_0, y_0 = x_0, y_0  # zone 0
            x_1, y_1 = x_1, y_1
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(x, y)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(x, y)


        elif dx < 0 and dy > 0:
            x_0, y_0 = -x_0, y_0  # zone 3
            x_1, y_1 = -x_1, y_1
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(-x, y)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(-x, y)

        elif dx < 0 and dy < 0:
            x_0, y_0 = -x_0, -y_0  # zone 4
            x_1, y_1 = -x_1, -y_1
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(-x, -y)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(-x, -y)

        elif dx > 0 and dy < 0:
            x_0, y_0 = x_0, -y_0  # zone 7
            x_1, y_1 = x_1, -y_1
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(x, -y)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(x, -y)

    if abs(dx) < abs(dy):
        if dx > 0 and dy > 0:
            x_0, y_0 = y_0, x_0  # zone 1
            x_1, y_1 = y_1, x_1
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(y, x)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(y, x)

        elif dx < 0 and dy > 0:
            x_0, y_0 = y_0, -x_0
            x_1, y_1 = y_1, -x_1  # zone 2
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(-y, x)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(-y, x)

        elif dx < 0 and dy < 0:
            x_0, y_0 = -y_0, -x_0  # zone 5
            x_1, y_1 = -y_1, -x_1
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(-y, -x)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(-y, -x)

        elif dx > 0 and dy < 0:
            x_0, y_0 = -y_0, x_0  # zone 6
            x_1, y_1 = -y_1, x_1
            dx, dy, d, E, NE = calcultion(x_0, y_0, x_1, y_1)
            x = x_0
            y = y_0
            draw(y, -x)
            while x < x_1:
                if d <= 0:
                    d = d + E
                    x += 1
                else:
                    d = d + NE
                    x += 1
                    y += 1
                draw(y, -x)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Template")
glutDisplayFunc(showScreen)

init()

glutMainLoop()
