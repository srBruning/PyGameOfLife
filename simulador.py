import random
import time
import sys
import pygame
from game import game_of_life

WHITE = (255, 255, 255)

# plano vazio 
SEED =  [[0]* 50 for _ in range(50)]

# glider 
# SEED[23][24] = 1 
# SEED[24][25] = 1 

# SEED[25][23] = SEED[25][24] = SEED[25][25] = 1 


# Glider gun
SEED[20][30] = 1
SEED[21][28] = SEED[21][30] = 1
SEED[22][18] = SEED[22][19] = SEED[22][26] = SEED[22][27] = SEED[22][40] = SEED[22][41] = 1
SEED[23][17] = SEED[23][21] = SEED[23][26] = SEED[23][27] = SEED[23][40] = SEED[23][41] = 1
SEED[24][6]  = SEED[24][7]  = SEED[24][16] = SEED[24][22] = SEED[24][26] = SEED[24][27] = 1
SEED[25][6]  = SEED[25][7]  = SEED[25][16] = SEED[25][20] = SEED[25][22] = SEED[25][23] = SEED[25][28] = SEED[25][30] = 1
SEED[26][16] = SEED[26][22] = SEED[26][30] = 1
SEED[27][17] = SEED[27][21] = 1
SEED[28][18] = SEED[28][19] = 1

# Rich's p16
# SEED[19][20] = SEED[19][21] = SEED[19][22] = SEED[19][26] = SEED[19][27] = SEED[19][28] = 1
# SEED[20][19] = SEED[20][23] = SEED[20][25] = SEED[20][29] = 1
# SEED[21][19] = SEED[21][23] = SEED[21][25] = SEED[21][29] = 1
# SEED[22][18] = SEED[22][20] = SEED[22][21] = SEED[22][22] = SEED[22][23] = SEED[22][25] = SEED[22][26] = SEED[22][27] = SEED[22][28] = SEED[22][30] = 1
# SEED[23][18] = SEED[23][19] = SEED[23][29] = SEED[23][30] = 1
# SEED[26][22] = SEED[26][23] = SEED[26][22] = SEED[26][25] = SEED[26][26] = 1
# SEED[27][21] = SEED[27][23] = SEED[27][25] = SEED[27][27] = 1
# SEED[28][22] = SEED[28][26] = 1

# Random
# SEED = [[random.choice([0, 1]) for _ in range(50)] for _ in range(50)]

pygame.init()

screen = pygame.display.set_mode((550, 550))

def draw_matrix(matrix):
    '''
    Função para desenhar o plano
    '''
    screen.fill([0,0,0])

    # percorre o plano desenhando as células
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell:
                # caso célula esteja viva pinta de branco
                pygame.draw.rect(screen, WHITE, (11*c, 11*r, 10, 10))

font = pygame.font.SysFont(None, 30)
txtMenu=[]
txtMenu.append(font.render('space: run game of life', True, (255,0,0)))
txtMenu.append(font.render('escape: exit', True, (255,0,0)))
txtMenu.append(font.render('mouse: draw', True, (255,0,0)))
txtMenu.append(font.render('space: next', True, (0,0,255)))

while True:
    p =20
    for m in txtMenu :
        screen.blit(m, [20, p])
        p+=20
    event = pygame.event.poll()

    if event.type ==  pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif (event.type == pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        else:
            break
    pygame.display.flip()
    time.sleep(0.03)


seed = SEED

draw_matrix(seed)

pygame.display.flip()

time.sleep(1)
in_game = False
mouse_press = False
while True:
    # processamento de entrada
    event = pygame.event.poll()

    if event.type ==  pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif (event.type == pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif (event.key == pygame.K_SPACE):
            in_game = not in_game
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_press = True
    elif event.type == pygame.MOUSEBUTTONUP:
        mouse_press = False

    if mouse_press:
        x, y = pygame.mouse.get_pos()
        seed[int(y/11)][int(x/11)] = 1

    # ATUALIZAÇÃO DO JOGO 
    
    if in_game:
        # aplica o game of life para processar a geração seguinte
        seed = game_of_life(seed)

    # DESENHO

    # desenha a nova geração na tela
    draw_matrix(seed)

    pygame.display.flip()

    if in_game:
        time.sleep(0.03)
    else:
        time.sleep(0.01)