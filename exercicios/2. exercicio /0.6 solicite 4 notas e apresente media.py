import os 

os.system("cls|| clear")

nota = 0
media = 0

primeiraNota = int(input("Digite uma Nota: "))
segundaNota = int(input("Digite uma segunda nota: "))
terceiraNota = int(input("Digite uma terceira nota: "))
quartaNota = int(input("Digite uma quarta nota: "))

media = (primeiraNota + segundaNota + terceiraNota + quartaNota) /4

print("\n=== Resultado ===")
print(f"Primeira Nota: {primeiraNota}")
print(f"Segunda Nota: {segundaNota}")
print(f"Terceira Nota: {terceiraNota}")
print(f"Quarta Nota: {quartaNota}")
print(f"Media: {media}")