# analisar o ano de nascimento de 7 pessoas e mostrar quantas atingiram a maioridade e quantas não.

from datetime import date
hj = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    p = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = hj - p
    if idade >= 21:
        totmaior += 1
    elif idade < 21:  # or else:
        totmenor += 1
print('''Ao todo, {} pessoas são maiores de idade e {}, menores de idade.'''.format(totmaior, totmenor))
