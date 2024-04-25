import os

os.system("cls|| clear")

primeiroValor= (input("Digite o Primeiro Valor: "))
segundoValor = float(input("Digite o Segundo valor: "))


soma = primeiroValor + segundoValor
media = soma /2
produto = primeiroValor * segundoValor

if primeiroValor > segundoValor:
   maiorNumero = primeiroValor 
else:
   menorValor = segundoValor

if primeiroValor < segundoValor:
   maiorNumero = segundoValor
else:
   maiorValor = primeiroValor


   print("\n===Resultado===")
   print(f"Primeiro Valor: {primeiroValor}")
   print(f"Segundo Valor: {segundoValor}")
   print(f"Soma: {soma}")
   print(f"Media: {media}")
   print(f"Produto: {produto}")
   print(f"Maior Numero: {maiorNumero}")
   print(f"Menor Numero: {menorNumero}")
   

