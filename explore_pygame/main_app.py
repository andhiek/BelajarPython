# Explore Pygame

import pygame


# Lnagkah membuat game

# 1. init
pygame.init()
# Variabel Running Game
isRun = True

# Membuat surface Object / Display
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang))

# Object Game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan Gerak
speed = 2

while isRun:
    # pygame.display.update()
    pygame.time.delay(10)
    # 2 . User Inpur / Databases Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # Ambil keybiard press
    keys = pygame.key.get_pressed()
    # ambil arah ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    # 3 . Update asset game
    window.fill("black")
    pygame.draw.rect(window, (255, 0, 0), (x, y, lebar, panjang))
    # game dynamic

    # 4 . Render ke Game
    pygame.display.update()

pygame.quit()
