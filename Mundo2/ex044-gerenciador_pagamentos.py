print('\033[1;33m======= NOVA ALIANÇA STORE =======\033[m')
p = float(input('\033[1;30mValor da sua compra: R$\033[m'))
print('''Formas de pagamento:
[ 1 ] À vista no dinheiro (10% off)
[ 2 ] À vista no cartão (5% off)
[ 3 ] 2x sem juros
[ 4 ] 3x ou mais (com juros de 20%)''')

form = int(input('\033[1;30mSelecione a forma de pagamento desejada: \033[m'))

if form == 1:
    print('\033[1;33mTotal a ser pago R${:.2f}\033[m'.format(0.9*p))
elif form == 2:
    print('\033[1;33mTotal a ser pago R${:.2f}\033[m'.format(0.95*p))
elif form == 3:
    print('\033[1;33mValor da parcela é R${:.2f}\033[m'.format(p / 2))
elif form == 4:
    parc = int(input('\033[1;30mNúmero de parcelas (3 a 6): \033[m'))
    if parc == 3 or 4 or 5 or 6:
        ptax = 1.2*p
        print('''\033[1;33mEm {}x o valor da parcela será de R${:.2f}
        e o total será de R${:.2f}\033[m'''.format(parc, ptax/parc, ptax))

else:
    print('\033[1;31mSelecione uma opção válida.\033[m')
