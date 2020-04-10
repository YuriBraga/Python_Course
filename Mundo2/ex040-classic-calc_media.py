# Exercício clássico de cálculo de média (nota<5 Reprovado, 5<=nota<=6.9 Recu, nota>7 Aprov)
import math

n1 = float(input('Nota da P1: '))
n2 = float(input('Nota da P2: '))

med = (n1 + n2)/2
print('O aluno tirou {:.1f} e {:.1f}'.format(n1, n2))

if med < 5:
    print('\033[1;31mLogo, está reprovado com média {:.1f}\033[m'.format(med))
elif 5 <= med < 7:
    print('\033[1;33mLogo, está de recuperação com média {:.1f}\033[m'.format(med))
elif med >= 7:
    print('\033[1;32mLogo, está aprovado com média {:.1f}\033[m'.format(med))
