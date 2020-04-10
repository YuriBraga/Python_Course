# Vamos comparar dois números

n1 = int(input('\033[1;30;47mDigite um número inteiro: \033[m'))
n2 = int(input('\033[1;30;47mDigite o segundo número inteiro: \033[m'))

if n1 == n2:
    print('Seja mais criativo. Escolha dois valores diferentes!')
elif n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
else:
    print('{} é menor que {}'.format(n1, n2))
