print("=== VERIFICADOR DE NÚMEROS PARES E ÍMPARES ===")
print("Digite números inteiros (ou 'sair' para encerrar)")

pares = impares = 0 

while True:
    entrada = input("Digite um número inteiro: ").strip().lower()
    
    if entrada == 'sair':
        break
    
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"->> {numero} é PAR")
            pares += 1
        else:
            print(f"->> {numero} é ÍMPAR")
            impares += 1
            
    except ValueError:
        print(f"Erro: '{entrada}' não é um número inteiro válido!")
print("RESULTADO FINAL:")
print(f"Total de números pares: {pares} e Total de números ímpares: {impares}")