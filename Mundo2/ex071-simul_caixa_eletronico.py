# Caixa eletrônico de saque. Informar quantas cédulas de cada valor serão entregues (apenas 50, 20, 10, 1)
print('='*30)
print('{:^30}'.format('BRAGA BANK'))
print('='*30)
# Fazer o programa pensar: ir retirando a maior quantidade possível do valor com a maior nota,
# quando chegar no limite, passa pra próxima cédula
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 100:  # Não consegui tirar 50 do valor então:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BRAGA BANK')
