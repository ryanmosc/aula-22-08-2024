#Desafio 3
nome=input("digite seu nome: ")
sobrenome = nome.split()

ultnome = (len(sobrenome))

if ultnome>= 1:
    print(sobrenome[-1])
else:
    print("coloque todo o nome")