"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
"""
import requests

def usuario_aleatorio():
    try:
        url = 'https://randomuser.me/api/'

        resposta= requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()['results'][0]
        nome = f'{dados['name']['first']} {dados['name']['last']}'
        email = dados['email']
        pais = dados['location']['country']
        return f"""
            nome: {nome}
            email:{email}
            pais: {pais}
        """
    except requests.RequestException as e:
        print(f'Erro ao obter usuário: {e}')
        return None
    
usuario = usuario_aleatorio()
print(usuario)