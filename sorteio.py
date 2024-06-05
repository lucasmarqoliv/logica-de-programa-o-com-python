import random
aluno_01 = (input('digite o nome do primeiro aluno: '))
aluno_02 = (input('digite o nome do segundo aluno: '))
aluno_03 = (input('digite o nome do terceiro aluno: '))
aluno_04 = (input('digite o nome do quarto aluno: '))
alunos = [aluno_01, aluno_02, aluno_03, aluno_04]
aluno_sorteado = random.choice(alunos)
print (aluno_sorteado)