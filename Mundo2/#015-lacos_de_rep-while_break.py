# Aula passada
'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

# Nessa aula:
# A verificação para dar break no loop infinito não entra na contagem.
n = s = 0
while True:
    n = int(input('Número:'))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')  # Uso de fstring: técnica de interpolação

'''e.g.:
nome = 'José'
idade = 33
sal = 2500
print(f'o {nome} tem {idade} anos e ganha R${sal:.2f}.')  # Python 3.6+
print('O %s tem %d anos e ganha R$%s.' % (nome, idade, sal))  # Python2'''
