"""
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
"""

num1 = int(input("Escolha um número: "))

if(num1 > 1):
    print("Seu número é positivo")

if(num1 == 0 ):
    print("Seu número é nulo")

if(num1 < 0 ):
    print("Seu número é negativo")