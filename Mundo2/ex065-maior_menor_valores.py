# ler varios nums. mostrar a media no final, mostrar maior e menor, perguntar se quer continuar
resp = 'S'
soma = qtd = med = maior = menor = 0
while resp in 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    qtd += 1
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
med = soma/qtd
print(f'Você digitou {qtd} números e a média foi {med:.1f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
