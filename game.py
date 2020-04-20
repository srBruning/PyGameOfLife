
def cell_check(section):
    '''
    Executa as regras do game if life em um recorte 3x3 para
    saber o estado da célula central
    '''
    # contador de visinhos
    neighbords = 0
    center = section[1][1]

    # soma todos os  elementos do grupo 
    for row in section:
        for cell in row:
            neighbords += cell
    
    # desconta o valor da célula central
    neighbords -= center

    # aplia as regras do 'game of life'
    if neighbords <=1 :
        # menos de dosi visinhos a célula morre por baixa população
        center = 0
    elif neighbords ==3 :
        # exatamente 3 a célula nasce por reprodução
        center = 1
    elif neighbords >=4 :
        #  mais que 3 a célula morre por superpopulação
        center = 0
    
    return center

def get_section(matrix, row, col):
    '''
    extrai um recorte 3x3 de um plano dado uma célula central
    '''
    # monta um plano 3x3 somente com células mortas para receber a cópia da área
    section = [[0 for _ in range(3)] for _ in range(3)]

    for sec_r, r in enumerate(range(row-1, row+2)):
        for sec_c, c in enumerate(range(col-1, col+2)):
            section[sec_r][sec_c] = matrix[r % 50][c % 50]
    
    return section

def game_of_life(seed):
    '''
    Recebe um seed de um plano 50x50, executa o game of life 
    e devolve a geração seguinte
    '''

    # cria um plano vazio para armazenar a geração seguinte
    next_gen = [[0 for _ in range(50)] for _ in range(50)]


    # percorre o plano tirando recortes 3x3 e os avalia
    for r, row in enumerate(seed):
        for c, col in enumerate(row) :
            next_gen[r][c] = cell_check(get_section(seed, r, c))
    
    return next_gen
