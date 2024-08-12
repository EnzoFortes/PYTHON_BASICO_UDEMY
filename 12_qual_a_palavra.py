"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Importanto biblioteca.
import os

# Definindo váriaveis.
palavra_secreta = "perfume"
letras_acertadas = ""
tentativas = 0

# Inicio do código
while True:
    letra_digitada = input("Digite uma letra: ") # Pedindo para o user digitar uma letra.

    tentativas += 1 # Contador de tentativas

    if len(letra_digitada) > 1:  # Assegurando que o user digite apenas uma letra por vez.
        print("Digite apenas uma letra")
        continue

    if letra_digitada in palavra_secreta:  # Checando se a letra digitada pelo user está na palavra secreta e adicionando á váriavel de letras acertadas.
        letras_acertadas += letra_digitada
    
    palavra_digitada = "" # definindo a váriavel para fins de comparação com a palavra secreta

    for letra_secreta in palavra_secreta:  # Para que seja mostrado ao user quais letras ele já acertou ou qual falta acertar.
        if letra_secreta in letras_acertadas:
            palavra_digitada += letra_secreta
        else:
            palavra_digitada += "*"
    print(palavra_digitada)
    
    if palavra_digitada == palavra_secreta: # Finalizando e zerando o programa para um novo ínicio.
        os.system("cls")
        print("Você ganhou, Párabens!")
        print("A palavra secreta era", palavra_secreta)
        print("tentativas:",tentativas)
        letras_acertadas = ""
        tentativas = 0

