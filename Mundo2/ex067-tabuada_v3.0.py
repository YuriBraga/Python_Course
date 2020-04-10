# v3.0 da tabuada. O programa só é interrompido quando o valor digitado for negativo
while True:
    n = int(input('Tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Programa tabuada v3.0 encerrado')
