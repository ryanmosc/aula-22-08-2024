numero = int(input("Enfia um numero"))

def verificaEntrada(numero):
    if numero > 0:
        return "Maior que 0"
    elif numero < 0:
        return "Menor que 0"
    else:
        return "Igual a 0"
verificaEntrada(numero)
print(verificaEntrada(numero))
    
    