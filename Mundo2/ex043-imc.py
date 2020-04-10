# Cálculo de IMC (fórmula:  imc = peso/(altura**2))

peso = float(input('Seu peso em kilogramas: '))
altura = float(input('Sua altura em metros: '))
imc = peso/(altura**2)

print('Seu imc é {:.1f} e você está '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('no Peso ideal.')
elif 25 <= imc < 30:
    print('com Sobrepeso.')
elif 30 <= imc < 40:
    print('Obeso.')
else:
    print('com Obesidade Mórbida.')

# Não leva em consideração muita coisa o cálculo do IMC, há muitas falhas. Feito de acordo com o Ministério da Saúde.
