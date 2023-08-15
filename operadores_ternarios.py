"""
Cire um programa que pergunte a idade do usuário
e em seguida informe se este usuário é menor ou maior de idade
"""

idade = int(input("Informe a sua idade: "))

# logica do op ternário: var = ( se for falrso, se for verdadeiro)( teste_condicional )
resposta = ("Você é menor de idade", "Você é maior de idade")[idade>=18]

print(resposta)