import os

os.system("cls|| clear")

nome = str(input("Digite seu nome: "))
idade = float(input("Digite sua Idade: " ))
print("Digite seu nome: ")
print("Digite sua iade: ")


print("\n===Resultado===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")


if idade <= 18:
    print("Não é obrigado a Votar.")

elif idade >= 65:
    print("Não é obrigado a votar.")

else:
    print("Voto Obrigatorio.")





