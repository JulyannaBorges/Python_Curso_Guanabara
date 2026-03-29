#faça um programa que leia um número inteiro qualquer e mostre  na tela a sua tabuada
N = int(input("Digite um número para ver a tabuada: "))
for cont in range(1, 11):
    print(f'{N} x {cont} = {N * cont}')
#range: comece em 1 e vá até 10.
#for cont in range: Para cada número dentro dessa sequência, guarde esse número na variável cont.
#print(f'{N} x {cont} = {N * cont}')
#{N} → valor da variável
#x → apenas caractere que você escreveu
#{cont} → valor do contador
#{N * cont} → cálculo
#F: Puxa o valor da variável