"""
Cire um programa que pergunte a idade do usuário
e em seguida informe se este usuário é menor ou maior de idade
"""

idade = int(input("Informe a sua idade: "))

#logica do op ternario2
# var = resultado_verdadeiro if teste_condicional else resultado_falso

resposta = "Você é maio de idade" if idade >= 18 else "Você é menor de idade"

print(resposta)