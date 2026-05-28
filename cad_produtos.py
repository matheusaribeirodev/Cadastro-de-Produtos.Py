import os
produtos = []
opcao = 0

while opcao != "5":
    print("\n--- SISTEMA DE GESTÃO DE PRODUTOS ---")
    print("1 - Adicionar Produto")
    print("2 - Listar Produtos")
    print("3 - Alterar Produto")
    print("4 - Remover Produto")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        codigo = input("Codigo: ")
        preco = input("Preço: ")
        quantidade = input("Quantidade: ")
        produtos.append({
            "nome": nome, 
            "codigo": codigo, 
            "preço": preco, 
            "quantidade": quantidade
        })
        print(f"Produto {nome} adicionado com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE PRODUTOS ---")
        if not produtos:
            print("A lista está vazia.")
        else:
            for i, u in enumerate(produtos):
                print(f"ID: {i} | Nome: {u['nome']} | Codigo: {u['codigo']} | Preço: {u['preço']} | Qtd: {u['quantidade']}")

    elif opcao == "3":
        if not produtos:
            print("Não há produtos para alterar.")
        else:
            for i, u in enumerate(produtos):
                print(f"ID: {i} | Nome: {u['nome']} | Codigo: {u['codigo']}")
            
            try:
                indice = int(input("\nDigite o ID do produto para alterar: "))

                p = produtos[indice]
                
                print(f"Editando: {p['nome']}")
                novo_nome = input(f"Novo nome [{p['nome']}]: ") or p['nome']
                novo_codigo = input(f"Novo codigo [{p['codigo']}]: ") or p['codigo']
                novo_preco = input(f"Novo preço [{p['preço']}]: ") or p['preço']
                novo_qtd = input(f"Nova quantidade [{p['quantidade']}]: ") or p['quantidade']
                
                produtos[indice] = {
                    "nome": novo_nome,
                    "codigo": novo_codigo,
                    "preço": novo_preco,
                    "quantidade": novo_qtd,
                }
                print("Dados atualizados!")
            except (ValueError, IndexError):
                print("Erro: ID inválido!")

    elif opcao == "4":
        if not produtos:
            print("Lista vazia.")
        else:
            for i, u in enumerate(produtos):
                print(f"ID: {i} | Nome: {u['nome']} | Codigo: {u['codigo']}")
            try:
                indice = int(input("\nID para remover: "))
                removido = produtos.pop(indice)
                print(f"Produto {removido['nome']} removido!")
            except (ValueError, IndexError):
                print("Erro: ID inválido!")

    elif opcao == "5":
        print("Saindo do sistema...")
    
    else:
        print("Opção inválida!")