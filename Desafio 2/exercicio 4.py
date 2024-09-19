
contatos = []

def adicionar_contato(nome, telefone):
    contato = {"nome": nome, "telefone": telefone}
    contatos.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso!")

def verificar_quantidade_contatos():
    quantidade = len(contatos)
    print(f"Você tem {quantidade} contato(s) na sua lista.")

def main():
    adicionar_contato("Alice", "123-456-789")
    adicionar_contato("Bob", "987-654-321")

    verificar_quantidade_contatos()

main()
