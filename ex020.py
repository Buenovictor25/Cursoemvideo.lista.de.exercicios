import random

n1 = input('Digite o nome do aluno(a):')
n2 = input('Digite o nome do aluno(a):')
n3 = input('Digite o nome do aluno(a):')
n4 = input('Digite o nome do aluno(a):')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de alunos para realizar a apresentaçao sera !')
print(lista)



