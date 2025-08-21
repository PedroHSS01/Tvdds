"""
* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
"""


produto = "Camiseta"
Preco = 50.00
desconto = 20

Valor_desconto = Preco * (desconto / 100)
Preco_final = Preco - Valor_desconto

print(f'O produto: {produto}, custa: {Preco} desconto será: {desconto}%, portanto o produto saira por {Preco_final}')