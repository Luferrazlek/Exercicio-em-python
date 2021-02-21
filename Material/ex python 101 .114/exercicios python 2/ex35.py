r1 = float(input('Digite o 1º Segmento do triângulo: '))
r2 = float(input('Digite o 2º Segmento do triângulo: '))
r3 = float(input('Digite o 3º Segmento do triângulo: '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima Não podem formar triangulo!')
else:
    print('Os segmentos acima podem formar triangulo')


