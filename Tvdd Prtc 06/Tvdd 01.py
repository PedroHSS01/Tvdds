"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""

import random
import string

def senha(tamanho):
    caractere = string.ascii_letters + string.digits + "!@#$%&"
    senha =''.join(random.choice(caractere) for _ in range(tamanho))
    return senha 

tamanho_senha =int(input("Digite o tamanho da senha desejada: "))
senha_gerada = senha(tamanho_senha)
print(senha_gerada)