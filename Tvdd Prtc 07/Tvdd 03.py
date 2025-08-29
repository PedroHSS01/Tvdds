"""
Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade."""
import csv
def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitura = csv.reader(arquivo_csv)
            for linha in leitura:
                print(linha)
    except FileNotFoundError:
        return(f'Arquivo ñ encintrado')
    
nome_arquivo = input('Qual o nome do arquvi? ')
print(ler_arquivo(nome_arquivo))