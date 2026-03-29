frase = 'curso em vídeo python'
print(frase)
#formas de fatiamento
print(frase[9:13]) #conta do caractere 9 até 13 (letras)
print(frase[:13]) #conta desde o início até o fim estabelecido
print(frase[1:15:2]) #conta do 1 ao 15 no intervalo de 2
print(frase[1:]) #conta do inicio estabelecido até o final
print(frase[9::3]) #conta do 9 até o final no intervalo de 3 em 3

#dica
print('''Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Enean commodo ligula eget dolor. 
Enéias massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. 
Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut,''')
#para escrever um texto longo, basta abrir as '' 3x

#formas de análise
print (len(frase)) #qual o comprimento da frase?
print (frase.count('o')) #quantos 'o' tem na frase?
print(frase.count('o',0,13)) #conta quantos 'o' tem no período de 0 e 13
print (frase.find('o')) #encontra o 'o'
print ('curso' in frase) #true ou false

#transformações
print (frase.replace('curso','aula'.title()))
print (frase.upper())
print (frase.lower())
print (frase.capitalize())
print (frase.title())
print (frase.strip())
print (frase.rstrip())
print (frase.lstrip())

#Divisor
print (frase.split())

#junção
print ('-'.join(frase.split()))
