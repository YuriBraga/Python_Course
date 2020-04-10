# Melhoramento do ex061 adicionando quantos termos o cliente quiser
print('Gerador de PA')
print('-=-'*5)
primeiro = int(input('1° termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais  # Vai valer 10 no início, pois são os primeiros 10 termos
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'PA finalizada com {total} termos exibidos.')
