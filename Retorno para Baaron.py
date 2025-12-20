import random

def dialogo():
    conversa = input('''\n\n\n=====================================================================================================================
Imediato: Mestre Cecil, a tripulação está indagando se foi certo o que fizemos ao roubar o cristal das mãos civís.
=====================================================================================================================
Pressione Enter para continuar.''')
    while conversa not in (''):
        conversa = input()


def verifiAcao(lista, acao):
    while acao not in lista:
        acao = input(' - - - - - - ACAO INVALIDA - - - - -')
    acao = int(acao)
    return acao


def stats():
    global persona
    for x in range(3):
        dic = {}
        if x == 0:
            dic['nome'] = 'Cecil'
            dic['imagem'] = '''                                %%%%                             &%%&
                              .            %%%%                             &%%&
                              .           *    %                           %%%%%%
                              .           & %%%                            &%%%%%
                              .           & %%%                            &%%%%%
                              .           &%%%%&                           %%%%%%%
                              .   &%%%%%%%%%%%%%%%%%% &             %%%%%%%%%%%%%%%%%%%%&
                              .&%%%&  %%,  %% %/%%%  ,&%%%       %%%&.  %%%%%%%%%% %#  &%%%%
                              .          , %    %%                       &&%%%%%%%
                              .          // .  *                           %%%%%%
                              .          ,* ,  *                           %%%%%%
                              .          .* *  /                           %%%%%%
                              .           * *  /                           %%%%%%
                              .           , ,  /                           %%%%%%
                              .           , ,  (                           %%%%%%
                              .           . ,  #                           %%%%%%
                              .           . .  #                           %%%%%%
                              .             .  %                           %%%%%%
                              .             .  %                           %%%%%%
                              .             .  &                           %%%%%%
                              .             .  &                           %%%%%%
                              .             .  %                           %%%%%%
                              .                %                           %%%%%%
                              .                %                           %%%%%%
                              .               .%                           %%%%%%
                              .               %&                           %%%%%%
                              .               %/                           %%%%%%
                              .               ,                             %%%%%
                              .           %                                 %%%%%
                              .            ,  /                             %%%%
                              .            %                                 %%%'''
            dic['tipo'] = 'Protagonista'
            dic['atk'] = random.randint(1,20)
            dic['def'] = random.randint(1,10)
            dic['hp'] = random.randint(1,100)
            dic['agil'] = random.randint(0,2)
        elif x == 1:
            dic['nome'] = 'Olhão'
            dic['imagem'] = """          /@&&&@&@@,                                                                                  (@&&&&&&@.        
     #&&&&,             /@&%                                                                 (@&%.            ./&&&&.   
   @&&&     ,&&&&   ,&         @&&%                                                   .@&&.         &   ,&&&%     .&&&. 
  #              /@   ,.          * /  .(@&&&&&&%                       ,@&&&&&&&/  @ &    (      &   .&               ,
                  ,@   &      (   &        .&&@@@(.@                 ,&,@@@&&@             @     *.  .&                 
                  (@   &    &%    .*%&&/    &                                (   ,@&%(,.    &/   /&   &                 
               (&&*       &#     .     &   .&                               /@    .    *      &#       &&@,             
        .&&&&&&&&&&&&&%     @       @   #@  &&                              &/  &    * (    @     .@&&&&&&&&&&&&&       
       *&%            &&&*   %    .,&&@,     &&      .&&@&,    .&@&@.     (&&     %&& @    *    &&&#           .&&      
                       /&&,      *&.     .@.   &&&&&&    @&&@@&&&    &&&&&#   %#      &&       &&&                      
                        &&     %&     #  &&&&&@/&&&   ,&.        ,&    @&@#&&&&&%  #     &     &&&                      
                       *&,    & .&@&&&&@&      &&*    &   %&&&&    &    *&/     .&&&&&&&% ,%    &&                      
                       &&   &&&@*       (@&&& &&@     &*  /&&&&   *@     @&.,&&&%,       %&&&/  *&                      
                       &&/&&,                &&&&      @%        &&      &&&.                &&&&&.                     
                       *&&&,                   .&        /&&&&&&%       *@                    &&&&                      
                        ,&&@                     &,                    &#                     &&@                       
                           %&*                    (&#               ,&%                     @@,                         
                                                     .&&@@*   *@&&@"""
            dic['tipo'] = 'Monstro'
            dic['atk'] = random.randint(1,20)
            dic['def'] = random.randint(1,10)
            dic['hp'] = random.randint(1,80)
            dic['agil'] = random.randint(0,2)
        else:
            dic['nome'] = 'Olhudo'
            dic['imagem'] = """          /@&&&@&@@,                                                                                  (@&&&&&&@.        
     #&&&&,             /@&%                                                                 (@&%.            ./&&&&.   
   @&&&     ,&&&&   ,&         @&&%                                                   .@&&.         &   ,&&&%     .&&&. 
  #              /@   ,.          * /  .(@&&&&&&%                       ,@&&&&&&&/  @ &    (      &   .&               ,
                  ,@   &      (   &        .&&@@@(.@                 ,&,@@@&&@             @     *.  .&                 
                  (@   &    &%    .*%&&/    &                                (   ,@&%(,.    &/   /&   &                 
               (&&*       &#     .     &   .&                               /@    .    *      &#       &&@,             
        .&&&&&&&&&&&&&%     @       @   #@  &&                              &/  &    * (    @     .@&&&&&&&&&&&&&       
       *&%            &&&*   %    .,&&@,     &&      .&&@&,    .&@&@.     (&&     %&& @    *    &&&#           .&&      
                       /&&,      *&.     .@.   &&&&&&    @&&@@&&&    &&&&&#   %#      &&       &&&                      
                        &&     %&     #  &&&&&@/&&&   ,&.        ,&    @&@#&&&&&%  #     &     &&&                      
                       *&,    & .&@&&&&@&      &&*    &   %&&&&    &    *&/     .&&&&&&&% ,%    &&                      
                       &&   &&&@*       (@&&& &&@     &*  /&&&&   *@     @&.,&&&%,       %&&&/  *&                      
                       &&/&&,                &&&&      @%        &&      &&&.                &&&&&.                     
                       *&&&,                   .&        /&&&&&&%       *@                    &&&&                      
                        ,&&@                     &,                    &#                     &&@                       
                           %&*                    (&#               ,&%                     @@,                         
                                                     .&&@@*   *@&&@"""
            dic['tipo'] = 'Monstro'
            dic['atk'] = random.randint(1,20)
            dic['def'] = random.randint(1,10)
            dic['hp'] = random.randint(1,80)
            dic['agil'] = random.randint(0,2)
        persona.append(dic)
        
        

