# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
N1 = int(input('Digite a primeira nota: '))
N2 = int(input('Digite a segunda nota: '))
Media = (N1+N2) / 2
media = min(Media, 10)
print (f'A média do aluno é {Media}')
if Media >= 7:
    print ('O aluno foi aprovado!')
else:
    print ('O aluno foi reprovado.')

