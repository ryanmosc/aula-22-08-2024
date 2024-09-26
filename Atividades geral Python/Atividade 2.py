def divisao():
    try:
        num1 = float(input("Qual seu primeiro número? "))
        num2 = float(input("Qual o segundo número? "))
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("Divisão por número 0 não é aceita.")
    except ValueError:
        print("Por favor, insira números válidos.")
resultado = divisao()
if resultado is not None:
    print(f"O resultado da divisão é: {resultado}")
