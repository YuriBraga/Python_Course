# Programa que calcule a soma entre todos os n°s ímpares, múltiplos de 3 no intervalo de 1 a 500
soma = 0  # Acumulador
cont = 0  # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        # print(c, end=' ')  -  Esse código imprimiria o laço de todos os valores solicitados
        cont += 1  # Contador de divisíveis por 3 ímpares
        soma += c  # Somatório de divisíveis por 3 ímpares
print('A soma de todos os {} ímpares divisíveis por 3, de 1 a 500 é {}'.format(cont, soma))
