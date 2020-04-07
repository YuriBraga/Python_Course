n = int(input('Digite um número inteiro para ver sua tabuada:'))
print('='*12)
print('{} x 01 = {}\n'
      '{} x 02 = {}\n'
      '{} x 03 = {}\n'
      '{} x 04 = {}\n'
      '{} x 05 = {}\n'
      '{} x 06 = {}\n'
      '{} x 07 = {}\n'
      '{} x 08 = {}\n'
      '{} x 09 = {}\n'
      '{} x 10 = {}\n'
      ''.format(n, n, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
print('='*12)
# Ao invés de 01, 02, 03... poderia também colocar os valores fixos da tabuada como {:2}.
# Indicando que em todos há dois dígitos.
