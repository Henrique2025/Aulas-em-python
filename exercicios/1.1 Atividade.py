import os

os.system("cls|| clear")

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))

primeiroNota = float(input("Digite a Primeira Nota: "))
segundaNota = float(input("Digite uma Segunda Nota: "))
terceiraNota = float(input("Digite uma Terceira Nota: "))


media = (primeiroNota + segundaNota + terceiraNota)/3
 

print("\n===RESULTADO===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira Nota: {primeiroNota}")
print(f"Segunda Nota: {segundaNota}")
print(f"Terceira Nota: {terceiraNota}")
print(f"Media: {media}")

if media >= 7:
    print("Você está Aprovado.")
else:    
    print("Você está Reprovado.")