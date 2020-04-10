# Ler o sexo de uma pessoa, caso o cliente tenha digitado algo diferente de M ou F pedir digitação novamente.

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, informe o sexo novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
