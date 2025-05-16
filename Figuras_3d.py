import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, pi, copysign

# ===================== UTILIDADES =====================
def sign_pow(val, exp):
    return copysign(abs(val) ** exp, val)

def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_size()

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return tex_id

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    light_pos = [1.0, 1.0, 2.0, 0.0]
    light_color = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_color)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1, 1, 1, 1])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])
    glMaterialf(GL_FRONT, GL_SHININESS, 50)

def update_projection(perspective=True):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if perspective:
        gluPerspective(45, 800 / 600, 0.1, 50.0)
    else:
        glOrtho(-2, 2, -2, 2, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def draw_menu():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Usar una proyección ortográfica para el menú
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Dibujar un cuadrado que cubra toda la pantalla
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 0.0)
    
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glEnd()
    
    # Restaurar la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


# ===================== FIGURA =====================
def draw_cubo():
    glColor3f(1, 1, 1)
    
    # Definir los vértices del cubo
    vertices = [
        # Cara frontal
        (-0.5, -0.5, 0.5),  # Abajo-izquierda
        (0.5, -0.5, 0.5),   # Abajo-derecha
        (0.5, 0.5, 0.5),    # Arriba-derecha
        (-0.5, 0.5, 0.5),   # Arriba-izquierda
        
        # Cara trasera
        (-0.5, -0.5, -0.5),
        (0.5, -0.5, -0.5),
        (0.5, 0.5, -0.5),
        (-0.5, 0.5, -0.5)
    ]
    
    # Definir las caras del cubo (cada cara es un cuadrilátero)
    faces = [
        (0, 1, 2, 3),  # Cara frontal
        (1, 5, 6, 2),  # Cara derecha
        (5, 4, 7, 6),  # Cara trasera
        (4, 0, 3, 7),  # Cara izquierda
        (3, 2, 6, 7),  # Cara superior
        (0, 4, 5, 1)   # Cara inferior
    ]
    
    # Coordenadas de textura
    texcoords = [
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (0.0, 1.0)
    ]
    
    # Normales para cada cara (perpendicular a la cara)
    normals = [
        (0, 0, 1),    # Frontal
        (1, 0, 0),    # Derecha
        (0, 0, -1),   # Trasera
        (-1, 0, 0),   # Izquierda
        (0, 1, 0),    # Superior
        (0, -1, 0)    # Inferior
    ]
    
    # Dibujar cada cara
    for i, face in enumerate(faces):
        glBegin(GL_QUADS)
        
        # Establecer la normal para toda la cara
        glNormal3fv(normals[i])
        
        # Dibujar los 4 vértices de la cara
        for j, vertex_index in enumerate(face):
            glTexCoord2fv(texcoords[j])
            glVertex3fv(vertices[vertex_index])
            
        glEnd()

def draw_piramide():
    glColor3f(1, 1, 1)
    
    # Definir los vértices de la pirámide de base cuadrada
    # Vértice superior
    apex = (0, 0.8, 0)
    
    # Base cuadrada (en plano y = -0.5)
    base = [
        (-0.5, -0.5, 0.5),   # Frente-izquierda
        (0.5, -0.5, 0.5),    # Frente-derecha
        (0.5, -0.5, -0.5),   # Atrás-derecha
        (-0.5, -0.5, -0.5)   # Atrás-izquierda
    ]
    
    # Dibujar la base (cuadrado)
    glBegin(GL_QUADS)
    glNormal3f(0, -1, 0)  # Normal apuntando hacia abajo
    
    glTexCoord2f(0, 0)
    glVertex3fv(base[0])
    
    glTexCoord2f(1, 0)
    glVertex3fv(base[1])
    
    glTexCoord2f(1, 1)
    glVertex3fv(base[2])
    
    glTexCoord2f(0, 1)
    glVertex3fv(base[3])
    glEnd()
    
    # Dibujar las 4 caras triangulares
    faces = [
        (0, 1),  # Cara frontal
        (1, 2),  # Cara derecha
        (2, 3),  # Cara trasera
        (3, 0)   # Cara izquierda
    ]
    
    # Normales aproximadas para cada cara triangular
    normals = [
        (0, 0.5, 1),    # Frontal
        (1, 0.5, 0),    # Derecha
        (0, 0.5, -1),   # Trasera
        (-1, 0.5, 0)    # Izquierda
    ]
    
    # Dibujar cada cara triangular
    for i, (v1, v2) in enumerate(faces):
        glBegin(GL_TRIANGLES)
        
        # Establecer normal para toda la cara
        nx, ny, nz = normals[i]
        glNormal3f(nx, ny, nz)
        
        # El triángulo: dos puntos de la base y el vértice superior
        glTexCoord2f(0.5, 1.0)  # Vértice superior de la textura
        glVertex3fv(apex)
        
        glTexCoord2f(0.0, 0.0)  # Esquina inferior izquierda de la textura
        glVertex3fv(base[v1])
        
        glTexCoord2f(1.0, 0.0)  # Esquina inferior derecha de la textura
        glVertex3fv(base[v2])
        
        glEnd()

