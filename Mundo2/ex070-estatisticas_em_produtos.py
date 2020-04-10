# Ler nome e preço de vários produtos, perguntar se quer continuar
# Mostrar depois: Total gasto na compra, Qts prod custaram mais de 1000 e qual o nome do prod mais barato
print('==='*10)
print('DELLinux Store'.center(30))
print('==='*10)
tot = tot1000 = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Produto: ')).strip().upper()
    valor = float(input('Preço R$'))
    cont += 1
    tot += valor
    if valor > 1000:
        tot1000 += 1
    '''if cont == 1:
        menor = valor
        barato = nome
    else:
        if valor < menor:
            menor = valor
            barato = nome'''
    # Pode ser otimizado, pois l16, l17 = l20, l21
    # O if inicial pode ser escrito como: if cont == 1 or valor < menor (l24 - l26):
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Mais algum produto? [S/N] ')).strip().upper()[0]
    if resp == 'N':  # Esse é o if do 'while True' lá do início
        break
print(f'''Valor total da compra: R${tot:.2f}
Quantidade de produtos que custam mais de R$1000.00: {tot1000}
Produto mais barato: {barato}, que custa R${menor:.2f}''')
