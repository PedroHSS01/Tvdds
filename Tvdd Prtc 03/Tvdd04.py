"""
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
"""

ano = int(input("Qual ano desejá saber se é bissexto ou não? "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'{ano} é bissexto')
        else:
            print(f'{ano} não é bissexto')
    else:
        print(f'{ano} é bissexto') 
else:
    print(f"{ano} não é bissexto")