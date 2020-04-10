'''Ler nome, idade e sexo de 4 pessoas.
Mostrar média de idade do grupo, nome do homem mais velho e quantas mulheres tem menos de 20 anos'''
somaidade = 0
medidade = 0

maioridadehomem = 0
nomevelho = ''

totmulher20 = 0

for p in range(1, 5):
    print('==== {}ª Pessoa ===='.format(p))
    nome = str(input('Seu nome: ')).strip().upper()
    idade = int(input('Sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade

    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'F' and idade < 20:
        totmulher20 += 1

medidade = somaidade/4
print('A média das idades é {}'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo, {} mulher(es) tem menos de 20 anos'.format(totmulher20))
