"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    invertido =''
    for letra in texto_limpo:
        invertido = letra + invertido

    if texto_limpo ==invertido:
        return True
    return False

palavra = input('Digite algum texto: ')
resultado = palindromo(palavra)
print(f'{palavra} é um palíndromo? {resultado}')