def soma(valor1, valor2):
    return valor1 + valor2

def mult(valor1, valor2):
    return valor1 * valor2  

def divi(valor1, valor2):
    if valor2 == 0:
        return "Erro: Divisão por zero!"
    return valor1 / valor2  

def exibir_opcoes():
    print("Escolha a operação desejada:")
    print("+ : Soma")
    print("* : Multiplicação")
    print("/ : Divisão")

def main():
    # Lista de operações
    operacoes = [soma, mult, divi]
    simbolos = ["+", "*", "/"]

    valor1 = float(input("Qual o primeiro valor? "))
    valor2 = float(input("Qual o segundo valor? "))

    exibir_opcoes()
    
    op = input("Digite o símbolo da operação: ")

    if op in simbolos:
        index = simbolos.index(op)
        resultado = operacoes[index](valor1, valor2)
        print(f"O resultado é: {resultado}")
    else:
        print("Operação inválida!")

if __name__ == "__main__":
    main()
