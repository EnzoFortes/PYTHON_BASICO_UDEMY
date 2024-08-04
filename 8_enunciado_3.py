"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = input("Digite seu primeiro nome:")
first_str = first_name.isdigit()

name_number = len(first_name)

if first_str is False:
    if name_number <= 4:
        print("Seu nome é curto")
    elif name_number >= 5 and name_number <= 6:
        print("Seu nome é normal")
    elif name_number > 6:
        print("Seu nome é muito grande")    
else:
    print("Você não digitou um nome")