# PA - ler o primeiro termo e a razão; depois mostre os 10 primeiros termos dessa PA.
prm = int(input('1° termo da PA: '))
rz = int(input('Razão da PA: '))
dec = prm + (10 - 1) * rz  # Fórmula de PA!
for c in range(prm, dec + rz, rz):
    print('{}'.format(c), end=' -> ')
print('Acabou!')
