#mostre um número e diga se ele é par ou ímpar
print ('='*28)
titulo = 'Par ou Impar'
print (titulo.center(28))
print ('='*28)
import random
numero = random.randint(0, 999999)
if numero % 2 == 0:
    print (f'Numero escolhido: {numero}. Esse número é par!')
else:
    print (f'Numero escolhido: {numero}. Esse número é impar!')