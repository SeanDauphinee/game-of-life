import pygame
import numpy as np

pygame.init()
#CONSTANTS
BLACK = 0, 0, 0 #setting RGB values for the screen
WHITE = 255, 255, 255
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10 #setting number of pixels allocated for each screen

#SCREEN SET UP
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
rows, cols = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
grid = np.zeros((rows, cols), dtype=int)

def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_x, new_y = x + i, y + j
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x, new_y] == 1:
                count += 1
    return count

def update_grid(grid):
    new_grid = np.copy(grid)

    for i in range(rows):
        for j in range(cols):
            neighbours = count_neighbors(grid, i , j)

            #CONWAY'S RULES
            if grid[i, j] == 1:
                if neighbours < 2 or neighbours > 3:
                    new_grid[i, j] = 0  #CELL DIES
                else:
                    if neighbours == 3:
                        new_grid[i, j] = 1  #CELL LIVES
            else:
                if neighbours == 3:
                    new_grid[i,j] = 1 #CELL LIVES
    return new_grid

def update_grid_mouse(grid, mouse_x , mouse_y):
    #THIS UPDATES GRID WHEN MOUSE POSISTION IS PASSED
    new_grid = np.copy(grid)

    cell_i = mouse_y // CELL_SIZE
    cell_j = mouse_x // CELL_SIZE

    new_grid[cell_i, cell_j] = 1 - new_grid[cell_i, cell_j]

    return new_grid


def draw_grid(grid):
    for i in range(rows):
        for j in range(cols):
            colour = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(screen, colour, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
