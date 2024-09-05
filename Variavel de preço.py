#Variaveis de Preço
p1 = int(input("Coloque um numero"))
p2 = 200
p3 = 300

#Formula para somar 
numeros = [p1, p2, p3]
total = sum(numeros)

#Formula  fazer o desconto
desc = 0
if total > 500:
    desconto = total * 0.1

r = total - desconto
    
print("Total da compra", total)
print("Desconto aplicado", desconto)
print ("Total com desconto", r)