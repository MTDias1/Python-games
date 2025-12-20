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

def verifi_menu(opcao):
    while opcao not in ('0','1','2','3','4'):
        print("\n - - - - - - Selecione um valor adequado - - - - - - -\n")
        opcao = input()
    opcao = int(opcao)
    return opcao


def verifi_jogado(armador):
    while armador not in ('1','2'):
        print("\n - - - - - - Selecione um valor adequado - - - - - - -\n")
        armador = input()
    armador = int(armador)
    return armador


def verifi_terreno(coluna):
    while coluna not in ('1','2','3','4','5'):
        coluna = input("\n - - - - - - Selecione um valor adequado - - - - - - -\n")
    coluna = int(coluna)
    coluna = coluna - 1
    return coluna



def menu(): #PROCEDIMENTO NÃO TEM RETURN
    global jogo, opcao
    print(' \n1 - Definir Armador\n2 - Plantar Armadilhas\n3 - Iniciar com Andarilho \n4 - Mostrar o placar\n0 - Finalizar o Jogo')
    opcao = input()
    opcao = verifi_menu(opcao)
    if opcao == 0:
        jogo = False
    elif opcao == 1:
        # ARMADOR E ANDARILHO
        print('Qual jogador plantará as armadilhas?[1 ou 2]')
        armador = input()
        armador = verifi_jogado(armador)
        andarilho = 0
        if armador == 1:
            andarilho = 2
        elif armador == 2:
            andarilho = 1
        print(f'O armador é o jogador: {armador}\nO andarilho é o jogador: {andarilho}')

        opcao = int(input('Para prosseguir, digite a opção "2"\n'))
        if opcao == 0:
            menu()
        while opcao != 2:
            print("\n - - - - - - Selecione um valor adequado - - - - - - -\n")
            opcao = int(input('Para prosseguir, selecione a opção 2\n'))
        print('\n - - - - - - - PLANTANDO ARMADILHAS - - - - - - \n\n')
        terreno = []
        x = 5
        for i in range(x):
            linha = []
            for j in range(x):
                linha.append('A')
            terreno.append(linha)
        print(f'\n0 1 2 3 4 5')
        for i in range(len(terreno)):
            print(f'{i+1} ' + ' '.join(terreno[i]))
        print(f'Jogador {armador}, você pode esconder até 3 ovos podres por linha do terreno')
        for i in range(len(terreno)):
            print(f'Em qual coluna da linha {i+1} você quer esconder ovos podres? [1 a 5]\n(Digite 0 para não colocar ovo)')
            n_ovos = 0
            while n_ovos < 3:
                coluna = input()
                if coluna == '0':
                    n_ovos = 3
                else:
                    coluna = verifi_terreno(coluna)
                    if coluna == -1:
                        terreno[i][coluna] = 'A' 
                    else:
                        terreno[i][coluna] = 'O'
                    n_ovos += 1
                print(f'{i+1} ' + ' '.join(terreno[i]))
        print(f'\n - - - - -TERRENO - - - - -\n0 1 2 3 4 5')
        for i in range(len(terreno)):
            print(f'{i+1} ' + ' '.join(terreno[i]))
        opcao3 = input('Deseja passar para o andarilho ou reiniciar o terreno?\n[0 para menu\n1 para reinicio\n3 para passar]\n')
        while opcao3 not in ('0','3'): # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            terreno = []
            x = 5
            for i in range(x):
                linha = []
                for j in range(x):
                    linha.append('A')
                terreno.append(linha)
            print(f'\n0 1 2 3 4 5')
            for i in range(len(terreno)):
                print(f'{i+1} ' + ' '.join(terreno[i]))
            print(f'Jogador {armador}, você pode esconder até 3 ovos podres por linha do terreno')
            for i in range(len(terreno)):
                print(f'Em qual coluna da linha {i+1} você quer esconder ovos podres? [1 a 5]\n(Digite 0 para não colocar ovo)')
                n_ovos = 0
                while n_ovos < 3:
                    coluna = input()
                    if coluna == '0':
                        n_ovos = 3
                    else:
                        coluna = verifi_terreno(coluna)
                        if coluna == -1:
                            terreno[i][coluna] = 'A' 
                        else:
                            terreno[i][coluna] = 'O'
                        n_ovos += 1
                    print(f'{i+1} ' + ' '.join(terreno[i]))
            print(f'\n - - - - -TERRENO - - - - -\n0 1 2 3 4 5')
            for i in range(len(terreno)):
                print(f'{i+1} ' + ' '.join(terreno[i]))
            opcao3 = input('Deseja passar para o andarilho ou reiniciar o terreno?\n[0 para menu\n1 para reinicio\n3 para passar]\n')
        if opcao3 ==0:
            menu()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        for i in range(100):
            print('=' * i)
        
        


jogo = True
while jogo:
    menu()
    
































