dist = float(input('Qual a distância da viagem em km?'))
print('Você está prestes a começar uma viagem de {:.2f}km.'.format(dist))
if dist <= 200:
    print('A viagem custará R${:.2f}'.format(dist*.05))
else:
    print('A viagem custará R${:.2f}'.format(dist*0.45))
print('Faça uma excelente viagem. A Braga Airlines agradece sua preferência!')
