frutas = ["Maça", "Banana", "Laranja"]
print("Lista de frutas", frutas)

frutas.append("Uva")
print("Lista de frutas atualizada:", frutas)

print("Primeira fruta:", frutas[0])
var1 = (input("Deseja remover ou adicinar alguma fruta?"))


pessoa = {"nome": "Brenda", "idade": 26, "filhos": {"nome": "Catarina", "Idade": 6}}

print (pessoa)

print(pessoa["nome"])

print(pessoa["filhos"])

pessoaB = pessoa["filhos"]
print(pessoaB["nome"])

del pessoa["filhos"]
print(pessoa)

#set é um metodo que dfine conjntos e não deixa numeros repetidos

lista = [1, 2, 3, 4, 4]
comjunto =set(lista)
print(comjunto)

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)#interseção
print(a | b)#União
print(a - b)#Diferença


conjunto = {1, 2, 3, 4, 5,}
print(3 in conjunto)#true
print(6 in conjunto)#false

