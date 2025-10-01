from datetime import datetime

# Sistema de Controle de Estoque de Remédios
# ODS 3 – Saúde e Bem-Estar

# Lista de dicionários para armazenar os remédios
remedios = [
    {"nome": "Paracetamol", "quantidade": 10, "validade": "21/07/2026"},
    {"nome": "Ibuprofeno", "quantidade": 5, "validade": "15/08/2025"},
    {"nome": "Insulina", "quantidade": 2, "validade": "01/09/2025"},
]

print("\n ============ Controle de Estoque de médicamento ============\n")

# Função para converter string para data
def str_para_data(data_str):
    return datetime.strptime(data_str, "%d/%m/%Y")

# Função para cadastrar remédio
def cadastrar_remedio(nome, quantidade, validade):
    validade_dt = str_para_data(validade)
    data = datetime.today()
    if validade_dt < data:
        print("Erro: não é possível cadastrar remédio com validade passada!")
        return

    for i in remedios:
        if i["nome"].lower() == nome.lower():
            # Verifica se o remédio existente ainda não venceu
            if str_para_data(i["validade"]) < data:
                print(f"Não é possível adicionar {nome}, pois a versão existente já está vencida!")
                return
            i["quantidade"] += quantidade
            print(f"{quantidade} unidades de {nome} adicionadas.")
            return

    remedios.append({"nome": nome, "quantidade": quantidade, "validade": validade})
    print(f"{nome} cadastrado com {quantidade} unidades.")

# Função para retirar remédio do estoque
def retirar_remedio(nome, quantidade):
    data = datetime.today()
    for i in remedios:
        if i["nome"].lower() == nome.lower():
            validade_dt = str_para_data(i["validade"])
            if validade_dt < data:
                print(f"Não é possível retirar {nome}, remédio vencido! Use a opção de excluir.")
                return
            if i["quantidade"] >= quantidade:
                i["quantidade"] -= quantidade
                print(f"{quantidade} unidades de {nome} retiradas.")
            else:
                print(f"Estoque insuficiente de {nome}.")
            return
    print("Remédio não encontrado.")

# Função para excluir remédio vencido
def excluir_vencido(nome):
    data = datetime.today()
    for i in remedios:
        if i["nome"].lower() == nome.lower():
            validade_dt = str_para_data(i["validade"])
            if validade_dt >= data:
                print(f"{nome} ainda não está vencido, não pode ser excluído!")
                return
            remedios.remove(i)
            print(f"{nome} vencido foi excluído do estoque.")
            return
    print("Remédio não encontrado.")

# Função para exibir o estoque
def mostrar_estoque():
    data = datetime.today()
    print("\n Estoque de Remédios:")
    for i in remedios:
        validade_dt = str_para_data(i["validade"])
        status = " Estoque baixo!" if i["quantidade"] < 3 else "OK"
        validade_status = " Vencido!" if validade_dt < data else "Válido"
        print(f"{i['nome']} - Quantidade: {i['quantidade']} - Validade: {i['validade']} ({validade_status}) - {status}")
    print()

# Loop interativo do sistema
while True:
    print(" 1 - Mostrar estoque\n 2 - Cadastrar remédio\n 3 - Retirar remédio\n 4 - Excluir remédio vencido\n 5 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        validade = input("Validade (dd/mm/aaaa): ")
        cadastrar_remedio(nome, quantidade, validade)
    elif opcao == "3":
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        retirar_remedio(nome, quantidade)
    elif opcao == "4":
        nome = input("Nome: ")
        excluir_vencido(nome)
    elif opcao == "5":
        print("Saindo... ")
        break
    else:
        print("Opção inválida! Tente novamente.")
