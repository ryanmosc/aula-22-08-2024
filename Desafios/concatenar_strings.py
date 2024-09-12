#Desafio 1
nome=input("Qual é o seu nome?")
snome=input("Qual é o seu sobrenome?")
print("Seja bem vindo",nome,snome)
#Desafio 2
palavra=input("Insira uma palavra")
numero=int(input("Insira um numero"))
vezes = palavra * numero
print(vezes)
#Desafio 3
nome=input("digite seu nome: ")
sobrenome = nome.split()

ultnome = (len(sobrenome))

if ultnome>= 1:
    print(sobrenome[-1])
else:
    print("coloque todo o nome")
#exercicio 5
tupla=(20, 30, 40)
print(tupla)

addtupla=35
tupla=(tupla[0], addtupla, tupla[1])
print(tupla)
#Exercicio 6
livro = {"Titulo": "Os monstros não falam", "Autor": "Rafael", "Data": 1945}
print(livro)
nd = int(input("Qual a nova data?"))
novadata = {"Titulo": "Os monstros não falam", "Autor": "Rafael", "Data": nd}
print(novadata)

