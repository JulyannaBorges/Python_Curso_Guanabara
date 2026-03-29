#escreva quanto dinheiro uma pessoa tem na carteira e quantos doláres ela consegue comprar
carteira = int(input('Quanto dinheiro você tem na carteira? '))
d = float(input('Quantos dolares quer comprar? '))
cotacao = 5.20
dolares = carteira / cotacao
print(f'Você pode comprar {dolares:.2f} dólares')
#{dolares:.2f}: é uma formatação de número decimal.
#: iniciar formatação
# 2= limite de duas casas decimais
# F: Float
#carteira = int(input('Quanto de dinheiro você tem na carteira? '))
#cotacao = 5.20
#dolares = carteira/cotacao
#print (f'voce pode comprar {dolares:.2f} dolares')


