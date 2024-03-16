# faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

# num_1 = int(input("Insira um número: "))
# num_2 = int(input("Insira outro número: "))
# resultado = num_1 // num_2
# print(resultado)


#Ex. Escreva um programa que calcule a área de um círculo, recebeno o raio como entrada

# raio = float(input("Insira o raio: "))
# area = 3.14*raio**2
# print(area)

#Crie um programa que peça ao usuario para digitar uma data no formato dd/mm/aaaa e, em seguida, imprima o dia, mês e o ano separadamente

data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_dia_mes_ano = data_usuario.split("/")
print(f"O elemento 1 é o: {lista_dia_mes_ano[0]}")
print(f"O elemento 2 é o: {lista_dia_mes_ano[1]}")
print(f"O elemento 3 é o: {lista_dia_mes_ano[2]}")