#faça um programa que leia o nome completo d euma pessoa, mostrando ems eguida o primeiro e o último nome separadamente.
#ex: Ana maria de Souza
#ex: Ana
#ex: Souza
nome = input('Digite seu nome completo: ')
print('O primeiro nome é:',nome.split()[0])
print ('O último nome é:',nome.split()[-1])