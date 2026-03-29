#faça um programa que leia o ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano: '))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
if bissexto:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto.')
# % → resto da divisão
# bissexto → segue regra dos 4, 100 e 400
# usa if com and e or

#Um ano bissexto é:
#É divisível por 4
#E NÃO é divisível por 100
#OU é divisível por 400