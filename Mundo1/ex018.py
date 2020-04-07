'''import math
ang = float(input('Qual o ângulo?'))
print('Cosseno vale {}'.format(math.cos(math.radians(ang))))
print('Seno vale {}'.format(math.sin(math.radians(ang))))
print('Tangente vale {}'.format(math.tan(math.radians(ang))))'''

# ângulo está em radianos, tem que converter para radianos com math.radians()

from math import cos, sin, tan, radians
ang = float(input('Qual o ângulo?'))
print('Cosseno vale {:.2f}'.format(cos(radians(ang))))
print('Seno vale {:.2f}'.format(sin(radians(ang))))
print('Tangente vale {:.2f}'.format(tan(radians(ang))))
