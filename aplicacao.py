from modelo import depositodebebidas, interface_atendente, interface_gerente, menus
atendente = depositodebebidas.Atendente()
produto = depositodebebidas.Produto()
gerente = depositodebebidas.Gerente()
cliente = depositodebebidas.Cliente()
vendas = depositodebebidas.Vendas()

def main():
    while True:
        try:
            opc = int(input(menus.menu_principal))
            match opc:

                case 1:
                    nome = input('Digite o nome do gerente: ')
                    cpf_funcionario = input('Digite o CPF do gerente: ')
                    matricula_funcionario = input('Digite a matrícula: ')
                    senha_funcionario = input('Digite uma senha alfanumérica: ')
                    cargo_funcionario = 'Gerente'
                    salario_funcionario = 4100.54
                    atendente.adiciona_funcionario(nome, cpf_funcionario, matricula_funcionario, senha_funcionario, cargo_funcionario, salario_funcionario)
                    continue

                case 2:
                    opc = int(input('1 - Login Gerente\n2 - Login Vendedor: '))
                    if opc == 1:
                        matricula = input('Digite a matrícula: ')
                        senha = input('Digite a senha: ')
                        login_gerente = gerente.autenticar_Funcionario(matricula, senha)
                        if login_gerente == True:
                            interface_gerente

                    elif opc == 2:
                        matricula = input('Digite a matrícula: ')
                        senha = input('Digite a senha: ')
                        login_atendente = atendente.autenticar_Funcionario(matricula, senha)
                        if login_atendente == True:
                            interface_atendente

                case 3:
                    print('| ENCERRANDO ...')
                    break    

        except:
            print('''
                |===ERRO===|
                ''')

if __name__ == '__main__':
    main()