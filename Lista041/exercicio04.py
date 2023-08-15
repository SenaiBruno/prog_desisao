"""
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”
"""

num1 = int(input("Escolha um número"))

div4 = num1 % 4
div5 = num1 % 5

if(div4 == 0 and div5 == 0):
    print("Seu número divido é dividido por 4 e por 5 ")

else:
    print("Seu número não é divisivel por 4 e por 5 ao mesmo tempo")