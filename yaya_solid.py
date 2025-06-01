from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0, 0, 0, 1) # Latar belakang hitam
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Menyesuaikan viewport agar ada ruang untuk 4 huruf berjejer
    gluOrtho2D(-1.5, 1.5, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW) # Pindah ke modelview matrix untuk transformasi

def draw_letter_Y(center_x, center_y, scale=1.0):
    """Menggambar huruf 'Y' di sekitar center_x, center_y dengan skala tertentu."""
    # Batang kiri atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.0 * scale), 0)
    glEnd()

    # Batang kanan atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.0 * scale), 0)
    glEnd()

    # Batang bawah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

def draw_letter_A(center_x, center_y, scale=1.0):
    """Menggambar huruf 'A' di sekitar center_x, center_y dengan skala tertentu."""
    # Kaki kiri
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.05 * scale), center_y + (0.3 * scale), 0)
    glEnd()

    # Kaki kanan
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.2 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.3 * scale), 0)
    glEnd()

    # Palang tengah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.05 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.05 * scale), 0)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255, 192, 203) # <--- DI SINI WARNA DIUBAH MENJADI PINK
    
    # Gambar huruf YAY A
    base_y = 0 # Posisi vertikal tengah huruf

    # Huruf Y pertama
    draw_letter_Y(-1.0, base_y, 0.7)

    # Huruf A pertama
    draw_letter_A(-0.5, base_y, 0.7)

    # Huruf Y kedua
    draw_letter_Y(0.0, base_y, 0.7)

    # Huruf A kedua
    draw_letter_A(0.5, base_y, 0.7)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(900, 400) # Ukuran window
glutCreateWindow(b"Huruf YAYA") # Judul window
init()
glutDisplayFunc(draw)
glutMainLoop()