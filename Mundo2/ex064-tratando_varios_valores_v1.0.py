# Ler varios nums inteiros até o cliente digitar o flag (999)
# Mostrar quantos nums foram digitados e a soma deles desconsiderando o flag
n = s = contador = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:
    contador += 1
    s += n
    n = int(input('Digite um número inteiro [999 para parar]: '))
print(f'Acabou, você digitou {contador} números e a soma vale {s}')
