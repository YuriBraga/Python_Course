from random import choice
a1 = input('1° aluno:')
a2 = input('2° aluno:')
a3 = input('3° aluno:')
a4 = input('4° aluno:')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno sortudo foi {}'.format(escolhido))
