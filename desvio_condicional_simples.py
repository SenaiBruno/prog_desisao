"""
Crie um programa que pergunte dois número ao usuário.
Em seguida o programa deverá somar os dois números e apresentar o resultado se o valor for maior que 10.
"""
num1 = int(input("Informe um número:"))
num2 = int(input("Informe outro número:"))

soma = num1 + num2

if( soma > 10 ):
    print("Soma dos valores: ", soma)

else:
    print("A soma dos valores é menor ou igual à 10.")