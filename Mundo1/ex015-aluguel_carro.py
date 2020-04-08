# Aluguel de carro

dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km rodados?'))

# Preço a pagar... R$60/dia e R$0.15/kmrodado
print('O preço a pagar pelo aluguel do carro é R${}'.format(60*dias + 0.15*km))
