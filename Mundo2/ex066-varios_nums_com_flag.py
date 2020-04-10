# ler vários nums inteiros. só para quando digitar 999. mostrar qts numeros foram digitados e qual foi a soma
n = s = contador = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
# O break deve ser antes da soma e da contagem para que não seja considerado o 999 na soma
    contador += 1
    s += n
print(f'{contador} números foram digitados e a soma resulta em {s}')
