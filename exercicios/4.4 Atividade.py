import os

os.system("cls|| clear")

nomeProduto = input("Digite o Nome do Produto: ")
precoProduto = float(input("Digite um valor: "))
quantidadeProduto = int(input("Digite o valor do Produto: "))

if quantidadeProduto <= 5:
    desconto = 0.02
elif quantidadeProduto <= 10:
    desconto = 0.03
else:
    desconto = 0.05

subTotal = precoProduto * quantidadeProduto
totalPagar = subTotal - (subTotal * desconto)

print("\n=== Exibindo Resultados===")
print(f"Nome do Produto: {nomeProduto}")
print(f"Preço do Produto: {precoProduto}")
print(f"Quantidade do Produto: {quantidadeProduto}")
print(f"Total a Pagar: {totalPagar}")

print("\n==FIM==")