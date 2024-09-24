import abc

class Conta(abc.ABC):
    
    def __init__(self,agencia,conta,saldo =0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    def depositar(self,valor):
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')    
    
    @abc.abstractmethod
    def sacar(self, valor):...

    def detalhes(self,msg =''):
        print(f'O seu saldo e {self.saldo:.2f} {msg}')

class ContaPoupanca(Conta):
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo})'
        return f'{class_name}{attrs}'
        
 
    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor 

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')


class ContaCorrente(Conta):
    def __init__(self,agencia,conta,saldo = 0,limite =0 ):
        super().__init__(agencia,conta,saldo)
        self.limite = limite

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo},{self.limite})'
        return f'{class_name}{attrs}'


    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor 
        limite_maximo = - self.limite
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')


if __name__ =='__main__':
    #cp1 = ContaPoupanca(111,222,0)
    #cp1.sacar(1)
    cc1 = ContaCorrente(111,222,0,100)
    cc1.sacar(1)    
    cc1.sacar(90)
    cc1.sacar(10)
    