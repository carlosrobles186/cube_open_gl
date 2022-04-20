import pygame
import sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import sin,cos

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (0,0,0),
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    (0,8),
    (1,8),
    (2,8),
    (3,8),
    (4,8),
    (5,8),
    (6,8),
    (7,8),

    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def drawText(x, y, text):
    font = pygame.font.SysFont('arial', 32)
    textSurface = font.render(text, True, (255, 255, 66, 255), (0, 66, 0, 255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


def main():
    zoom = -5
    zoomed = False
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)



    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glPushMatrix()
    glTranslatef(0.0,0.0, zoom)





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glPopMatrix()
                    zoom+=1
                    glTranslatef(0.0,0.0, zoom)
                    glPushMatrix()
                    print("zooming out")
                    zoomed = True
                if event.key == pygame.K_DOWN:
                    if zoomed != True:
                        glPushMatrix()

                    zoom-=1
                    glTranslatef(0.0,0.0, zoom)
                    glPushMatrix()
                    print("zooming in")
                    zoomed = False
        glRotatef(1, 1, 1, 4)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)



        Cube()
        drawText(140, 120, str(sys.argv[1]))
        pygame.display.flip()
        pygame.time.wait(10)


main()