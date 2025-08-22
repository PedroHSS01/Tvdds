"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin
"""
temperatura = float(input("Qual a temperatura? "))
origem = input('Digite a unidade de origem (C, F, K): ').upper()
destino = input('Digite a unidade de destino (C, F, K): ').upper()

if origem == destino:
    resultado = temperatura
    print(f"{temperatura} {origem} = {resultado} {destino}")

elif origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura}°C = {resultado}°F")
    elif destino == "K":
        resultado = temperatura + 273.15
        print(f"{temperatura}°C = {resultado}K")

elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura}°F = {resultado}°C")
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
        print(f"{temperatura}°F = {resultado}K")

elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
        print(f"{temperatura}K = {resultado}°C")
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
        print(f"{temperatura}K = {resultado}°F")