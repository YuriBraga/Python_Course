# ANSI code
print('\033[1;34;40mOlá, Mundo!\033[m')
print('\033[1;30;47mOlá, Mundo!\033[m')

# Isso é um dicionário
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7; 30m'}

a = 3
b = 5
s = a + b
print('A soma de {} e {} é {}{}{}.'.format(a, b, cores['amarelo'], s, cores['limpa']))


# Style
# 0 - none,
# 1 - bold,
# 4 - underline,
# 7 - negative

# Text 30, 31, 32, 33, 34, 35, 36, 37
# Back 40, 41, 42, 43, 44, 45, 46, 47
# Text and Back has the same pattern: white, red, green, yellow, blue, purple, light blue, grey
