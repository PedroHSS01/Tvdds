produto = "Cadeira Infantil"
preco = 12.40
Quantidade = 3

def preco_total(preco, Quantidade):
    return preco * Quantidade

total = preco_total( 12.40, 3)
print(f'{Quantidade} x {produto} Total: R$ {total:.2f}')