al = {"ryan":2, "Galvao":3, "Rafael":10,}
verificaaluno=input("qual aluno voce quer?")
if verificaaluno in al:
    if verificaaluno == "Rafael":
        print(f"a sua nota é {al['Rafael']}")
    if verificaaluno == "Galvao":
        print(f"a sua nota é {al['Galvao']}")
    if verificaaluno == "ryan":
        print(f"a sua nota é {al['ryan']}")