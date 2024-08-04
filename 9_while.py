
#       012345678910
nome = input("Digite seu nome:")
#     -1110987654321
tamanho_nome = len(nome)

# print(nome)
# print(tamanho_nome)
# print(nome [3])
indice  = 0     
nome_print  = ""

while indice < tamanho_nome:
    letra = nome[indice]
    nome_print += f"*{letra}"
    indice += 1
    
nome_print += "*"
print(nome_print)