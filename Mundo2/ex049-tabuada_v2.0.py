# v1.0 é o ex009 da tabuada
n = int(input('Digite um número inteiro para ver sua tabuada: '))
for c in range(0, 17):
    print('{} x {} = {}'.format(n, c, n*c))
