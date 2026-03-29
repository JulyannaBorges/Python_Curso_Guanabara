#desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200km e R$0.45 para viagens mais longas
print ('='*38)
titulo = 'Planejador de Custos'
print (titulo.center(38))
print ('='*38)
viagem = float(input('Qual a distância da sua viagem? '))
preco_viagem1 = viagem * 0.5
preco_viagem2 = viagem * 0.45
if viagem <= 200:
    print ('O preço da passagem é: R$ {:.2f}'.format(preco_viagem1))
else:
    print ('O preço da passagem é: R$ {:.2f}'.format(preco_viagem2))
print ('='*38)
titulo_final = 'Boa viagem!'
print (titulo_final.center(38))
print ('='*38)