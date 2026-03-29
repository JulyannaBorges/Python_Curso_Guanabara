#Faça um programa que leia o comprimento do cateto opostoso e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
print("A hipotenusa é:", hipotenusa)
#cateto_oposto**2: **2 significa elevar ao quadrado.
#math.sqrt(): Calcula a raiz quadrada.