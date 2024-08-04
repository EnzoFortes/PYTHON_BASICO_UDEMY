# CALCULADORA COM WHILE






# if primeiro_numero_int or segundo_numero_int:
#     ...
# else:
#     print("Vôce não digitou um número.")


while True:
    num_1 = input("Digite um número: ")
    num_2  = input("Digite outro número: ")
    print("As operações são: Divisão = /  Multiplicação = * Adição = + Subtração = - ") 
    operador = input("Escolha uma operação:")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try: 
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True

    except:
        numeros_validos = None 

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos")
        continue

    operadores_permitidos = "+-/*"


    if operador not in operadores_permitidos:
         print("Operador inválido")
         continue
    
    if len(operador) > 1:
         print("Digite apenas um operador")
         continue
    
    print("Realizando sua conta. Confira o resultado abaixo:")

    if operador == "+":
        print(num_1_float + num_2_float)

    elif operador == "-":
        print(num_1_float - num_2_float)
        
    elif operador == "*":
        print(num_1_float * num_2_float)

    elif operador == "/":
        print(num_1_float / num_2_float)
        
    else:
        print("Não deve chegar aqui")



    sair = input("Quer sair? [s]im: ").lower().startswith("s") # lower converte todos os caracteres digitados que podem ser minusculos ou maiusculos, em minusculos.     
                                                               # startswith verifica se o texto digitado inicia com o caracter definido.
    
    if sair:
        break

