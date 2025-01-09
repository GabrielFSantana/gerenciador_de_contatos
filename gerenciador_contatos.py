import os
import json

# Caminho do arquivo de contatos
ARQUIVO_CONTATOS = "contatos.json"

# Função para carregar contatos do arquivo
def carregar_contatos():
    if not os.path.exists(ARQUIVO_CONTATOS):
        return {}
    with open(ARQUIVO_CONTATOS, "r") as arquivo:
        return json.load(arquivo)

# Função para salvar contatos no arquivo
def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w") as arquivo:
        json.dump(contatos, arquivo, indent=4)

# Função para adicionar um contato
def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    if nome in contatos:
        print("Contato já existe!")
        return
    contatos[nome] = {"telefone": telefone, "email": email}
    salvar_contatos(contatos)
    print("Contato adicionado com sucesso!")

# Função para listar todos os contatos
def listar_contatos():
    contatos = carregar_contatos()
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    for nome, dados in contatos.items():
        print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}")

# Função para buscar contatos pelo nome parcial
def buscar_contatos_por_nome(nome_parcial):
    contatos = carregar_contatos()
    resultados = {nome: dados for nome, dados in contatos.items() if nome_parcial.lower() in nome.lower()}
    
    if resultados:
        print("\nContatos encontrados:")
        for nome, dados in resultados.items():
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}")
    else:
        print("Nenhum contato encontrado com esse nome.")

# Função para deletar um contato
def deletar_contato(nome):
    contatos = carregar_contatos()
    if nome in contatos:
        del contatos[nome]
        salvar_contatos(contatos)
        print("Contato deletado com sucesso!")
    else:
        print("Contato não encontrado.")

# Menu principal
def menu():
    while True:
        print("\n=== Gerenciador de Contatos ===")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato (Parcial)")
        print("4. Deletar Contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            adicionar_contato(nome, telefone, email)
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            nome_parcial = input("Digite parte do nome que deseja buscar: ")
            buscar_contatos_por_nome(nome_parcial)
        elif opcao == "4":
            nome = input("Digite o nome do contato que deseja deletar: ")
            deletar_contato(nome)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()
