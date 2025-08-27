def calcular(a, b, operacao):
    ops = {'+': a+b, '-': a-b, '*': a*b, '/': a/b if b != 0 else None}
    return ops[operacao]

try:
    a = float(input("Primeiro número: "))
    operacao = input("Operação (+, -, *, /): ")
    b = float(input("Segundo número: "))
    
    if operacao not in {'+', '-', '*', '/'}:
        print("Operação inválida!")
    else:
        resultado = calcular(a, b, operacao)
        print(f"{a} {operacao} {b} = {resultado}" if resultado is not None else "Erro: Divisão por zero!")
        
except ValueError:
    print("Digite números válidos!")