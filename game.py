import pygame
import random

from image_process import image
from main import Board

black =  (0,0,0)
white = (255,255,255)
width = 1 #20, 8
height = 1 #20, 8
margin = 1 #5, 2

#grid = Board([[random.randint(0, 1) for i in range(240)] for j in range(1500)])
img = image('Resources/delhi_contrasting.jpg')
img.compress(840, 600)
img.convert_to_black()
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
#window_size = [1200, 750] # ratio 1.6
window_size = [1600, 1000]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("GRID")
clock = pygame.time.Clock()
done = False

pause = False
first_loop = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: pause = True
            if event.key == pygame.K_s: pause = False
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
    if first_loop:
        pygame.image.save(screen, "Resources/initila_screenshot.jpeg")
        first_loop = False
    if not pause:
        grid.update()
    #frames per sec
    clock.tick(30)
    pygame.display.flip()

pygame.quit()


