"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""
import csv

def escrever(arquivo, dados):
    try:
        with open(arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escrita = csv.writer(arquivo_csv)
            escrita.writerow(['nome', 'idade', 'cidade'])
            for linha in dados:
                escrita.writerow(linha)
            return (f'Salvo em {arquivo}')
    except Exception as e:
        return(f'Erro ao salvar: {e}')

dados= [['Pedro', '26', 'são Paulo'],['Henrique', '62', 'Santa catarina'], ['Camila', '2', 'alagoas']]

nome_arquivo = input('Qual o nome do arquivo: ')
print(escrever(nome_arquivo, dados))