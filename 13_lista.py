"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print("Selecione uma opção:")
    opcao = input("[i]nserir [a]pagar [l]istar: ")
    opcao.lower

    if opcao == "i":
        os.system("cls")
        valor = input("Qual valor gostaria de adicionar?: ")
        lista.append(valor)
    
    elif opcao == "a":
        indice_str = input("Qual valor gostaria de apagar?: ")
      

        try:
            indice_int = int(indice_str)
            del lista[indice_int]  

        except ValueError:
            print("Por favor, digite apenas números inteiros")
        except IndexError:
            print("Esse valor não existe na lista")
            
    elif opcao == "l":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para listar")

        for i, valor in enumerate(lista):
            print(i, valor)


    else: 
        print("Digite apenas 'i', 'a' ou 'l'")
    

