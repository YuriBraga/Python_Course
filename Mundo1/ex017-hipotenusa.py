'''from math import sqrt
catop = float(input('Comprimento do cateto oposto:'))
catad = float(input('Comprimento do cateto adjacente:'))
hip = sqrt(catop**2+catad**2)
print('A hipotenusa medirá {:.2f}'.format(hip))'''

import math
x = float(input('Cat Op:'))
y = float(input('Cat Adj:'))
print('A Hipotenusa vale {:.2f}'.format(math.hypot(x, y)))
