p = float(input('Qual o preço do produto? R$'))
print('O produto que custava R${}, somente hoje está com desconto de 5%, '
      'o novo preço é de R${:.2f}.'.format(p, p*0.95))

# Porcentagem é ok, se tem desconto de x%, o novo valor com o desconto é
# 'valor*(100%-x%)'.
