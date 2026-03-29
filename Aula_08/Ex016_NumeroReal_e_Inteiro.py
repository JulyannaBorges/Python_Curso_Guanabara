#crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira.
#Ex: digite um numero: 6.127 tem a parte inteira 6
import math
n = float(input('Digite um numero: '))
n2 = math.trunc(n)
print(f'O numero digitado foi {n2}')
