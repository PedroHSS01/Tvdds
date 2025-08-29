"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""
import json

def ler_json(arquivo):
    try:
        with open(arquivo, 'r', newline='', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            print(dados_json)
    except FileNotFoundError:
        return(f'Arquivo ñ encintrado')
    
def escrever_json(arquivo, dados):
    try:
        with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f'Salvo em: {arquivo}')
    except Exception as e:
        return(f'Erro ao salvar: {e}')

dados= {
    "nome": "Silva",
    "idade": 18,
    "cidade": "são miguel do norte"
}

nome_arquivo = input('Qual o nome do arquivo: ')
escrever_json(nome_arquivo, dados)
ler_json(nome_arquivo)
