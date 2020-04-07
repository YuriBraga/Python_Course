sal = float(input('Qual o salário do funcionário? R$'))
print('O funcionário que ganhava R${}, com 15% de aumento, '
      'passa a receber R${:.2f}.'.format(sal, sal*1.15))

# Para redução de um valor, 'valor*(100%-x%)'
# Para aumento de um valor, 'valor*(100%+x%)'
