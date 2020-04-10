# Jokenpo - Pedra Papel Tesoura

from random import randint  # Randomizar a escolha do PC
from time import sleep  # Dar um tempo entre uma string da outra

item = ('Pedra', 'Papel', 'Tesoura')  # Biblioteca
pc = randint(0, 2)

print('''Suas opções:\033[1;30m
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura\033[m''')
opt = int(input('Sua jogada: '))

if opt == 0 or opt == 1 or opt == 2:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!')
    sleep(1)

    print('-=-'*10)
    print('O computador jogou {}'.format(item[pc]))
    print('Você jogou {}'.format(item[opt]))
    print('-=-'*10)

    if pc == 0:  # Pedra
        if opt == 0:
            print('Empate!')
        elif opt == 1:
            print('Você ganhou!')
        elif opt == 2:
            print('Computador ganhou!')

    elif pc == 1:  # Papel
        if opt == 0:
            print('Computador ganhou!')
        elif opt == 1:
            print('Empate!')
        elif opt == 2:
            print('Você ganhou!')

    elif pc == 2:  # Tesoura
        if opt == 0:
            print('Você ganhou!')
        elif opt == 1:
            print('Computador ganhou!')
        elif opt == 2:
            print('Empate!')
else:
    print('\033[1;31mJOGADA INVÁLIDA\033[m')
