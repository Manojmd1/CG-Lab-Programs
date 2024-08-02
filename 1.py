import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
 
def LineBres(X1, Y1, X2, Y2): 
    glClear(GL_COLOR_BUFFER_BIT) 
    dx, dy = abs(X2 - X1), abs(Y2 - Y1) 
    p, twoDy, twoDyDx = 2 * dy - dx, 2 * dy, 2 * (dy - dx) 
    x, y = (X2, Y2) if X1 > X2 else (X1, Y1) 
    X2 = max(X1, X2) 
     
    glBegin(GL_POINTS) 
    glVertex2i(x, y) 
    while x < X2: 
        x, p = x + 1, p + (twoDy if p < 0 else twoDyDx) 
        if p >= 0: y += 1     
        glVertex2i(x, y) 
    glEnd() 
    glFlush() 
 
def Init(): 
    glClearColor(1.0, 1.0, 1.0, 0) 
    glColor3f(0.0, 0.0, 0.0) 
    glPointSize(4.0) 
    glViewport(0, 0, 300, 400) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluOrtho2D(0, 300, 0, 400) 
 
def main(): 
    pygame.init() 
    pygame.display.set_mode((700, 700), DOUBLEBUF | OPENGL) 
    Init() 
 
    X1, Y1 = map(int, input("Enter X1, Y1: ").split()) 
    X2, Y2 = map(int, input("Enter X2, Y2: ").split()) 
 
    running = True 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
         
        LineBres(X1, Y1, X2, Y2) 
        pygame.display.flip() 
        pygame.time.wait(100) 
pygame.quit() 
if __name__ == "__main__": main() 
