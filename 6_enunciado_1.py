"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = input("Digite um número: ")

if numero_digitado.isdigit():
    numero_int = int(numero_digitado)
    par_ou_impar = numero_int % 2

    if par_ou_impar == 0:
        print("Seu número é par.")
    elif par_ou_impar != 0:
        print("Seu número é impar.")

else:
    print("Vôce não digitou um número inteiro")