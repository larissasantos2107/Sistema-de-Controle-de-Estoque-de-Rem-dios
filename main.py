# Sistema de Controle de Estoque de Remédios
# ODS 3 – Saúde e Bem-Estar
# Esse programa ajuda a controlar estoque de medicamentos:
# cadastrar novos, retirar quando usados e verificar validade/quantidade.

# Lista de dicionários para armazenar os remédios
remedios = [
    {"nome": "Paracetamol", "quantidade": 10, "validade": 2026},
    {"nome": "Ibuprofeno", "quantidade": 5, "validade": 2025},
    {"nome": "Insulina", "quantidade": 2, "validade": 2025},
]

# Função para cadastrar remédio
def cadastrar_remedio(nome, quantidade, validade):
    # Se já existir no estoque, só aumenta a quantidade
    for r in remedios:
        if r["nome"].lower() == nome.lower():
            r["quantidade"] += quantidade
            print(f"{quantidade} unidades de {nome} adicionadas.")
            return
    # Se não existir, adiciona como novo
    remedios.append({"nome": nome, "quantidade": quantidade, "validade": validade})
    print(f"{nome} cadastrado com {quantidade} unidades.")

# Função para retirar remédio do estoque
def retirar_remedio(nome, quantidade):
    for r in remedios:
        if r["nome"].lower() == nome.lower():
            # Só retira se tiver quantidade suficiente
            if r["quantidade"] >= quantidade:
                r["quantidade"] -= quantidade
                print(f"{quantidade} unidades de {nome} retiradas.")
            else:
                print(f"Estoque insuficiente de {nome}.")
            return
    print("Remédio não encontrado.")

# Função para exibir o estoque
def mostrar_estoque():
    print("\n Estoque de Remédios:")
    for r in remedios:
        # Alerta se quantidade baixa
        status = " Estoque baixo!" if r["quantidade"] < 3 else "OK"
        # Alerta se perto do vencimento
        validade_status = " Perto do vencimento!" if r["validade"] <= 2025 else "Válido"
        print(f"{r['nome']} - Quantidade: {r['quantidade']} - Validade: {r['validade']} ({validade_status}) - {status}")
    print()

# Loop interativo do sistema
while True:
    print(" 1 - Mostrar estoque\n 2 - Cadastrar remédio\n 3 - Retirar remédio\n 4 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        validade = int(input("Validade (ano): "))
        cadastrar_remedio(nome, quantidade, validade)
    elif opcao == "3":
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        retirar_remedio(nome, quantidade)
    elif opcao == "4":
        print("Saindo... ")
        break
    else:
        print("Opção inválida! Tente novamente.")
