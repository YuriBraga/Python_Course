# ex036 - 045

nome = str(input('Qual é o o seu nome? '))

if nome == 'Yuri':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('Seu nome é Bíblico.')
elif nome in 'Ana':
    print('Nome feminino muito bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

# Condições aninhadas! Começa com if, quantos elif vc quiser e depois termina com else.
