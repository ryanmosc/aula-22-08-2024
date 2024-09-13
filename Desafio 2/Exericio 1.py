def calcular_celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 1.8) + 32

def calcular_fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9
def main():
    temperatura = float(input("Insira a temperatura: "))
    unidade = input("Digite 'C' para converter Celsius para Fahrenheit ou 'F' para converter Fahrenheit para Celsius: ").strip().upper()

    if unidade == 'C':
        resultado = calcular_celsius_para_fahrenheit(temperatura)
        print(f"{temperatura}°C é igual a {resultado:.2f}°F")
    elif unidade == 'F':
        resultado = calcular_fahrenheit_para_celsius(temperatura)
        print(f"{temperatura}°F é igual a {resultado:.2f}°C")
    else:
        print("Unidade inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")
main()
