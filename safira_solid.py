from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0, 0, 0, 1) # Latar belakang hitam
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Menyesuaikan viewport agar ada ruang untuk nama "FIRAH"
    gluOrtho2D(-1.5, 1.5, -1.0, 1.0) # Sesuaikan rentang X agar FIRAH pas
    glMatrixMode(GL_MODELVIEW) # Pindah ke modelview matrix untuk transformasi

# --- Fungsi Menggambar Huruf ---

def draw_letter_S(center_x, center_y, scale=1.0):
    """Menggambar huruf 'S' kapital yang benar (disimpan untuk referensi)."""
    thickness = 0.05 * scale # Ketebalan garis huruf

    # 1. Bagian horizontal atas (Puncak 'S')
    glBegin(GL_QUADS)
    glVertex3f(center_x - 0.2 * scale,      center_y + 0.3 * scale, 0)
    glVertex3f(center_x + 0.2 * scale,      center_y + 0.3 * scale, 0)
    glVertex3f(center_x + 0.2 * scale,      center_y + 0.3 * scale - thickness, 0)
    glVertex3f(center_x - 0.2 * scale,      center_y + 0.3 * scale - thickness, 0)
    glEnd()

    # 2. Bagian vertikal kanan atas (Kurva pertama S)
    glBegin(GL_QUADS)
    glVertex3f(center_x + 0.2 * scale - thickness, center_y + 0.3 * scale - thickness, 0)
    glVertex3f(center_x + 0.2 * scale,             center_y + 0.3 * scale - thickness, 0)
    glVertex3f(center_x + 0.2 * scale,             center_y + 0.0 * scale + thickness / 2, 0)
    glVertex3f(center_x + 0.2 * scale - thickness, center_y + 0.0 * scale + thickness / 2, 0)
    glEnd()

    # 3. Bagian horizontal tengah (Perut 'S')
    glBegin(GL_QUADS)
    glVertex3f(center_x - 0.2 * scale,             center_y + 0.0 * scale + thickness / 2, 0)
    glVertex3f(center_x + 0.2 * scale,             center_y + 0.0 * scale + thickness / 2, 0)
    glVertex3f(center_x + 0.2 * scale,             center_y + 0.0 * scale - thickness / 2, 0)
    glVertex3f(center_x - 0.2 * scale,             center_y + 0.0 * scale - thickness / 2, 0)
    glEnd()

    # 4. Bagian vertikal kiri bawah (Kurva kedua S)
    glBegin(GL_QUADS)
    glVertex3f(center_x - 0.2 * scale,             center_y + 0.0 * scale - thickness / 2, 0)
    glVertex3f(center_x - 0.2 * scale + thickness, center_y + 0.0 * scale - thickness / 2, 0)
    glVertex3f(center_x - 0.2 * scale + thickness, center_y - 0.3 * scale, 0)
    glVertex3f(center_x - 0.2 * scale,             center_y - 0.3 * scale, 0)
    glEnd()

    # 5. Bagian horizontal bawah (Dasar 'S')
    glBegin(GL_QUADS)
    glVertex3f(center_x - 0.2 * scale,      center_y - 0.3 * scale, 0)
    glVertex3f(center_x + 0.2 * scale,      center_y - 0.3 * scale, 0)
    glVertex3f(center_x + 0.2 * scale,      center_y - 0.3 * scale + thickness, 0)
    glVertex3f(center_x - 0.2 * scale,      center_y - 0.3 * scale + thickness, 0)
    glEnd()


def draw_letter_A(center_x, center_y, scale=1.0):
    """Menggambar huruf 'A' di sekitar center_x, center_y."""
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

def draw_letter_F(center_x, center_y, scale=1.0):
    """Menggambar huruf 'F' di sekitar center_x, center_y."""
    # Batang vertikal
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.2 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

    # Batang horizontal atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.25 * scale), 0)
    glEnd()

    # Batang horizontal tengah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.05 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.05 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.0 * scale), 0)
    glEnd()

