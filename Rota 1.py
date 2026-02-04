"""                      CÓDIGO PADRÃO DE MATRIZ
Matriz = []
    #linha  #dimensão (2x2, 3x3)
for i in range(x):
    Linha = []
       #Coluna
    for j in range(y):
        #Cria espaço vazio na lista Linha
        Linha.append(" ")
    #Adiciona as linhas e colunas da Matriz principal
    Matriz.append(linha)
"""
# - - - - - - - - - - - - - JOGO POKEMON PROVA - - - - - - - - -
import random

def mapainit(x,y):
    terreno = [
        ['  A',' A',' A',' A',' A','  ','  ',' A',' A',' A',' A',' A'],
        ['  A','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',' A'],
        ['  A','  ','  ','  ',' A','  ','  ','  ','  ','  ','  ',' A'],
        ['  A',' E',' E',' E',' A',' E',' E',' E',' G',' G',' G',' A'],
        ['  A','  ','  ','  ',' A',' G',' G',' G',' G',' G',' G',' A'],
        ['  A',' E',' E',' E',' A',' G',' G',' G',' G',' G',' G',' A'],
        ['  A','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',' A'],
        ['  A','  ','  ','  ','  ','  ','  ','  ',' G',' G',' G',' A'],
        ['  A',' A',' E',' E',' E',' A',' A',' A',' G',' G',' G',' A'],
        [' A','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',' A'],
        [' A',' E','  ',' E',' E','  ',' E',' E',' E',' E',' E',' A'],
        [' A','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',' A'],
        [' A','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',' A'],
        [' A',' A',' A',' A',' A',' A',' G',' G',' G',' E',' E',' A'],
        [' A','  ','  ','  ','  ','  ',' G',' G',' G','  ','  ',' A'],
        [' A','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',' A'],
        [' A',' E',' E','  ','  ',' E',' E',' E',' E',' E',' E',' A'],
        [' A','  ',' G',' G',' G',' G','  ','  ',' G',' G',' G',' A'],
        [' A',' G',' G',' G','  ','  ','  ',' G',' G','  ','  ',' A'],
        [' A',' A',' A',' A',' A',' A',' G',' A',' A',' A',' A',' A'],
        ]
    print('0  1  2  3  4  5  6  7  8  9 10 11 12')
    terreno[x][y] = ' J'
    for i in range(len(terreno)):
        print(f'{i+1}'+' '.join(terreno[i]))
    return terreno



def menu():
    print('\nBem vindo!\nA qualquer momento você pode escolher uma das opções:\n'
          '9- Abrir esse menu\n8- Subir \n2- Descer \n4- Ir para esquerda \n6- Ir para direita \n5- Abrir a pokedex \n0- Sair do jogo\n'
          )



def verifiAcao(acao):
    while acao not in ('0','2','4','5','6','8','9'):
        print('- - - - - - - - - - AÇÃO INVÁLIDA - - - - - - -')
        acao = input()
    acao = int(acao)
    return acao



def verifiEscolha(captura):
    while captura not in ('0','1','2'):
        print('- - - - - - - - - - AÇÃO INVÁLIDA - - - - - - -')
        captura = input()
    captura = int(captura)
    return captura

def verifiTerreno(acao,x,y):
    if terreno[x][y] == ' E':
        print('\n - - - - - - - Bump! VOCÊ BATEU A CABEÇA NUMA ELEVAÇÃO - - - - - - - - -\n')
        if acao == 8:
            x += 1
        elif acao == 2:
            x += 1
        elif acao == 4:
            y += 1
        elif acao == 6:
            y -= 1
    if terreno[x][y] == ' A':
        print('\n - - - - - - - Bump! VOCÊ BATEU A CABEÇA NUMA ÁRVORE - - - - - - - - -\n')
        if acao == 8:
            x += 1
        elif acao == 2:
            x -= 1
        elif acao == 4:
            y += 1
        elif acao == 6:
            y -= 1
    return acao, x, y



def grama(x,y,cont):
    if terreno[x][y] == ' G':
        chance = random.randint(1,2)
        if chance == 2:
            captura = input('Um pokemon selvagem apareceu!\nCapturar ou correr? [1-Capturar ou 2-Correr]\n')
            captura = verifiEscolha(captura)
            if captura == 2:
                print('Fujão!!!')
            elif captura == 1:
                novoPokemon()
                cont -= 1
                print(f'Parabéns, você capturou um pokemon! Faltam {cont}')
        return cont



def posicao(acao,x,y):
        if acao == 8:
            x -= 1
        elif acao == 2:
            x += 1
        elif acao == 4:
            y -= 1
        elif acao == 6:
            y += 1
        acao, x, y = verifiTerreno(acao,x,y)
        print(f'Sua posição atual é: [{x}][{y}]')
        return mapainit(x,y), x, y


def menuPokedex():
    print(pokedex)
    menupokedex = input("""Digite
1 para Listar Detalhes
2 para Apagar Registro
0 para voltar ao menu principal
Escolha uma ação:\n""")
    menupokedex = verifiEscolha(menupokedex)
    if menupokedex == 1:
        detalhes = input('Qual o nome do Pokemon?')
    elif menupokedex == 2:
        remover = input('Qual Pokemon deseja remover?\n')
        pokedex.remove(remover)
    else:
        return pokedex

    
def novoPokemon():
    stats = {}
    stats['Nome'] = pokemons[random.randint(0,9)]
    stats['Hp'] = random.randint(1,100)
    stats['Atk'] = random.randint(1,100)
    stats['Def'] = random.randint(1,100)
    stats['Sp.Atk'] = random.randint(1,100)
    stats['Sp.Def'] = random.randint(1,100)
    stats['Speed'] = random.randint(1,100)
    pokedex.append(stats)
    if stats['Nome'] in pokedex:
        print('Você já capturou esse pokemon')
        pokedex.pop()
    return pokedex, stats





pokemons = ['Ratata', 'Pidgey', 'Weedle', 'Caterpie', 'Paras', 'Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu', 'Evee']
pokedex = []
cont = 10
x = 19
y = 6
acao = 1
terreno = mapainit(x,y)
menu()
print('Entrando na Rota 1')
print(f'Sua posição atual é: [{x}][{y}]')
while acao != 0:
    acao = input()
    acao = verifiAcao(acao)
    if acao == 9:
        menu()
    elif acao == 5:
        menuPokedex()
    elif acao == 0:
        acao = 0
    else:
        acao, x, y = posicao(acao,x,y)
        if cont > 0:
            grama(x,y,cont)
    if x == 0 and y == 6 or x == 0 and y == 5:
        acao = 0
print('\nFim de jogo!!!\n')













"""for i in range(20):
    linha = []
    for j in range(12):
        linha.append(' ')
    terreno.append(linha)"""


