import pygame
from copy import deepcopy
from random import choice, randrange

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
FPS = 60

pygame.init()

game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W  //2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TILE - 2,TILE - 2)
field = [[0 for i in range(W)] for j in range(H)]
anim_count, anim_speed, anim_limit = 0, 60, 2000

figure = deepcopy(choice(figures))

get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))
color = get_color()

def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    elif figure[i].y > H -1 or field[figure[i].y][figure[i].x]:
        return False
    return True 

while True:
    dx, rotate = 0, False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 100 
            elif event.key == pygame.K_UP:
                rotate = True  
    # mover x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break
        
        #mover y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
              for i in range(4):
                field[figure_old[i].y][figure_old[i].x] = color
                color = get_color()
              figure = deepcopy(choice(figures))
              anim_limit = 60
              break
    # rotate 
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x  - center.x
            figure[i].x = center.x - x
            figure[y].y = center.y + y
            if not check_borders():
               figure = deepcopy(figure_old)
               break
           
    #Chequear las lineas
    line = H -1
    for row in range(H - 1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
                field[line][i] = field[row][i]
        if count < W:
            line -= 1
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid] 
    #draw figuras
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, color, figure_rect)
        
    # draw field
    for y, raw in enumerate(field):
       for x, col in enumerate(raw):
           if col:
               figure_rect.x,figure_rect.y = x * TILE, y * TILE
               pygame.draw.rect(game_sc, col, figure_rect)
        
    pygame.display.flip()
    clock.tick()
    