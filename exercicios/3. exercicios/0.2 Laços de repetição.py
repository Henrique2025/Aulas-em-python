import os

os.system("cls|| clear")

print("\n==Exibindo dados===")

numero = int(input("Digite um numero entre 100 e 121: "))

for i in range(100, 121):
    if numero % 2 == 0:
        print("numero é par")

else:
    print("esse numero é impar")
