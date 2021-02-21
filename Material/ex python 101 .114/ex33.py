anum1 = int(input('Digite 1° valor: '))
bnum2 = int(input('Digite 2° valor: '))
cnum3 = int(input('Digite 3° valor: '))
#verificando quem é menor
menor = anum1
if bnum2 < anum1 and bnum2 < cnum3:
    menor = bnum2
if cnum3 < anum1 and cnum3 < bnum2:
        menor = cnum3
#verificando quem é maior
maior = anum1
if bnum2 > anum1 and bnum2 > cnum3:
    maior = bnum2
if cnum3 > anum1 and cnum3 > bnum2:
        maior = cnum3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))





