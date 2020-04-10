# ex028 é a v1.0 do jogo. Fazer várias tentativas até acertar o número que o computador 'pensou'
# número int entre 0 e 10

from random import randint
pc = randint(0, 10)
print('''Sou seu computador,...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue acertar com menos de 4 tentativas?''')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Seu palpite: '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente novamente')
        else:
            print('Menos... Tente novamente')
print(f'Acertou com {palpite} tentativas!', end=' ')
if palpite <= 3:
    print('Parabéns!')
else:
    print('Better luck next time!')
