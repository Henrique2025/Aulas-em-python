import os

os.system("cls|| clear")

# Inicializando variavel.
resultado = False
while True:
    os.system("cls|| clear")

    #Solicitar dados do usuario.

    operador = input('Digite uma opção: ')
    
    match(operador):
        case '1':
            resultado = 'Segunda'
            break
        case '2':
            resultado = 'Terça'
            break
        case '3':
            resultado = 'Quarta'
            break
        case '4':
            resultado = 'Quinta'
            break
        case '5':
            resultado = 'Sexta'
            break
        case '6':
            resultado = 'Sabado'
            break
        case'7':
            resultado = "Domingo"
            break
        case _:
            input("Dia invalido")
if resultado :
        print(f"Resultado: {resultado}")
