'''
 Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

resto = num1 % num2

if(resto==0):
    print("O segundo número inserido é um divisor do primeiro número!")

else:
    print("O segundo número não é um divisor do primeiro número!")