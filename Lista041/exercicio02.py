"""
 Desenvolver um programa que permita ao aluno responder qual a capital do Brasil. O programa deverá exibir se
a resposta está certa ou errada.
"""

resp = input("Qual a capital do Brasil? (A letra inicial deverá ser em maiuscula, lembrando da acentuação gráfica): ")
cap = "Brasília"
if(resp == cap ):
    print("Sua resposta está certa!")

else:
    print("Sua resposta está errada! A resposta certa é Brasília ")