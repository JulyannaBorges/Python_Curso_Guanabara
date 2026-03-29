nome = str(input('Qual é o seu nome? '))
if nome == 'Julyanna':
    print ('Que nome lindo você tem! ')
else:
    print (f'Bom dia!{nome}')

#exemplo 2
n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua nota:'))
m = (n1 + n2) / 2
print (f'A sua média foi {m:.1f}')
if m >= 7.0:
    print ('Sua média foi boa! Parabéns!! ')
else:
    print ('A sua média foi ruim... Estude mais! ')


