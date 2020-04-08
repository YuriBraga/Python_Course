fras = str(input('Digite um frase:')).strip().upper()
print('A letra A aparece {} vezes.'.format(fras.count('A')))
print('A letra A aparece pela primeira vez em {}'.format(fras.find('A')+1))
print('A letra A aparece pela última vez em {}'.format(fras.rfind('A')+1))
