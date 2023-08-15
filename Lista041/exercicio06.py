"""
Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
"""

num1 = int(input("Escolha um número:"))
num2 = int(input("Escolha outro número:"))

maior = num1
menor = num1

if(num1 < num2 ):
    num2 = maior
    if(num1 > num2):
        num2 = menor
