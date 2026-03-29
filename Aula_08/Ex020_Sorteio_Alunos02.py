#o mesmo professor do desafio, quer sortear a ordem de apresentação dos trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
Aluno1 = "Julyanna"
Aluno2 = "Julia"
Aluno3 = "Jonas"
Aluno4 = "Julio"
Sorteio = [Aluno1, Aluno2, Aluno3, Aluno4]
Escolhido = random.choice(Sorteio)
print(Escolhido)