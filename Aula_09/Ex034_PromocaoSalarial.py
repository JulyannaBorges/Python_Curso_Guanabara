#escreva um programa que peça o salário e ajuste para um aumento.
#Para salários maiores a 1.250, aumente 10%
#para inferiores ou iguais, aumente 15%
print ('='*38)
titulo = 'Promoção!'
print (titulo.center(38))
print ('='*38)
salario = float(input('Digite seu salário: '))
nv1 = salario + (salario*10/100)
nv2 = salario + (salario*15/100)
if salario > 1250:
    print (f'Você recebeu um aumento de 10%. Seu novo salário é: {nv1}')
else:
    print (f'Você recebeu um aumento de 15%. Seu novo salário é: {nv2}')