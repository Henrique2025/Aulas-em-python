import os
os.system("cls || clear")

QUANTIDADES_NOTAS = 6

numero = 0
numeros = []

for i in range(QUANTIDADES_NOTAS):
    numero = float(input("Digite uma numero: "))
    numero.append(numero)

    maiorNumero = max(numeros)
    menorNumero = min(numeros)

for i, numero in enumerate(numeros):
    print(f"{i+i}ª número: {numero}")

    print(f"==Resultado==")
    print(f"Maior Numero: {maiorNumero}")
    print(f"Menor Numero: {menorNumero}")