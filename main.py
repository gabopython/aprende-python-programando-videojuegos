import pygame
from pygame.locals import *


WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants
TAMANO_CUADRADO = 30
GRAVEDAD = 0.1

# variables
cuadrado = pygame.Rect(300, 0, TAMANO_CUADRADO, TAMANO_CUADRADO)
pisos = [
    pygame.Rect(0, 400, 60, TAMANO_CUADRADO),
    pygame.Rect(60, 140, 60, TAMANO_CUADRADO),
    pygame.Rect(140, 340, 60, TAMANO_CUADRADO),
    pygame.Rect(300, 300, 60, TAMANO_CUADRADO),
]
velocidad_y = float(0)
print(velocidad_y)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    # code here
    keys = pygame.key.get_pressed()
    if keys[K_d]:
        cuadrado.x = cuadrado.x + 1
    elif keys[K_a]:
        cuadrado.x = cuadrado.x - 1

    for piso in pisos:
        pygame.draw.rect(screen, (0, 0, 255), piso)
        if cuadrado.colliderect(piso):
            velocidad_y = 0

    velocidad_y = velocidad_y + GRAVEDAD
    cuadrado.y = cuadrado.y + velocidad_y

    pygame.draw.rect(screen, (255, 0, 0), cuadrado)

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)
