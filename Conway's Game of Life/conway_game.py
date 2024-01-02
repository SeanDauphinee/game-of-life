import pygame
import numpy as np 
from grid_operations import *

pygame.init()

#CONSTANTS
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
BLACK = 0, 0, 0
WHITE = 255, 255, 255

# #PYTHON SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
rows, cols = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
grid = np.zeros((rows, cols), dtype=int)

#GAME LOOP
running = True
paused = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            paused = not paused
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            grid = update_grid_mouse(grid, mouse_pos[0], mouse_pos[1])
            
    
    if not paused:
        grid = update_grid(grid)

    screen.fill((BLACK))
    draw_grid(grid)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()