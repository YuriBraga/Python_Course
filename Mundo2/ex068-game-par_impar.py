# Jogo só é interrompido quando o jogador perder mostrando o total de vitórias
from random import randint
v = 0
while True:
    player = int(input('Digite um valor inteiro: '))
    pc = randint(0, 10)
    tot = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip()[0].upper()
    print(f'Você jogou {player} e o computador {pc}. Total de {tot}')
    print('DEU PAR' if tot % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes')
