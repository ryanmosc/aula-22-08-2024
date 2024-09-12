with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
        
 ##########################################
    
    
with open("exemplo2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá Mundo!\n")
    arquivo.write("OIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
 
 #Metodo de acrescentar

with open("exemplo2.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nTexto AdicionalS")


