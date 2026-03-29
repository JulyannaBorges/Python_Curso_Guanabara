#faça um algoritmo que guarde o preço fornecido pelo usuário e dê uma porcentagem de 5%
p = float(input('Digite o valor do produto:'))
v = (p*5/100)
vf = p - v
print (f'O valor final é {vf:.2f}')