def itens():
    bolsa = []
    nPocoes = random.randint(0,3)
    if nPocoes != 0:
        pocoes = {
        'pAtk': random.randint(10,20),
        'pDef': random.randint(10,20),
        'pHp': random.randint(10,20),
        }
        for i in range(nPocoes):
            linha = []
            pocaoAleatoria = random.choice(list(pocoes.items()))
            linha.append(pocaoAleatoria)
            bolsa.append(linha)
    print(*bolsa)

def ordem(persona):
    global posicaoCecil
    n = len(persona)
    for i in range(n):
        for j in range(0, n-i-1):
            if persona[j]['agil'] > persona[j+1]['agil']:
                persona[j], persona[j+1] = persona[j+1], persona[j]
    mostraPersona(persona)
    for y in range(len(persona)):
        if persona[y]['nome'] == 'Cecil':
            posicaoCecil = y
        elif persona[y]['nome'] == 'Olhão':
            posicaoOlhao = y
        elif persona[y]['nome'] == 'Olhudo':
            posicaoOlhudo = y
    return persona


def mostraPersona(persona):
    for x in range(len(persona)):
        for chave,valor in persona[x].items():
            print(f'{chave} = {valor}')
    

def combate(persona):
    if persona[0]['tipo'] == 'Monstro':
        dano = persona[0]['atk'] - persona[posicaoCecil]['def']
        if dano <= 0:
            print(' - - - - - - - O ataque não surtiu efeito - - - - -')
            acao = input('='*120+f'\nPressione enter para continuar\n'+'='*120)
            while acao not in (''):
                acao = input(' - - - - - - ACAO INVALIDA - - - - -')
        else:
            persona[posicaoCecil]['hp'] = persona[posicaoCecil]['hp'] - dano
            print('='*120, f'\nCecil sofeu dano e perdeu {dano} pontos de vida\n', '='*120)
            acao = input(f'\nPressione enter para continuar\n')
            while acao not in (''):
                acao = input(' - - - - - - ACAO INVALIDA - - - - -')
            
    if persona[0]['tipo'] == 'Protagonista':
        persona[0]['bolsa'] = itens()
        acao = input('''Opções:
0 - Atacar
1 - Usar item
2 - Fugir\n''')
        lista = ['0','1','2']
        acao = verifiAcao(lista,acao)
        if acao == 2:
            batalha = False
            return batalha
        menuCecil(acao)
        
def menuCecil(acao):
    acao = input('''Escolha um inimigo para atacar
0 - Olhudo
1 - Olhão\n''')
    lista = ['0','1']
    acao = verifiAcao(lista,acao)
    if acao == 0:
        dano = persona[posicaoCecil]['atk'] - persona[posicaoOlhudo]['def']
        if dano <= 0:
            print(' - - - - - - - O ataque não surtiu efeito - - - - -')
        else:
            persona[posicaoOlhudo]['hp'] = persona[posicaoOlhudo]['hp'] - dano
            print('='*120, f'\nOlhudo sofeu dano e perdeu {dano} pontos de vida\n', '='*120)
            return persona[posicaoOlhudo]['hp']
    elif acao == 1:
        dano = persona[posicaoCecil]['atk'] - persona[posicaoOlhao]['def']
        if dano <= 0:
            print(' - - - - - - - O ataque não surtiu efeito - - - - -')
        else:
            persona[posicaoOlhao]['hp'] = persona[posicaoOlhao]['hp'] - dano
            print('='*120, f'\nOlhão sofeu dano e perdeu {dano} pontos de vida\n', '='*120)
            return persona[posicaoOlhao]['hp']
    if persona[posicaoCecil]['hp'] <= 0:
        print('='*120, f'\nCecil morreu. Fim de jogo\n', '='*120)
    elif persona[posicaoOlhao]['hp'] and persona[posicaoOlhudo]['hp'] <= 0:
        print('='*120, f'\nCecil venceu. Fim de jogo\n', '='*120)





persona = []
conversa = '0'
dialogo()
stats()
ordem(persona)

batalha = True
while batalha:
    for chave,valor in persona[0].items():
        print(f'{chave} = {valor}')
        print('')
    combate(persona)






"""
for x in range(len(persona)):
    for chave, valor in persona[x].items():
        print(f'{chave}  =  {valor}')
"""
