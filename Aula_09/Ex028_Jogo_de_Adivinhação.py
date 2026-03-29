#escreva um programa que faça o computador pensar em um número entre 0 a 5
#peça para o usuário tentar adivinhar qual numero o computador pensou
print ('='*38)
titulo = 'Bem Vindo(a) ao Jogo de Adivinhação!'
print (titulo.center(38))
print ('='*38)
print('Tente adivinhar o número que o computador está pensando (0 a 5)')
import random
numero = random.randint(0, 5)
chute = input('Digite seu chute: ')
if chute.isnumeric():
    chute = int(chute)
    if 0 <= chute <= 5:
        if chute == numero:
            print('Parabéns! Você acertou!')
        else:
            print(f'Você errou! O número era {numero}')
    else:
        print('Digite um número entre 0 e 5.')
else:
    print('Por favor, digite apenas números.')
