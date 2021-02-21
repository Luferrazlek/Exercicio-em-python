'''from random import randint
velocidade = randint(80, 124)
km = float(input('Quantos km rodados?'))
km =  (km * 7.00)
if velocidade >= 80:
 print('Você ultrapassou o limite de velocidade acima permitido, pagara a multa de {}reais'.format(velocidade,km))
else:
    print('velocidade permitida!')'''

velocida = float(input('Digite a velocidade do carro?'))
if velocida > 80:
    print('MULTADO!execedeu o limite permitido de 80km/h')
    multa = (velocida-80) * 7
    print('pagara uma multa equivalente a R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança! ')












