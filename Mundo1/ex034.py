sal = float(input('Qual o salário do funcionário?'))
if sal <= 1250:
    print('O salário com aumento será de R${:.2f}'.format(sal*1.15))
else:
    print('O salário com aumento será de R${:.2f}'.format(sal*1.1))
print('Muito bom trabalho! Você merece!!!')
