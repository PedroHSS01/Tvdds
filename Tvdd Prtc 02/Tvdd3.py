"""
* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
"""

Nota_1 = float(input('Digite sua nota: '))
Nota_2 = float(input('Digite sua nota: '))
Nota_3 = float(input('Digite sua nota: '))

media = (Nota_1 + Nota_2 + Nota_3) / 3

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = 'Reprovado'
print(f"As médias são: {Nota_1}, {Nota_2}, {Nota_3}, portanto você esta {situacao}")