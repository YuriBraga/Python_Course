# Seq de Fibonacci
print('-=-'*8)
print('Sequência de Fibonacci')
print('-=-'*8)
# 0, 0+1, 0+1, 1+1, 2+1, ..., n = (n-1) + (n-2)
n = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
cont = 3  # Começa no 3, pois o primeiro e segundo termos já foram mostrados
while cont <= n:
    # Fazer o t1, t2 e t3 andarem na sequência.
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2  # linha 16 e 17 que "andam" pela sequência
    t2 = t3
    cont += 1
print(' -> Fim')
