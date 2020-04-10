# Conversor de bases numéricas de decimal para octal, hexadecimal ou binário

print('\033[1;30;47mConversor de bases numéricas!\033[m')

num = int(input('Digite um número inteiro: '))
print('''Selecione a transformação desejada: 
[ 1 ] Converter para binário
[ 2 ] Converter para octal
[ 3 ] Converter para hexadecimal''')
opt = int(input('Sua opção: '))


if opt == 1:
    print('{} em binário é igual a {}'.format(num, bin(num)[2:]))
elif opt == 2:
    print('{} em octal é igual a {}'.format(num, oct(num)[2:]))
elif opt == 3:
    print('{} em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Escolha uma opção válida!')
