import random


def empty_seed():
    return  [[0]* 50 for _ in range(50)]

def glider():
    SEED = empty_seed()
    SEED[23][24] = 1 
    SEED[24][25] = 1 
    SEED[25][23] = SEED[25][24] = SEED[25][25] = 1 
    return SEED

def glider_gun():
    SEED = empty_seed()
    SEED[20][30] = 1
    SEED[21][28] = SEED[21][30] = 1
    SEED[22][18] = SEED[22][19] = SEED[22][26] = SEED[22][27] = SEED[22][40] = SEED[22][41] = 1
    SEED[23][17] = SEED[23][21] = SEED[23][26] = SEED[23][27] = SEED[23][40] = SEED[23][41] = 1
    SEED[24][6]  = SEED[24][7]  = SEED[24][16] = SEED[24][22] = SEED[24][26] = SEED[24][27] = 1
    SEED[25][6]  = SEED[25][7]  = SEED[25][16] = SEED[25][20] = SEED[25][22] = SEED[25][23] = SEED[25][28] = SEED[25][30] = 1
    SEED[26][16] = SEED[26][22] = SEED[26][30] = 1
    SEED[27][17] = SEED[27][21] = 1
    SEED[28][18] = SEED[28][19] = 1
    return SEED

def richs_p16():
    '''
    Rich's p16
    '''
    SEED = empty_seed()
    SEED[19][20] = SEED[19][21] = SEED[19][22] = SEED[19][26] = SEED[19][27] = SEED[19][28] = 1
    SEED[20][19] = SEED[20][23] = SEED[20][25] = SEED[20][29] = 1
    SEED[21][19] = SEED[21][23] = SEED[21][25] = SEED[21][29] = 1
    SEED[22][18] = SEED[22][20] = SEED[22][21] = SEED[22][22] = SEED[22][23] = SEED[22][25] = SEED[22][26] = SEED[22][27] = SEED[22][28] = SEED[22][30] = 1
    SEED[23][18] = SEED[23][19] = SEED[23][29] = SEED[23][30] = 1
    SEED[26][22] = SEED[26][23] = SEED[26][22] = SEED[26][25] = SEED[26][26] = 1
    SEED[27][21] = SEED[27][23] = SEED[27][25] = SEED[27][27] = 1
    SEED[28][22] = SEED[28][26] = 1
    return SEED

def random_game():
    return [[random.choice([0, 1]) for _ in range(50)] for _ in range(50)]
