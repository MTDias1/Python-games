import random

"""              
monstros.keys()
entrada = input()
for nomes in monstros.keys():
    if entrada == nomes:
        print(entrada)
"""

def menuInicio():
    print('''1 - Iniciar duelo
2 - Exibir placar
0 - Encerrar o jogo'''
          )
    
def verifiMenu(escolha):
    while escolha not in ('1','2','3'):
        escolha = input('  - - - - - - - Entrada inválida - - - - - -')
    escolha = int(escolha)
    return escolha


def duelistas(nome1,nome2):
    mao1 = []
    for i in range(len(monstros)):
        cartaAleatoria = random.choice(list(monstros.keys()))
        mao1.append(cartaAleatoria)
    joga1 = {
        nome1:
            {'vida':8000,
             'baralho': monstros,
             'mão': mao1,
             campo = [],
             cemiterio = []
        }
    mao2 = []
    for j in range(len(monstros)):
        random.choice(list(monstros.keys()))
        mao2.append(cartaAleatoria)
    joga2 = {
        nome2:
            {'vida':8000,
             'baralho': monstros,
             'mão': mao2,
             campo = [],
             cemiterio = []
        }
    print(mao1, mao2, joga1, joga2)

monstros = {
    'Dragão':{'ATK': 2500, 'DEF': 2000}
    'Mago negro':{'ATK': 2100, 'DEF': 1800}
    'Guardião Celta':{'ATK': 1400, 'DEF': 1200}
    'Curiboh':{'ATK': 300, 'DEF': 200}
    'Gigante de Pedra':{'ATK': 1300, 'DEF': 2000}
    }

partida = 1
while partida != 0:
    menuInicio()
    escolha = input()
    escolha = verifiMenu(escolha)
    if escolha == 1:
        nome1 = input('Escolha seu Nickname')
        nome2 = input('Escolha seu Nickname')
        duelistas(nome1,nome2)
    else:
        pass
