import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
 
# Initial transformation values 
tx, ty = 0, 0  # Translation 
angle = 0      # Rotation angle 
scale = 1      # Scale factor 
 
def init(): 
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0) 
    glMatrixMode(GL_MODELVIEW) 
 
def draw_square(): 
    glBegin(GL_QUADS) 
    glColor3f(1.0, 0.0, 0.0) 
    glVertex2f(-1.0, -1.0) 
    glVertex2f(1.0, -1.0) 
    glVertex2f(1.0, 1.0) 
    glVertex2f(-1.0, 1.0) 
    glEnd() 
 
def display(): 
    glClear(GL_COLOR_BUFFER_BIT) 
     
    glLoadIdentity() 
    glTranslatef(tx, ty, 0) 
    glRotatef(angle, 0, 0, 1) 
    glScalef(scale, scale, 1) 
     
    draw_square() 
     
    pygame.display.flip() 
 
def main(): 
    global tx, ty, angle, scale 
     
    pygame.init() 
    screen = pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL) 
    pygame.display.set_caption("2D Geometric Operations") 
    init() 
     
    running = True 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            elif event.type == KEYDOWN: 
                if event.key == K_w:       # Move up 
                    ty += 2 
                elif event.key == K_s:     # Move down 
                    ty -= 1 
                elif event.key == K_a:     # Move left 
                    tx -= 1 
                elif event.key == K_d:     # Move right 
                    tx += 1 
                elif event.key == K_r:     # Rotate clockwise 
                    angle -= 45 
                elif event.key == K_e:     # Rotate counterclockwise 
                    angle += 45 
                elif event.key == K_EQUALS:  # Scale up 
                    scale += 0.1 
                elif event.key == K_MINUS:   # Scale down 
                    scale -= 0.1 
         
        display() 
     
    pygame.quit() 
 
if __name__ == "__main__": main() 
