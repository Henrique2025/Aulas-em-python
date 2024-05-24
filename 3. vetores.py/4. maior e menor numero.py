import os
os.system("clear")

notas = []
i = 0
maior_nota = 0
menor_nota = 0

for i in range(5):
    nota = float(input(f"Digite a {i + 1}º nota: "))
    notas.append(nota)

print("\n==Notas==")

for i in range(5):
    print(f"Nota: {notas[i]}")

# Maior e menor nota:
    maior_nota = max(notas)
    menor_nota = min(notas)

print("\n==Maiores e menores notas==")
print(f"Maior Nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")