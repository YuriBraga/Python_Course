# Cadastrar n pessoas até o cliente não querer cadastrar mais
# no final mostrar o num de pessoas com mais de 18
# num total de homens cadastrados e qtd de mulheres com menos de 20 anos
tot18 = totH = totM20 = tot = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    tot += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {tot18}
Total de pessoas: {tot}
Total de Homens: {totH}
Total de Mulheres < 20 anos: {totM20}''')
