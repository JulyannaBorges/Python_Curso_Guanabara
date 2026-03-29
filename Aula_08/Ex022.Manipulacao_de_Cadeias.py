#crie um programa que leia o nome completo de uma pessoa e mostre:
#1: o nome em letras maiúsculas
#2: o nome em letras minúsculas
#3: quantas letras tem ao todo sem considerar os espaços
#4: quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ')
print('O nome em maiúsculo é:', nome.upper())
print('O nome em minúsculo é:',nome.lower())
print('O tamanho do nome é:',len(nome.split())) #conta o tamanho da lista
print ('Quantos caracteres tem?', (len(nome)))
print('Quantos caracteres sem espaço tem?', len(nome.replace(" ", "")))
print('O primeiro nome é:',nome.split()[0]) #primeiro nome
print('Quantidade de letras:', len(nome.split()[0]))