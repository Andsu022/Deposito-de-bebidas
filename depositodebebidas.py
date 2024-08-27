# Sistema de gerenciamento para comércios de venda de bebidas, com opções de cadastrar produtos, cadastrar funcionários, efetuar vendas;
import abc
#Classe Funcionario como interface para as classes Atendente e Gerente
class Funcionario(abc.ABC):    

    def __init__(self):
        self.lista_funcionarios = {}

    @abc.abstractmethod
    def autenticar_Funcionario(self, matricula, senha):
        pass
    

    @abc.abstractmethod
    def exibir_funcionario(self):
        pass
    
    @abc.abstractmethod
    def gerar_bonificacao(self, matricula, valor):
        pass

class Atendente(Funcionario):
    def __init__(self):
        super().__init__()


    def adiciona_funcionario(self, nome, cpf, matricula, senha, cargo, salario):
        self.lista_funcionarios.update({matricula:{'Nome': nome, 'CPF': cpf, 'Cargo': cargo, 'Senha': senha, 'Salário': salario}})


    def autenticar_Funcionario(self, matricula, senha):
        for chave, valor in self.lista_funcionarios.items():
            if (matricula == chave) and (senha == valor['Senha']):
                return True
           
        return None


    def exibir_funcionario(self):
        for chave, valor in self.lista_funcionarios.items():
            senha_backup = str(valor['Senha'])
            valor['Senha'] = ('*' * len(senha_backup))
            cpf_backup = valor['CPF']
            valor['CPF'] = ('*' * len(cpf_backup))
            print(f'Matrícula: {chave}\nInformações:{valor}')
            print('-------------')
            valor['Senha'] = int(senha_backup)
            valor['CPF'] = cpf_backup


    def gerar_bonificacao(self, matricula, valor):
        pass


class Gerente(Funcionario):
    def __init__(self):
        super().__init__()


    def adiciona_funcionario(self, nome, cpf, matricula, cargo, senha, salario):
        self.lista_funcionarios.update({matricula:{'Funcionário': nome, 'CPF': cpf, 'Cargo': cargo, 'Senha': senha, 'Salário': salario}})


    def autenticar_Funcionario(self, matricula, senha):
        for chave, valor in self.lista_funcionarios.items():
            if (matricula == chave) and (senha == valor['Senha']):
                return True
           
        return None
    

    def exibir_funcionario(self):
        for chave, valor in self.lista_funcionarios.items():
            senha_backup = str(valor['Senha'])
            valor['Senha'] = ('*' * len(senha_backup))
            cpf_backup = valor['CPF']
            valor['CPF'] = ('*' * len(cpf_backup))
            print(f'Matrícula: {chave}\nInformações:{valor}')
            print('-------------')
            valor['Senha'] = int(senha_backup)
            valor['CPF'] = cpf_backup


    def gerar_bonificacao(self, matricula, valor):
        pass

class Cliente():

    def __init__(self):
        self.lista_clientes = {}


    def adicionar_cliente(self, nome, cpf, rua, numero, bairro, complemento):
        self.lista_clientes.update({nome:{'CPF': cpf, 'Rua': rua, 'Número': numero, 'Bairro': bairro, 'Complemento': complemento}})

    @classmethod
    def exibir_cliente(cls):
        for chave, valor in cls.lista_clientes.items():
            cpf_backup = valor['CPF']
            valor['CPF'] = ('*' * len(cpf_backup))
            print(f'Cliente:{chave}\nInformações:{valor}')
            valor['CPF'] = cpf_backup


class Produto:

    def __init__(self):
        self.lista_produtos = {}


    def adicionar_produto(self, nome_produto, preco, volume, estoque, id_produto):
            self.lista_produtos.update({id_produto:{'Produto': nome_produto, 'Preco em R$': preco, 'Volume': volume, 'Quantidade em estoque': estoque}})


    def alterar_estoque(self, id_produto, quantidade):
        for chave, value in self.lista_produtos.items():
            if id_produto == chave:
                value['Quantidade em estoque'] -= quantidade

    @classmethod
    def exibir_produto(cls):
        for chave, value in cls.lista_produtos.items():
            print(f'ID:{chave}\nDados:{value}')
            print('--------------------------------')
    
    

class Vendas(Produto, Atendente):
    
    def __init__(self):
        super().__init__()
        super().__init__()
        self.lista_vendas = {}
        self._total_vendas = 0
        

    def efetuar_venda(self, id_vendedor, id_produto, quantidade):
        vendedor = Atendente()
        produto = Produto()

        for chave, value in vendedor.lista_funcionarios.items():
            if id_vendedor == chave:
                nome_vendedor = value['Funcionário']

        for chave, value in produto.lista_produtos.items():
            if id_produto == chave:
                nome_produto = value['Produto']
                preco_produto = value['Preco em R$']

        produto.alterar_estoque(id_produto, quantidade)

        self._total_vendas += preco_produto
        self.lista_vendas.update({'Produto': nome_produto, 'Quantidade': quantidade, 'Vendedor': nome_vendedor, 'Valor': preco_produto})

    @classmethod
    def exibir_vendas(cls):
        for chave, valor in cls.lista_vendas.items():
            print(f'{chave}:{valor}')
            print('----------------------------------')

        print(f'Faturamento total: R${cls._total_vendas}')
 