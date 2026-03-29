#desenvolva um programa que leia 3 retas e diga se pode ou não formar um triângulo
R1 = float(input('Digite a primeira reta: '))
R2 = float(input('Digite a segunda reta: '))
R3 = float(input('Digite a terceira reta: '))
if R1 + R2 > R3 and R1 + R3 > R2 and R2 + R3 > R1:
    print('Essas retas PODEM formar um triângulo!')
else:
    print('Essas retas NÃO podem formar um triângulo.')