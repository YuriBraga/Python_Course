# Se quiser uma contagem de 6: 0 a 6 ou 1 a 7 ou 2 a 8, pois conta do 0 ao 5 e no 6 para
for c in range(1, 7):
    print(c)
print('FIM')
print('-=-'*10)

# -1 serve para contar ao contrário
for c in range(6, 0, -1):
    print(c)
print('FIM')
print('-=-'*10)

# O terceiro valor resulta é o salto ou manipulação do laço
for c in range(-10, 11, 2):
    print(c)
print('-=-'*10)

# Digitar um número e dar uma sequência de números
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('-=-'*10)

# Você escolhe uma sequência de números
i = int(input('Início: '))
f = int(input('Final: '))
s = int(input('Salto: '))
for c in range(i, f+1, s):
    print(c)
print('-=-'*10)

# Somatório e inputs
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n  # Mesma coisa que s = s + n
print('O somatório dos números é {}'.format(s))
