import depositodebebidas, menus
atendente = depositodebebidas.Atendente()
produto = depositodebebidas.Produto()
gerente = depositodebebidas.Gerente()
cliente = depositodebebidas.Cliente()
vendas = depositodebebidas.Vendas()

while True:
    opc_gerente = int(input(menus.menu_gerente))
    match opc_gerente:
        case 1:
            nome = input('Digite o nome do funcionário: ')
            cpf_funcionario = input('Digite o CPF do funcionário: ')
            matricula_funcionario = input('Digite a matrícula: ')
            senha_funcionario = input('Digite uma senha alfanumérica: ')
            cargo_funcionario = 'Atendente'
            salario_funcionario = 2100.54
            atendente.adiciona_funcionario(nome, cpf_funcionario, matricula_funcionario, senha_funcionario, cargo_funcionario, salario_funcionario)
            continue
        
        case 2:
            nome_produto = input('Digite o nome do produto: ')
            preco_produto = float(input('Digite o preço do produto: '))
            volume = input('Digite o volume do produto(ex: 1ml, 2kg...): ')
            quantidade_produto = int(input('Digite a quantidade em estoque: '))
            id_produto = input('Digite o ID do produto: ')
            produto.adicionar_produto(nome_produto, preco_produto, volume, quantidade_produto, id_produto)
            continue

        case 3:
            vendas.exibir_vendas()
            continue

        case 4:
            produto.exibir_produto()
            continue