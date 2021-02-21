ano = int(input('Em que ano quer comsultar? '))
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
 print(' Esse ano é bissexto {}'.format(ano))
else:
    print('Ano Nao bissexto!'.format(ano))


