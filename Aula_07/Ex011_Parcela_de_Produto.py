P1 = float(input('Digite o preço do produto:'))
PG = input('Qual será a forma de pagamento?').lower()
if PG == 'a vista':
    print ('Recebe valor de 15%')
    VF1 = P1 * 0.85
    print(f'O valor final é de {VF1:.2f}')
else:
    if PG == 'parcelado' :
        print ('Acréscimo de valor de 20%')
        parcela = int(input('Parcela em quantas vezes?'))
        VF2 = (P1 * 1.20/parcela)
        print (f'O valor de cada parcela é {VF2:.2f}')
