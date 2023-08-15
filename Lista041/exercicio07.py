"""
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo
"""

n1 = int(input("Escolha um número:"))

if(n1 < 0 ):
    neg = n1 * 1
    print(f"O módulo {n1} é {neg}")

else:
    print(f"O módulo do {n1} é ele mesmo")