# Ler número inteiro e ver se é primo (divisível por 1 e por ele mesmo)
n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;32m', end='')
        tot += 1
    else:
        print('\033[1;30m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisível por {} números.'.format(n, tot))
if tot == 2:
    print('Portanto, ele é primo')
else:
    print('Portanto, ele não é primo.')
