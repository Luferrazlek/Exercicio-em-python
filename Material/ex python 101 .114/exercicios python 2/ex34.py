sal = float(input('Digite o valor atual do salário R$: '))
print('Analisando sálario.....!')
if sal <= 1250:
   reajuste = sal + (sal * 15/100)
else:
   reajuste = sal + (sal * 10/100)
print('O sálario atual é de {:.2f} com reajuste sera de {:.2f}'.format(sal,reajuste))
