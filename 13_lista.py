"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = [] # Definindo a lista.

while True:
    print("Selecione uma opção:")
    opcao = input("[i]nserir [a]pagar [l]istar: ") # Definindo menu de opções.
    opcao.lower # Filtrando para que sempre venha com a letra minuscula.

    if opcao == "i": # Criando a opção "i" de iserir e o input para capitar o valor a ser adicionado.
        os.system("cls") # Apenas para limpar o terminar. dependendo do terminal usado pode ser "clear"
        valor = input("Qual valor gostaria de adicionar?: ") 
        lista.append(valor) # Adicionando o valor a lista.
    
    elif opcao == "a": # Definindo a opção "a" e o input.
        indice_str = input("Qual valor gostaria de apagar?: ")
      

        try: # Usando o try except para previnir erros na filtragem e caso o usúario digite algo diferente do índice ou que não esteja no range.
            indice_int = int(indice_str)
            del lista[indice_int]  

        except ValueError:
            print("Por favor, digite apenas números inteiros")
        except IndexError:
            print("Esse valor não existe na lista")
            
    elif opcao == "l": # Criando a opção "l" para listar o itens.
        os.system("cls")
        if len(lista) == 0: # Checando a quantidade de itens na lista e se ela for igual a zero...
            print("Nada para listar")

        for i, valor in enumerate(lista): # Listando.
            print(i, valor)


    else: 
        print("Digite apenas 'i', 'a' ou 'l'")
    

