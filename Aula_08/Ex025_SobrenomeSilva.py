#Crie um programa que pergunte o nome completo do usuário e diga se ele tem o sobrenome 'Silva' no nome
nome_completo = input('Digite seu nome completo: ')
if 'silva' in nome_completo.lower():
    print('Esse nome contém "SILVA"')
else:
    print('Esse nome não contém "SILVA"')