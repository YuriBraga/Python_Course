# Empréstimo bancário (prestação não pode exceder 30% do salário, se exceder será negado)

sal = float(input('Salário: R$'))
casa = float(input('Valor da casa: R$'))
anos = int(input('Quantos anos de financiamento?'))

presta = casa/(anos*12)

if presta <= .3*sal:
    print('Para pagar uma casa de R${:.2f} em {} anos, será necessária uma prestação mensal de R${:.2f};'
          ' portanto seu empréstimo foi CONCEDIDO.'.format(casa, anos, presta))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, será necessária uma prestação mensal de R${:.2f};'
          ' portanto seu empréstimo foi NEGADO.'.format(casa, anos, presta))
