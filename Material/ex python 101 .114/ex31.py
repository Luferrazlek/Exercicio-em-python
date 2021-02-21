dis = float(input('Qual a distancia pecorrida:?'))
print('Voce está prestes a começar uma viagem de {}km'.format(dis))
if dis <=200:
  preço = dis * 0.50
else:
  preço =dis * 0.45
print('O valor da corrida é de R${:.2f}'.format(preço))









