import os 

os.system("cls|| clear")

QUANTIDADE_NOTAS = 2
soma = 0
nota = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota (entre 0 e 10): "))

        if nota < 0 or nota > 10:
            print("Nota invalida. Por favor, tente novamente. \n")

        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Media: {media}")
print(f"Situação do aluno: {resultado}")