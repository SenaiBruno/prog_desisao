"""
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
"""
num1 = int(input("Escolha um número inteiro: "))

if(num1 <= 10 and num1 >= 1):
    print("Seu valor está entre 1 e 10")

else:
    print("Seu valor não está entre 1 e 10:")