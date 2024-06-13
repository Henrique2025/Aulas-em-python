import os
from dataclasses import dataclass

os.system("cls || clear")

#Constante
QUANTIDADES_ALUNOS = 2

# classe.
@dataclass
class Aluno:
    nome: str
    idade: int
alunos = []

#Solicitando dados para o usúario.
for i in range(QUANTIDADES_ALUNOS):
    aluno = Aluno(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: "))
    )
    alunos.append(aluno)

    #Exibindo dados para o usúario.
    for i in alunos:
        print(f"Nome: {i.nome}")
        print({f"Idade: {aluno.idade}"})