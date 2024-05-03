import os

os.system("cls|| clear")

print("\n==Exibindo dados===")

numero = int(input("Digite um numero entre 1 e 20: "))

for i in range(1, 20):
    if numero % 2 == 0:
        print("numero é par: ")

else:
    print("esse numero é impar: ")
