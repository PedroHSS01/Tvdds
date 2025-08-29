"""
Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. 
"""

import pandas as pd
def logs_treinamento(arquivo):
    try:
        leitor = pd.read_csv(arquivo)
        media_tempo = leitor['tempo_execucao'].mean()
        desvio= leitor['tempo_execucao'].std()
        return f"""
                Tempo médio de execução: {media_tempo}
                Desvio padrão do tempo de execução: {desvio:.2f}
                """
    except FileNotFoundError:
        return "Arquivo não encontrado"
    
nome_arquivo = input("Digite o nome do arquivo csv: ")

print(logs_treinamento(nome_arquivo))