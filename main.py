#Aula de Try,Except,else,Finally

# try:
#     resultado = len("Luciano")
#     print(resultado)
# except TypeError as e:
#     print(e) #Imprime o erro
# else:
#     print("Deu tudo certo") #No caso do try, quando dá certo, ele printa o else
# finally:
#     print("O importante é participar") #Printa independente da resposta


# Casos com if:
# numero = int(input("Insira um numero: "))
# if isinstance(numero, int):
#     print("a variavel é inteiro") #Imprime o erro
# else:
#     print("a variavel não é um inteiro") #No caso do try, quando dá certo, ele printa o else

idade = 18

if idade < 18:
    print("Não pode dirigir")
elif idade == 18:
    print("Pode tirar a carteira de motorista")
else:
    print("Pode dirigir")