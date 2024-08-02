import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
 
# Initial transformation values 
tx, ty, tz = 0, 0, -5  # Translation 
angle_x, angle_y, angle_z = 0, 0, 0  # Rotation angles 
scale = 1  # Scale factor 
 
def init(): 
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    glEnable(GL_DEPTH_TEST) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluPerspective(45, 1.0, 0.1, 50.0) 
    glMatrixMode(GL_MODELVIEW) 
 
def draw_cube(): 
    vertices = [ 
        [-1, -1, -1], 
        [1, -1, -1], 
        [1, 1, -1], 
        [-1, 1, -1], 
        [-1, -1, 1], 
        [1, -1, 1], 
        [1, 1, 1], 
        [-1, 1, 1] 
    ] 
 
    edges = [ 
        [0, 1], 
        [1, 2], 
        [2, 3], 
        [3, 0], 
        [4, 5], 
        [5, 6], 
        [6, 7], 
        [7, 4], 
        [0, 4], 
        [1, 5], 
        [2, 6], 
        [3, 7] 
    ] 
 
    glBegin(GL_LINES) 
    for edge in edges: 
        for vertex in edge: 
            glVertex3fv(vertices[vertex]) 
    glEnd() 
 
def display(): 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
     
    glLoadIdentity() 
    glTranslatef(tx, ty, tz) 
    glRotatef(angle_x, 1, 0, 0) 
    glRotatef(angle_y, 0, 1, 0) 
    glRotatef(angle_z, 0, 0, 1) 
    glScalef(scale, scale, scale) 
     
    draw_cube() 
     
    pygame.display.flip() 
 
def main(): 
    global tx, ty, tz, angle_x, angle_y, angle_z, scale 
     
    pygame.init() 
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL) 
    pygame.display.set_caption("3D Transformations") 
    init() 
     
    running = True 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            elif event.type == KEYDOWN: 
                if event.key == K_w:  # Move up 
                    ty += 0.1 
                elif event.key == K_s:  # Move down 
                    ty -= 0.1 
                elif event.key == K_a:  # Move left 
                    tx -= 0.1 
                elif event.key == K_d:  # Move right 
                    tx += 0.1 
                elif event.key == K_q:  # Move forward 
                    tz += 0.1 
                elif event.key == K_e:  # Move backward 
                    tz -= 0.1 
                elif event.key == K_i:  # Rotate up 
                    angle_x += 5 
                elif event.key == K_k:  # Rotate down 
                    angle_x -= 5 
                elif event.key == K_j:  # Rotate left 
                    angle_y -= 5 
                elif event.key == K_l:  # Rotate right 
                    angle_y += 5 
                elif event.key == K_u:  # Rotate clockwise 
                    angle_z += 5 
                elif event.key == K_o:  # Rotate counterclockwise 
                    angle_z -= 5 
                elif event.key == K_EQUALS:  # Scale up 
                    scale += 0.1 
                elif event.key == K_MINUS:  # Scale down 
                    scale -= 0.1 
         
        display() 
     
    pygame.quit() 
 
if __name__ == "__main__": 
    main() 
