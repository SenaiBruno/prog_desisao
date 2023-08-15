"""
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações
"""

num1 = float(input("Escolha um número: "))

num2 = num1 / 2

if( num1 > 20 ):
    print(f"Esse é seu número, {num1} e, essa é a metade dele: {num2:}")

else:
    print("Seu número é maior ou igual a 20.")