# aprende-programacion-programando-videojuegos
por [@gabopython](https://www.tiktok.com/@gabopython?lang=en)

Curso de programación en
[youtube](https://youtu.be/3o6nieWbqHU?si=TC7essbpCG_WRSlQ)

<img src="https://github.com/gabopython/IMAGES/blob/main/make_the_best_and_simplest_logo_ever_remeber_sh.jpg" alt="drawing" width="60"/>


  instalar pygame en Windows
```
pip install pygame
```
Mac
```
pip3 install pygame
```


codigo base de pygame

```python
import pygame
from pygame.locals import *


WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants


# variables


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    # code here

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)
```
