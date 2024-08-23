numero = input("Entrada de N: ")

def verificaEntrada(numero):
    if int(numero) > 0:
        return "Número maior que 0"
    else:
        return "Número menor ou igual a 0"

mensagem = verificaEntrada(numero)
print(mensagem)
