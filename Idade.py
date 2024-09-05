#Inserir Idade 
idade = int(input("Qual sua idade?"))
categoria = "Indefinida"

#Classificador de idades
if idade < 13:
    categoria = "Criança"
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"
elif idade >= 18 and idade <50:
    categoria = "Adulto"
else:
   categoria = "Idoso"
 
 #Mostra sua idade
print (f"A pessoa é  classificada como:, {categoria}")