def manipularstring(texto):
    textoMaiusculo = texto.upper()
    textoMinusculo = texto.lower()
    totaisCaracteres = len(texto)
    
    return (textoMaiusculo, textoMinusculo, totaisCaracteres )

def main():
    palavra = input("Diite uma string para ser manipulada: ")
    
    resultadoMaiusculo, resultadoMinusculo, resultadototaisCaracteres = manipularString(palavra)
    
    print(f"Sua palavra em maiusculo: {resultadoMaiusculo}")
    print(f"Sua palavra em maiusculo: {resultadoMinusculo}")
    print(f"Totais de caracteres de sua palavra: {resultadototaisCaracteres}")
main()
