velo = float(input('Qual a velocidade do carro?'))
if velo > 80:
    print('Você foi multado, excedeu o limite permitido que é de 80km/h')
    multa = (velo - 80)*7
    print('Sua multa é de R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
