from random import randint
from time import sleep

#funções
def limparTela():
    print('\n'*100)

def cabecalho():
    print('{:^50}'.format('=' * 50))
    print('{:^50}'.format('JOGO DA VELHA'))
    print('{:^50}'.format('=' * 50))

def boasvindas():
    limparTela()
    cabecalho()
    print('{:^50}'.format('Bem-vindo ao jogo da velha!!'))
    print('{:^50}'.format('-' * 50))

def placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, simboloP1):
    limparTela()
    cabecalho()
    if simboloP1 == '1':
        simboloP1 = 'o'
        simboloP2 = 'x'
    elif simboloP1 == '2':
        simboloP1 = 'x'
        simboloP2 = 'o'
    print(' '*9, f'{nomeP1[0:15]:.<15}({simboloP1}): {vitoriasP1} vitórias')
    print(' '*9, f'{nomeP2[0:15]:.<15}({simboloP2}): {vitoriasP2} vitórias')
    print(' '*9, f'Empates...........: {empates}')
    print('{:^50}'.format('=' * 50))

def tabuleiro (c1, c2, c3, c4, c5, c6, c7, c8, c9):
    print('{:^19}'.format('MAPA DO JOGO'), '          ', '{:^19}'.format('JOGO EM ANDAMENTO'))
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  1  │  2  │  3  │', '          ', f'│  {c1}  │  {c2}  │  {c3}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  4  │  5  │  6  │', '          ', f'│  {c4}  │  {c5}  │  {c6}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  7  │  8  │  9  │', '          ', f'│  {c7}  │  {c8}  │  {c9}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print()
    print('{:^50}'.format('=' * 50))


def opcaoInicial():
    while True:
        boasvindas()
        print('Escolha...\n'
              '[0] para conhecer as regras\n'
              '[1] para ser " o "\n'
              '[2] para ser " x "\n')
        opcao = input('Qual a sua opção? ').strip()
        while opcao != '0' and opcao != '1' and opcao != '2':
            opcao = input('Opção inválida. Qual a sua opção? [0/1/2] ').strip()
        if opcao == '0':
            regras()
        if opcao == '1' or opcao == '2':
            break
    return opcao

def opcaoPlayer():
    print('Escolha...\n'
          '[1] para jogar contra o computador\n'
          '[2] para jogar contra outra pessoa\n')
    opcao = input('Qual a sua opção? ').strip()
    while opcao != '1' and opcao != '2':
        opcao = input('Opção inválida. Qual a sua opção? [1/2] ').strip()
    return opcao

def regras():
    limparTela()
    cabecalho()
    print('|{:^48}|'.format('REGRAS DO JOGO'))
    print('{:^50}'.format('-' * 50))
    print("""
- O tabuleiro  é uma matriz  de três linhas por
três colunas.
- Dois jogadores escolhem uma marcação cada um,
geralmente um círculo (o) e um xis (x).
- Os jogadores jogam alternadamente, uma marcação
por vez, numa lacuna que esteja vazia.
- O objectivo é conseguir três círculos ou três
xis em linha, quer horizontal, vertical ou
diagonal , e ao mesmo tempo, quando possível,
impedir o adversário de ganhar na próxima jogada.

Pronto para jogar?
""")
    input('Tecle enter para continuar!')

def dica():
    print("""Dica: para jogar, escolha o número de uma casa que
      esteja disponível no tabuleiro da direita.
Digite " novo " para reiniciar com novos jogadores.
Digite " sair " para encerrar o aplicativo.
Digite " zerar " para zerar o placar""")
    print('{:^50}'.format('=' * 50))


#execução
jogada = ''
while True:
    # variaveis do jogo
    nomeP1 = ''
    nomeP2 = ''
    simboloP1 = ''
    simboloP2 = ''
    vitoriasP1 = 5
    vitoriasP2 = 4
    empates = 0
    # variaveis dos campos do tabuleiro
    c1 = ' '
    c2 = ' '
    c3 = ' '
    c4 = ' '
    c5 = ' '
    c6 = ' '
    c7 = ' '
    c8 = ' '
    c9 = ' '

    opcaoUsuario = opcaoInicial()
    nomeP1 = input('Qual o seu nome? ')
    if opcaoUsuario == '1':
        simboloP1 = 'o'
        simboloP2 = 'x'
    elif opcaoUsuario == '2':
        simboloP1 = 'x'
        simboloP2 = 'o'

    jogadores = opcaoPlayer()
    if jogadores == '2':
        nomeP2 = input('Qual o nome do segundo jogador? ')
    else:
        nomeP2 = 'Computador'
    proximoJogador = ''

    while True:
        if jogada == 'sair':
            break
        elif jogada == 'novo':
            jogada = ''
            break
        elif jogada == 'zerar':
            vitoriasP1 = 0
            vitoriasP2 = 0
            empates = 0
            # variaveis dos campos do tabuleiro
            c1 = ' '
            c2 = ' '
            c3 = ' '
            c4 = ' '
            c5 = ' '
            c6 = ' '
            c7 = ' '
            c8 = ' '
            c9 = ' '

        placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, opcaoUsuario)
        tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
        dica()

        if proximoJogador == '' or proximoJogador == nomeP2:
            proximoJogador = nomeP1
            proximoSimbolo = simboloP1
        else:
            proximoJogador = nomeP2
            proximoSimbolo = simboloP2
        while True:
            jogada = input(f'É a vez do {proximoJogador}({proximoSimbolo}): ').strip().lower()
            if jogada == 'sair' or jogada == 'novo' or jogada == 'zerar':
                break
            if jogada.isnumeric():
                if int(jogada) >= 1 or int(jogada) <= 9:
                    if jogada == '1' and c1 == ' ':
                        c1 = proximoSimbolo
                        break
                    elif jogada == '2' and c2 == ' ':
                        c2 = proximoSimbolo
                        break
                    elif jogada == '3' and c3 == ' ':
                        c3 = proximoSimbolo
                        break
                    elif jogada == '4' and c4 == ' ':
                        c4 = proximoSimbolo
                        break
                    elif jogada == '5' and c5 == ' ':
                        c5 = proximoSimbolo
                        break
                    elif jogada == '6' and c6 == ' ':
                        c6 = proximoSimbolo
                        break
                    elif jogada == '7' and c7 == ' ':
                        c7 = proximoSimbolo
                        break
                    elif jogada == '8' and c8 == ' ':
                        c8 = proximoSimbolo
                        break
                    elif jogada == '9' and c9 == ' ':
                        c9 = proximoSimbolo
                        break
                    else:
                        print('Opção inválida, por favor escolha uma casa que esteja disponível e digite seu número!')
                else:
                    print('Opção inválida, por favor escolha uma casa que esteja disponível e digite seu número!')
            else:
                print('Opção inválida, por favor escolha uma casa que esteja disponível e digite seu número!')
    if jogada == 'sair':
        print('='*50)
        print('Obrigado por jogar!!!Espero que tenha gostado!!!')
        print('='*50)
        break