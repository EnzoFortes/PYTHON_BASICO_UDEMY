"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual  = input("Digite o horário atual: ")
if hora_atual.isdigit():
    hora_int = int(hora_atual)
    
    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia!")
    elif hora_int >= 12 and hora_int <= 17:
        print("Boa tarde!")
    elif hora_int >= 18 and hora_int <= 23:
        print("Boa noite!")
    else:
        print("Não conheço essa hora.")

else:
    print("Vôce não digitou um horário, digite apenas números inteiros.")
