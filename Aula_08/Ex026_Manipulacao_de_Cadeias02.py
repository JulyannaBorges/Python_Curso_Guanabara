#faça um programa que peça uma frase ao usuário e mostre:
#quantas vezes aparece a letra 'A'
#em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase = input('Digite uma frase: ').lower()
print('Quantidade de "a":', frase.count('a'))
print('Primeira posição:', frase.find('a') + 1)
print('Última posição:', frase.rfind('a') + 1)