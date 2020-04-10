'''palíndromo é uma frase que pode ser lida normal ou de trás pra frente e o sentido será o mesmo:
apos a sopa, a torre da derrota, a sacada da casa, etc
detectar se a frase é um palíndromo'''

frase = str(input('Digite uma frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
# print(junto, inverso) - feito para ver se o código até aqui está correto
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')

# pode ser feito sem o 'for' usando fatiamento:

frase = str(input('Digite uma frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')
