m = float(input('Uma Distância em metros:'))
print('{}m vale {:.2f}cm e {:.2f}mm.'
      '\n{}km, {}nm e {}hm.'.format(m, m * 100, m * 1000, m / 1000, m / (10 ** 9), m / 100))
