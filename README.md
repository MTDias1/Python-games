# Python-games
Some game-based software that I developed at UPE (Universidade de Pernambuco), to practice my programming logic

# Rota 1
Nesse software, a ideia era recriar a cena das primeiras versões do jogo pokemon, a Rota 1, em texto.<br>
O objetivo era seu personagem representado pela letra J (Jogador) atravessar todo o mapa em uma matriz com alguns obstáculos<br>
O primeiro deles sendo as árvores, que impediam completamente a passagem do jogador em qualquer direção<br>
O segundo sendo as elevações que permitiam a movimentação apenas por uma direção, e não ficar em cima delas<br>
E o último a grama, que o jogador poderia se movimentar, mas há uma chance do jogador ser interrompido por um pokemon selvagem, que o jogador pode escolher capturar ou fugir.<br>
Ao fugir a interação se encerra e o jogador pode se movimentar novamente. Mas quando escolhe captrar, o pokemon é adicionado à lista Pokedex, e cada pokemon tem um dicionário com atributos próprios e aleatórios.<br>
A pokedex também pode ser interagida para ver os pokemons

# Retorno para Baaron
Nesse, era recriar a cena de combate de Cecil, o protagonista, com dois inimigos independentes com atributos aleatórios.<br>
O diferencial é a dinâmica de combate por turnos, a atualização do dicionário de atributos dos inimigos e do Cecil, e a lógica para impedir que:<br>
A) Cecil se ataque na sua vez<br>
B) O inimigo se ataque na sua vez<br>
C) O inimigo ataque seu aliado
