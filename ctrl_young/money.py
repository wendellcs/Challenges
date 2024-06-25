class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome 
        self.cpf = cpf 
        self.idade = idade 

# Conta Poupança
class Cp(Pessoa):
    def __init__(self, nome, cpf, idade):
        super().__init__( nome, cpf, idade)
        self.__saldo = 500

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo

# Conta Corrente    
class Cc(Pessoa):
    def __init__(self, nome, cpf, idade, cp):
        super().__init__( nome, cpf, idade)
        self.cp = cp

    def pagar(self, valor):
        if self.cp.getSaldo() > valor:
            self.cp.setSaldo(self.cp.getSaldo() - valor)
            print('Pagamento efetuado com sucesso! \nSaldo disponível em conta: R$' + str(self.cp.getSaldo()))
            self.gerarComprovante(valor)
        else: 
            print('Saldo insuficiente.')

    def gerarComprovante(self, valor):
        with open('comprovante.txt', 'w' , encoding='utf8') as comprovante:
            comprovante.write(f'Transação realizada com sucesso! \nDados: \n -> Nome: {self.nome} \n -> CPF: {self.cpf}. \nValor pago: R${valor:.2f}')

       
pessoa_poupanca = Cp("Nome Exemplo", "12345678900", 30)
pessoa_corrente = Cc("Nome Exemplo", "12345678900", 30, pessoa_poupanca)

pessoa_corrente.pagar(20)