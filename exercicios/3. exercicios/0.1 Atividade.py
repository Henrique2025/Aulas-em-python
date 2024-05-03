import os

os.system("cls|| clear")

pesoMorangos = int(input('Digite o peso Dos Morangos (em Kg): '))
pesoMacas = int(input('Digite o peso das Maçãs (em kg):'))

if pesoMorangos < 5:
    precoMorangos =2.50
else:
    precoMorango = 2.20

if pesoMacas < 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

pesoTotal = pesoMorangos + pesoMacas
subTotal = (precoMorango * pesoMorangos) + (precoMaca * pesoMacas)

if pesoTotal > 8 or subTotal > 25:
        desconto = subTotal * 0.10

else:
     desconto = 0

     totalPagar = subTotal - desconto

print("\n=== Exibindo resultados ===")
print(f"Peso de morangos (em kg):  {pesoMorangos} ")
print(f"Peso de maçãs (em kg): {pesoMacas}")
print(f"Soma dos pesos (em kg): {pesoTotal}")
print(f"Subtotal: R$ {subTotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {totalPagar:.2f}")