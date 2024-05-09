import os

os.system("cls|| clear")

QUANTIDADE_NOTAS = 2

nota = 0
soma = 0
media = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = int(input(f"Digite uma {i+1}ª nota: \n"))

        if nota < 0 or nota > 10:
            print("Nota invalida. Por favor, tente novamente. \n")

        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS
print(f"Média: {media}")