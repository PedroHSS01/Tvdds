"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
"""
print('Verificador de senhas')
print('A senha deve ter no minimo 8 caracteres e 1 numero')


while True:
    senha = input('Digite uma senha: ')

    numeros = False
    for caractere in senha:
        if caractere in '0123456789':
            numeros = True

    if len(senha) >= 8 and numeros:
        print('Senha válida!')
        break
    else:
        print('Senha inválida')