"""
 Criar um código que registre as notas de alunos e calcular a média da turma.
"""

notas = []

print("Registro de média da turma")

while True:
    nota = float(input("Digite uma nota ou -1 para calcular a média da sala: "))
    if nota == -1:
        break
    notas.append(nota)
    
def media_turma(notas):
    soma = sum(notas)
    qtidade = len(notas)
    media  = soma / qtidade
    return media
media = media_turma(notas)

print(media)