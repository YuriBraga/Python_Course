# v2.0 add Equilátero (tds lados iguais) , Isósceles (dois lados iguais) e Escaleno (tds lados diferentes)
# v1.0 é o ex035
# Para formar um triângulo, cada segmento deve ser menor que a soma dos outros dois segmentos

print('-=-'*10)
print('\033[1;36mAnalista de Triângulos v2.0\033[m')
print('-=-'*10)

l1 = float(input('1° segmento: '))
l2 = float(input('2° segmento: '))
l3 = float(input('3° segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos formam um triângulo ', end='')
    if l1 == l2 == l3:
        print('Equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isósceles!')
    elif l1 != l2 != l3 != l1:
        print('Escaleno!')

else:
    print('Os segmentos não formam um triângulo.')
