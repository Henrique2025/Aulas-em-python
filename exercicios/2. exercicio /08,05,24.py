import os 

os.system("cls|| clear")

nota = 0
media = 0

primeiraNota = int(input("Digite uma Nota: "))
segundaNota = int(input("Digite uma segunda nota: "))
terceiraNota = int(input("Digite uma terceira nota: "))

media = (primeiraNota + segundaNota + terceiraNota) /3

print("\n=== Resultado ===")
print(f"Primeira Nota: {primeiraNota}")
print(f"Segunda Nota: {segundaNota}")
print(f"Terceira Nota: {terceiraNota}")
print(f"Media: {media}")

if media >= 7:
    print("Você foi Aprovado!!")

elif media >= 4: 
    print("Você está em recuperação!!")

else: 
     print("Reprovado!!")