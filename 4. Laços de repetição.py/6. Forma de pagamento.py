import os 

os.system("cls||clear")

#Solicita a forma de pagamento

valor_produto = float(input("Informe o valor do produto R$: ")) 

print("Escolha a forma de pagamento: ")
print("Pagamento Avista - Digite 1")
print("Pagamento Parcelado - Digite 2") 
forma_pagamento = int(input("Digite a opção (1 ou 2): "))

if forma_pagamento == 1:
    # Pagamento Avista
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    print("\nForma de pagamento: á vista")
    print(f"Valor do produto: R$ {valor_produto:.2f}")
    print(f"Valor do desconto: R$ {desconto: .2f}")
    print(f"Total a pagar: R$ {valor_final: .2f}")

elif forma_pagamento == 2:
    #Pagamento a prazo
    parcelas = int(input("Digite a quantidade de parcelas: "))
    valor_parcela = valor_produto / parcelas
    print("\nForma de pagamento: a prazo")
    print(f"Valor do produto: R$ {valor_produto: .2f}")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcelas: R$ {valor_parcela: .2f}")
    print(f"Total a prazo: R$ {valor_produto: .2f}")

else:
    print("opção invalida. por favor, escolha 1 ou 2.")