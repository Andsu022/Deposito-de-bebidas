import abc
lista_produtos = {}
lista_clientes = {}

class Funcionario():

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.lista_func = {}




class Atendente(Funcionario):

    def __init__(self, nome, matricula, senha, cargo):
        super().__init__(nome, matricula)
        self.nome = super().nome
        self.matricula = super().matricula
        self._senha = senha
        self.cargo = cargo


    def adiciona_funcionario(self, nome, matricula, cargo, senha):
        if len(self.lista_func) == 0:
            dados = {}
            dados['Nome'] = nome
            dados['Cargo'] = cargo
            dados['Senha'] = senha
            self.lista_func[matricula] = dados
        else:
            self.lista_func.update({matricula:{'Nome': nome, 'Cargo': cargo, 'Senha': senha}})


    def autenticarFuncionario(self, senha):
        for valor in self.lista_func.values():
            if senha == valor['Senha']:
                return True
           
        return None
        
    def exibirfunc(self):
        for chave, valor in self.lista_func.items():
            senha_backup = valor['Senha']
            valor['Senha'] = '********'
            print(f'{chave}: {valor}')
            valor['Senha'] = senha_backup



class Gerente(Funcionario):
    def __init__(self, nome, matricula, cargo, senha):
        super().__init__(nome, matricula)
        self.nome = super().nome
        self.matricula = super().matricula
        self.cargo = cargo
        self._senha = senha

    def autenticarFuncionario(self, senha):
        if(senha == self._senha):
            return True
        else:
            return False
        
    def exibirfunc(self):
        print(lista_func)


class Cliente():

    def __init__(self, nome, cpf, endereco, id):
        self._nome_cliente = nome
        self._cpf = cpf
        self._endereco = endereco
        self._id_cliente = id
        lista_clientes[self._id_cliente] = (self._nome_cliente, self._cpf, self._endereco)

    @property
    def nome_cliente(self):
        return self._nome_cliente
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def id_cliente(self):
        return self._id_cliente
    
    @nome_cliente.setter
    def nome_cliente(self, nome):
        self._nome_cliente = nome
    
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @id_cliente.setter
    def id_cliente(self, id):
        self._id_cliente = id


    def exibirCliente(self):
        print(lista_clientes)



class Produto():
    
    def __init__(self, nome_produto, preco, volume, estoque, id_produto):
        self._nome = nome_produto
        self._preco = preco
        self._volume = volume
        self._quantidade_no_estoque = estoque
        self._id_produto = id_produto
        self.lista_produtos = {}

    def adicionar_produto(self, nome_produto, preco, volume, estoque, id_produto):
        if len(self.lista_produtos) == 0:
            self.lista_produtos.update({id_produto:{'Produto': nome_produto, 'Preco': preco, 'Volume': volume, 'Quantidade no estoque': estoque}})
        else:
            self.lista_produtos.update({id_produto:{'Produto': nome_produto, 'Preco': preco, 'Volume': volume, 'Quantidade no estoque': estoque}})

    
    def alterar_estoque(self, id_produto, quantidade):
        for chave, value in self.lista_produtos.items():
            if id_produto == chave:
                value['Quantidade no estoque'] -= quantidade


    def exibirProduto(self):
        print('|=====LISTA DE PRODUTOS======|')
        for chave, value in self.lista_produtos.items():
            print(f'{chave}: {value}')


class Venda(Produto, Cliente):

    def __init__(self, prod, cliente, atendente, quantidade):
        pass


    def efetuarVenda(self, id_produto, id_cliente, id_atendente, quantidade):
        for i in lista_produtos.keys:
            if id_produto == i:
                for j in lista_produtos.items:
                    j.estoque -= quantidade

    def exibirVenda(self):
        print("Produto:",self._prodvenda)
        print("Cliente:",self._cliente_venda)
        print("Vendedor:",self._atendentenome)
        print("Quantidade:",self._quant_venda)
        print("Valor:R$ %.2f"%(self._valor))

'''
gerente  = Gerente("Anderson Luz", 200216, 9756)
atendente = Atendente("Andre Luz", 202402, 2556)
def main():
    print("--Login--\n")
    login = int(input("Digite a senha: "))
    if (gerente.autenticarFuncionario(login) == True) or (atendente.autenticarFuncionario(login) == True):
        
        while True:
            print("|Menu\n|1-Cadastrar cliente\n|2-Cadastrar produto\n|3-Cadastrar funcionário(acesso apenas do gerente)\n|4-Realizar venda\n|5-Exibir cliente\n|6-Exibir produto\n|7-Sair\n")
            menu = int(input("|Digite a opção desejada: "))
            
            if (menu == 7):
                print("ENCERRANDO SISTEMA...")
                break
            elif(menu == 1):
                cod_cliente = input("Digite um código identificador do cliente: ")
                nome = input("Digite o nome do cliente: ")
                cpf = int(input("Digite o cpf: "))
                endereco = input("Digite o endereço(apenas a rua e o numero): ")
                id = cod_cliente
                cod_cliente = Cliente(nome, cpf, endereco, id)
                lista_clientes[cod_cliente] = nome
                continue
            elif(menu == 2):
                cod_p = input("Digite um código identificador do produto: ")
                prod = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                volume = input("Digite o volume do produto(ex. 1L, 300ml): ")
                id_prod = cod_p
                estoque = int(input("Digite a quantidade em estoque: "))
                cod_p = Produto(prod, preco, volume, id_prod, estoque)
                lista_produtos[cod_p] = prod
                continue
            elif(menu == 3):
                    senha_gerente = int(input("Digite a senha: "))
                    if gerente.autenticarFuncionario(senha_gerente) == True:
                        nome_func = input("Digite o nome do funcionário: ")
                        matricula = input("Digite uma matrícula: ")
                        senha = int(input("Digite uma senha: "))
                        func = Atendente(nome_func, matricula, senha)
                        lista_func[matricula] = nome_func
                        continue
                    else:
                        print("ACESSO NEGADO !")
                        break
            elif(menu == 4):
                p = input("Digite o id do produto: ")
                cliente =  input("Digite o id do cliente: ")
                quant = input("Digite a quantidade do pedido: ")
                func = input("Digite o id do atendente: ")
                v = Venda()
                v.efetuarVenda(p, cliente, func, quant)
                opc = int(input("Ver dados de venda: 1-Sim\n2-Não\nR:"))
                if opc == 1:
                    v.exibirVenda()
                else:
                    continue
            elif(menu == 5):
                cod_cliente.exibirCliente()
                continue
            elif(menu == 6):
                cod_p.exibirProduto()
                continue
            elif(menu == 7):
                print("Finalizando sistema...")
                break
    else:
        print("ACESSO NEGADO !")



main() 
'''