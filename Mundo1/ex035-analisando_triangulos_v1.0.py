print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
# Para formar um triângulo, cada segmento deve ser menor que a soma dos outros dois segmentos
s1 = float(input('1° segmento:'))
s2 = float(input('2° segmento:'))
s3 = float(input('3° segmento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos formam um triângulo!')
else:
    print('Os segmentos não podem formar triângulo.')
