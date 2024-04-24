import os

os.system("cls|| clear")

print("=== Solicitando dados ===\n")
primeiroNumero = int(input("Digite um primeiro numero: "))
segundoNumero= int(input("Digite um segundo Número: "))

print("\n")

soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero

print("===Exibindo Resultados=== \n")
print(f"Primeiro número:  {primeiroNumero}")
print(f"Segundo Número: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

