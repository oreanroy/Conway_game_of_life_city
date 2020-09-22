import pygame
import random

from image_process import image
from main import Board

black =  (0,0,0)
white = (255,255,255)
width = 20
height = 20
margin = 5

grid = Board([[random.randint(0, 1) for i in range(40)] for j in range(24)])
img = image('Resources/delhi_img.PNG')
img.convert_to_black()
img.compress(40, 24)
grid = Board(img.get_binary_arr())
#grid = Board([[0,0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,1,0,0,0,0,0,0],
#              [0,0,0,0,0,1,0,0,0,0,0],
#              [0,0,0,1,1,1,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0,0,0,0]])

pygame.init()
# width, height (25*40), (25*24) (each cell of width/height 25)
window_size = [1000, 600]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("GRID")
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # think of replacing with round off
            cell_col = pos[0]//25
            cell_row = pos[1]//25
            grid.set_arr_live(cell_row, cell_col)
            print(pos)
            print(cell_col, cell_row)

    screen.fill(black)
    for row in range(grid.get_row()):
        for col in range(grid.get_col()):
            color = black
            if grid.get_arr()[row][col]==1:
                color = white
            pygame.draw.rect(screen, color,
                             [(margin+width)*col+margin,
                              (margin+height)*row+margin,
                             width,
                             height])
    grid.update()
    #frames per sec
    clock.tick(60)
    pygame.display.flip()

pygame.quit()

