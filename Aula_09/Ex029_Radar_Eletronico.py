#escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, multe-o
#a multa vai custar R$7,00 por cada Km acima do limite
print ('='*28)
titulo = 'Radar Eletrônico'
print (titulo.center(28))
print ('='*28)
import random
quilometragem = random.randint(20, 120)
print (f'O radar eletrônico registrou que o automóvel estava a {quilometragem} km/h!')
print ('O valor da multa é a quilometragem registrada, multiplicada por R$7.00.')
Calculo_Multa = quilometragem * 7
if quilometragem >= 80:
    print ('Você foi mutado! O valor da multa é: R$ {:.2f}'.format(Calculo_Multa))
else:
    print ('Você está dentro do limite de velocidade!')
