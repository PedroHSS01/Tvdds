"""
Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""

import datetime

def tempo_vivido(ano_nascimento, horas_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365

ano_nascimento = int(input("Qual o ano que você nasceu? "))
idade_em_dias = tempo_vivido(ano_nascimento)

print(f'A idade em dias é aproximdamente: {idade_em_dias} dias')