import time
import sys
import pygame
from game import game_of_life
import game_seed as gseed

WHITE = (255, 255, 255)

# plano vazio 
SEED = gseed.random_game()
 
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

def loop_game(seed):
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
                break
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


def loop_menu():
    font = pygame.font.SysFont(None, 30)
    txtMenu=[]
    txtMenu.append(font.render('space: run game of life', True, (255,0,0)))
    txtMenu.append(font.render('escape: exit', True, (255,0,0)))
    txtMenu.append(font.render('mouse: draw', True, (255,0,0)))
    txtMenu.append(font.render('space: next', True, (0,0,255)))

    txtMenu.append(font.render('space: next empity game', True, (0,0,255)))
    txtMenu.append(font.render('q: seed glider', True, (0,0,255)))
    txtMenu.append(font.render('w: seed glider gun', True, (0,0,255)))
    txtMenu.append(font.render("e: seed rich's p16", True, (0,0,255)))
    txtMenu.append(font.render('r: seed random seed', True, (0,0,255)))


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
            elif event.key == pygame.K_q:
                loop_game(gseed.glider())
            elif event.key == pygame.K_w:
                loop_game(gseed.glider_gun())
            elif event.key == pygame.K_e:
                loop_game(gseed.richs_p16())
            elif event.key == pygame.K_r:
                loop_game(gseed.random_game())
            else:
                print(event.key)
                loop_game(gseed.empty_seed())
        pygame.display.flip()
        time.sleep(0.03)            


loop_menu()