import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Setup layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Objek Bergerak dengan Pygame")
clock = pygame.time.Clock()

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Objek (bola)
ball_pos = [WIDTH // 2, HEIGHT // 2] #Posisi awal tengah
ball_radius = 20
ball_speed_x = 5 # Kecepatan horizointal
ball_speed_y = 0 # Vertikal (bisa diubah)

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update posisi bola
    ball_pos[0] += ball_speed_x
    ball_pos[1] += ball_speed_y

    # Cek batas dan pantul
    if ball_pos[0] + ball_radius > WIDTH or ball_pos[0] - ball_radius < 0:
        ball_speed_x = -ball_speed_x
    if ball_pos[1] + ball_radius > HEIGHT or ball_pos[1] - ball_radius < 0:
        ball_speed_y = -ball_speed_y # Jika tambah gerak vertikal

    # Gambar layar
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, ball_pos, ball_radius)
    pygame.display.flip()

    # Kontrol FPS (60 frame per detik)
    clock.tick(60)
# Tutup
pygame.quit()
sys.exit()