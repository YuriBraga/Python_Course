nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome)-nome.count(' ')))
'''print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))'''
# Encontrar o primeiro espaço é saber quantas letras tem o 1° nome.

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
