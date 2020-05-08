import numpy as np
# import pygame
# from math import pi
# pygame.init()

# screen = pygame.display.set_mode((100, 100))
# WHITE = pygame.Color(255, 255, 255)
# RED = pygame.Color(255, 0, 0)

# size = (50, 50)
# # The corner points of the polygon.
# points = [(25, 0), (50, 25), (25, 50), (0, 25)]

# polygon = pygame.Surface(size)
# pygame.draw.polygon(polygon, RED, points, 10)

# polygon_filled = pygame.Surface(size)
# pygame.draw.polygon(polygon_filled, RED, points)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit()

#     screen.blit(polygon_filled, (25, 25))
#     pygame.display.update()

distTot = 2
pos = 310
lenght = 27
arrResult = []
for longitud in range(0, 2*distTot+1):
    arr = []
    for y in range(pos - (lenght*(distTot-longitud))-distTot, pos - (lenght*(distTot-longitud)) +
                   distTot+1):
        arr.append(y)
    arrResult.append(arr)

print(arrResult)
print(np.array(arrResult))
