from random import randint
from time import sleep
comp = randint(0, 10) # Faz o computador pensar
print('-=-'*20)
print('Vou pensar em um número inteiro de 0 a 10, tente adivinhar...')
print('-=-'*20)
pense = int(input('Em que número pensei?')) # Tentativa do Jogador
print('PROCESSANDO...')
sleep(2)
if pense == comp:
    print('Acertô mizeravi')
else:
    print('Melhore sua leitura de HD... Pensei no número {} e não {}.'.format(comp, pense))
print('Volte sempre!')
