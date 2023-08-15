"""
 Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
"""

num1 = int(input("Escolha um número: "))

resultado = num1%2

if(resultado == 0):
    print("Seu número é par!")

else:
    print("Seu número é impar!")