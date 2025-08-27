"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado. 
"""
import requests

def consulta(cep):
    url= f'https://viacep.com.br/ws/{cep}/json'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if 'erro' in dados:
            return "CEP não encontrado"
        
        return f"""
                    CEP: {dados['cep']}
                    Logradouro: {dados ['logradouro']}
                    Bairro: {dados['bairro']}
                    Cidade: {dados['localidade']}
                    Estado: {dados['estado']}
                """
    except requests.RequestException as e:
        print(f'Erro ao obter usuário: {e}')


cep = input('Digite um CEP para consuta: ')
resultados= consulta(cep)
print(resultados)