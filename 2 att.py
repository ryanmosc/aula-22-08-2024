pessoa = {"nome": "Brenda", "idade": 26, "filhos": {"nome": "Catarina", "Idade": 6}}

print (pessoa)

print(pessoa["nome"])

print(pessoa["filhos"])

pessoaB = pessoa["filhos"]
print(pessoaB["nome"])

del pessoa["filhos"]
print(pessoa)

