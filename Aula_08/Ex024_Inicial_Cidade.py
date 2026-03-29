#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = input('Digite o nome de uma cidade: ')
if cidade.split()[0].upper() == 'SANTO':
    print('Essa cidade começa com "SANTO"')
else:
    print('Essa cidade não começa com "SANTO"')