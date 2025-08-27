"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o
 código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da 
 última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""

import requests

def cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()[f'{moeda}BRL']
        return f"""
                Cotação de {moeda} para BRL: 
                Valor: R$ {float(dados['bid']):.2f}
                Valor Máximo: R$ {float(dados['high']):.2f}
                Valor Minimo: R$ {float(dados['low']):.2f}
                Data/hora: {dados['create_date']}
                """
    except requests.RequestException as e:
        return f'Erro ao obter cotação: {e}'
    
moeda = input('Digite o código da moeda (EUR, USD ou BRL): ')
resposta = cotacao(moeda)
print(resposta)