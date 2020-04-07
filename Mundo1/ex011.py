l = float(input('Largura da parede (em metros):'))
h = float(input('Altura da parede (em metros):'))
# Para cada 2m² de parede, precisa de 1L de tinta para ser pintado.
print('Sua parede te dimensão {}x{}m tem {:.2f}m²'.format(l, h, l*h))
print('Para pintar a parede de {:.2f}m² serão necessários {:.2f}L de tinta.'.format(l*h, (l*h)/2))
