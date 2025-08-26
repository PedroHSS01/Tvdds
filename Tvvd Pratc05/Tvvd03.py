"""
Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

def calculo_desconto(valor_produto, porcentagem_desconto):
    desconto = valor_produto * (porcentagem_desconto / 100)
    valor_final = valor_produto - desconto
    return round(valor_final ,2)

total_conta = float(input("Digite o valor da compra: "))
porcentagem_desconto = float(input("Qual porcentagem (%) do desconto? "))

valor_desconto = calculo_desconto(total_conta, porcentagem_desconto)
print(f"o valor do produto final é: R$ {valor_desconto}")