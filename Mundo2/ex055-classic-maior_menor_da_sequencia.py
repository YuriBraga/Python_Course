# Ler peso de 5 pessoas e ler o mais pesado e o mais leve
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}kg.'.format(maior))
print('O menor peso lido foi de {:.1f}kg.'.format(menor))

# tem pessoas que fazem gambiarra colocando menor = 9999999... muito zuado, faz direito!
