#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escolhendo o nome do escolhido.
import random
N1 = str(input("Digite o nome do primeiro aluno: "))
N2 = str(input("Digite o nome do segundo aluno: "))
N3 = str(input("Digite o nome do terceiro aluno: "))
N4 = str(input("Digite o nome do quarto aluno: "))
Sorteio = [N1, N2, N3, N4]
escolhido = random.choice(Sorteio)
print(f"O aluno escolhido foi: {escolhido}")

