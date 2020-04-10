# Alistamento Militar (Está na hora? Já passou? Quando você deve se alistar?)

from datetime import date
atual = date.today().year

print('\033[1;32;40m  ALISTAMENTO MILITAR  \033[m')
sexo = input('Seu sexo é masculino ou feminino? Digite \033[1mm\033[m para masculino'
             'e \033[1mf\033[m para feminino: ')
if sexo == 'm':
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc

    print('Quem nasce em {} tem/terá {} anos em {}.'.format(nasc, idade, atual))

    if idade == 18:
        print('Está na hora de você se alistar! É agora em 2020.')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda falta(m) {} ano(s) para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Como você é mulher, não precisar participar do Alistamento Militar Obrigatório.')