def draw_superellipsoid(a=1, b=1, c=0.5, n1=0.5, n2=0.5, resolution=40):
    glColor3f(1,1,1)
    du = pi / resolution
    dv = 2 * pi / resolution

    if glIsEnabled(GL_TEXTURE_2D):
        glEnable(GL_TEXTURE_2D)

    for i in range(resolution):
        u = -pi/2 + i * du
        un = -pi/2 + (i + 1) * du

        glBegin(GL_TRIANGLE_STRIP)
        for j in range(resolution + 1):
            v = -pi + j * dv

            def get_point(u, v):
                x = a * sign_pow(cos(u), n1) * sign_pow(cos(v), n2)
                y = b * sign_pow(cos(u), n1) * sign_pow(sin(v), n2)
                z = c * sign_pow(sin(u), n1)
                return x, y, z

            x1, y1, z1 = get_point(u, v)
            x2, y2, z2 = get_point(un, v)

            tx = j / resolution
            ty1 = i / resolution
            ty2 = (i + 1) / resolution

            glNormal3f(x1, y1, z1)
            glTexCoord2f(tx, ty1)
            glVertex3f(x1, y1, z1)

            glNormal3f(x2, y2, z2)
            glTexCoord2f(tx, ty2)
            glVertex3f(x2, y2, z2)
        glEnd()

def draw_esfera():

    glColor3f(1,1,1)
    quadric = gluNewQuadric()#Genera un objeto de tipo Quadric para facilitar creacion de figuras
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, 1, 36, 36)
    gluDeleteQuadric(quadric)#Libera memoria de quadric

def draw_cilindro():

    glColor3f(1,1,1)
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluCylinder(quadric, 0.5, 0.5, 1.5, 36, 16) #quadric,Radio de base, radio del tope, altura,particiones sobre el centro,cortes horizontales
    gluDisk(quadric, 0, 0.5, 36, 1)#radio interior,radio exterior,particiones sobre el centro,loops
    glPushMatrix()
    glTranslatef(0, 0, 1.5)#Mueve uno de los discos al otro extremo
    gluDisk(quadric, 0, 0.5, 36, 1)
    glPopMatrix()
    gluDeleteQuadric(quadric)

# ===================== MAIN =====================
def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800 / 600, 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)

    is_perspective = True
    update_projection(is_perspective)

    texture_id = load_texture("textura.jpg")
    menu_texture_id = load_texture("menu.jpg")
    glBindTexture(GL_TEXTURE_2D, texture_id)

    setup_lighting()
    lighting_enabled = True
    texture_enabled = True
    menu=True
    rot_x = rot_y = 0
    move_x = move_z = 0
    scale = 1.0
    figura=0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or figura==6:
                pygame.quit()
                return

            if event.type == KEYDOWN:
                if event.key == K_r:
                    rot_x = rot_y = move_x = move_z = 0
                    scale = 1.0
                elif event.key == K_t:
                    texture_enabled = not texture_enabled
                elif event.key == K_i:
                    lighting_enabled = not lighting_enabled
                    if lighting_enabled:
                        glEnable(GL_LIGHTING)
                    else:
                        glDisable(GL_LIGHTING)
                elif event.key == K_p:
                    is_perspective = not is_perspective
                    update_projection(is_perspective)
                elif event.key == K_ESCAPE:
                    menu=True

        if(menu==True):
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, menu_texture_id)
            draw_menu()
            glDisable(GL_TEXTURE_2D)
            keys = pygame.key.get_pressed()
            if keys[K_1]:figura=1;menu=False
            if keys[K_2]:figura=2;menu=False
            if keys[K_3]:figura=3;menu=False
            if keys[K_4]:figura=4;menu=False
            if keys[K_5]:figura=5;menu=False
            if keys[K_6]:figura=6
        else:

            keys = pygame.key.get_pressed()
            if keys[K_LEFT]: rot_y -= 1
            if keys[K_RIGHT]: rot_y += 1
            if keys[K_UP]: rot_x -= 1
            if keys[K_DOWN]: rot_x += 1
            if keys[K_w]: move_z += 0.1
            if keys[K_s]: move_z -= 0.1
            if keys[K_a]: move_x -= 0.1
            if keys[K_d]: move_x += 0.1
            if keys[K_PLUS] or keys[K_KP_PLUS]: scale += 0.05
            if keys[K_MINUS] or keys[K_KP_MINUS]: scale = max(0.1, scale - 0.05)
            if keys[K_ESCAPE]:menu=True

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslatef(move_x, 0.0, -5 + move_z)
            glScalef(scale, scale, scale)
            glRotatef(rot_x, 1, 0, 0)
            glRotatef(rot_y, 0, 1, 0)

            if texture_enabled:
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, texture_id)
            else:
                glDisable(GL_TEXTURE_2D)
            
            
            if figura==1:draw_cubo()
            if figura==2:draw_piramide()
            if figura==3:draw_esfera()
            if figura==4:draw_cilindro()
            if figura==5:draw_superellipsoid()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
