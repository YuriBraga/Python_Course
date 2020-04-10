# Programa lê 6 números inteiros e mostre a soma dos pares. Se for impar, desconsiderar.
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('{}° valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} número(s) par(es) e a soma deles é {}'.format(cont, soma))
