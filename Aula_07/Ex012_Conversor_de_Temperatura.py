C = float(input('Digite a temperatura em Celsius: '))
Conversor = (C * 1.8) + 32
print (f'A temperatura de {C}°C corresponde a {Conversor:.2f}°F')
#pode ser colocado 9/5 para conversão ou 1.8. Isso acontece porque 0°C e 0.35°F, onde C=100 e F=180. 100/180= 1.8
#1.8 em fração é 18/10
# simplificando, fica 9/5. Por isso 1.8 ou 9/5 == tem o mesmo valor
