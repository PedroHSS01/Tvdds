"""
< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

peso = float(input('Qual seu peso em Kg exemplo (79))? '))
altura = float(input('Qual sua altura em metros exemplo (1.77) ? '))

imc = peso/(altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")