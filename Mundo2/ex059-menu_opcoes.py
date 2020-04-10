# Ler 2 valores e criar um menu (somar, multiplicar, maior, novos numeros, sair do programa)
from time import sleep
n1 = int(input('Primeiro valor inteiro: '))
n2 = int(input('Segundo valor inteiro: '))

opt = 0
while opt != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do programa''')
    opt = int(input('Sua opção: '))

    if opt == 1:
        s = n1 + n2
        print(f'{n1} + {n2} = {s}')
    elif opt == 2:
        p = n1 * n2
        print(f'{n1} x {n2} = {p}')
    elif opt == 3:
        if n1 > n2:
            maior = n1
            print(f'{maior} é o maior valor')
        elif n1 < n2:
            maior = n2
            print(f'{maior} é o maior valor')
        else:
            print('São iguais, não tem maior')
    elif opt == 4:
        print('Informe outros dois números')
        n1 = int(input('Primeiro valor inteiro: '))
        n2 = int(input('Segundo valor inteiro: '))
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-='*10)
    sleep(1.5)
print('Fim do Programa')
