#faça um programa que leia um número de 0 a 9999 e mostre na tecla cada um dos dígitos separados
#ex: digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
numero = input('Digite um número de 0 a 9999: ')
print('Unidade:', numero[-1])
print('Dezena:', numero[-2] if len(numero) >= 2 else 0)
print('Centena:', numero[-3] if len(numero) >= 3 else 0)
print('Milhar:', numero[-4] if len(numero) >= 4 else 0)