def draw_letter_I(center_x, center_y, scale=1.0):
    """Menggambar huruf 'I' di sekitar center_x, center_y."""
    # Batang vertikal
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.025 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.025 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.025 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.025 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

    # Batang horizontal atas (opsional, untuk tampilan lebih kotak)
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (0.25 * scale), 0)
    glEnd()

    # Batang horizontal bawah (opsional)
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.25 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (-0.25 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.1 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

def draw_letter_R(center_x, center_y, scale=1.0):
    """Menggambar huruf 'R' di sekitar center_x, center_y."""
    # Batang vertikal
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (-0.2 * scale), center_y + (-0.3 * scale), 0)
    glEnd()

    # Batang horizontal atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.3 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (-0.2 * scale), center_y + (0.25 * scale), 0)
    glEnd()

    # Batang horizontal tengah (bagian lengkungan P)
    glBegin(GL_QUADS)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.05 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.05 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (-0.15 * scale), center_y + (0.0 * scale), 0)
    glEnd()

    # Bagian lengkungan kanan atas
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.25 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glEnd()

    # Garis diagonal ke bawah
    glBegin(GL_QUADS)
    glVertex3f(center_x + (0.0 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.05 * scale), center_y + (0.0 * scale), 0)
    glVertex3f(center_x + (0.15 * scale), center_y + (-0.3 * scale), 0)
    glVertex3f(center_x + (0.1 * scale), center_y + (-0.3 * scale), 0)
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255, 192, 203) # Warna PINK

    # Posisi vertikal tengah semua huruf
    base_y = 0
    # Skala huruf
    letter_scale = 0.6

    # Posisi awal huruf pertama 'F' untuk FIRAH
    start_x = -0.7 # Sesuaikan posisi awal agar FIRAH berada di tengah

    # Gambar huruf F
    draw_letter_F(start_x, base_y, letter_scale)

    # Gambar huruf I
    draw_letter_I(start_x + 0.4, base_y, letter_scale) # Geser I sedikit karena ramping

    # Gambar huruf R
    draw_letter_R(start_x + 0.85, base_y, letter_scale) # Geser R agar ada spasi yang baik

    # Gambar huruf A
    draw_letter_A(start_x + 1.35, base_y, letter_scale) # Geser A lagi

    # Gambar huruf H
    # Karena kita belum punya fungsi draw_letter_H, mari kita buat yang sederhana dulu.
    # Batang vertikal kiri
    glBegin(GL_QUADS)
    glVertex3f(start_x + 1.85 - 0.2 * letter_scale, base_y + 0.3 * letter_scale, 0)
    glVertex3f(start_x + 1.85 - 0.15 * letter_scale, base_y + 0.3 * letter_scale, 0)
    glVertex3f(start_x + 1.85 - 0.15 * letter_scale, base_y - 0.3 * letter_scale, 0)
    glVertex3f(start_x + 1.85 - 0.2 * letter_scale, base_y - 0.3 * letter_scale, 0)
    glEnd()
    # Batang vertikal kanan
    glBegin(GL_QUADS)
    glVertex3f(start_x + 1.85 + 0.15 * letter_scale, base_y + 0.3 * letter_scale, 0)
    glVertex3f(start_x + 1.85 + 0.2 * letter_scale, base_y + 0.3 * letter_scale, 0)
    glVertex3f(start_x + 1.85 + 0.2 * letter_scale, base_y - 0.3 * letter_scale, 0)
    glVertex3f(start_x + 1.85 + 0.15 * letter_scale, base_y - 0.3 * letter_scale, 0)
    glEnd()
    # Batang horizontal tengah
    glBegin(GL_QUADS)
    glVertex3f(start_x + 1.85 - 0.15 * letter_scale, base_y + 0.05 * letter_scale, 0)
    glVertex3f(start_x + 1.85 + 0.15 * letter_scale, base_y + 0.05 * letter_scale, 0)
    glVertex3f(start_x + 1.85 + 0.15 * letter_scale, base_y - 0.0 * letter_scale, 0)
    glVertex3f(start_x + 1.85 - 0.15 * letter_scale, base_y - 0.0 * letter_scale, 0)
    glEnd()


    glFlush() # Memastikan semua perintah gambar dieksekusi

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 400) # Ukuran window disesuaikan untuk FIRAH
glutCreateWindow(b"Nama FIRAH") # Judul window

init()
glutDisplayFunc(draw)
glutMainLoop()