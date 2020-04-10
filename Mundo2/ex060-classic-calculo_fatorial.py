# Calcular o fatorial de qualquer número

from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'{n}! = {f}')
# Não é toda linguagem que possui 'factorial' na sua biblioteca... logo, fazer do jeito tradicional:

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
