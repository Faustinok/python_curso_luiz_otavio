import contas
import pessoas
class Banco:
    def __init__(
        self,agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None, 
        contas: list[contas.Conta] | None = None ,
        ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas  or []
           
    def __repr__(self):        
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r},{self.contas!r})'
        return f'{class_name}{attrs}'

    def _checa_se_conta_e_do_cliente(self,cliente,conta):
        print('checando se a conta e do cliente')
        if  conta is cliente.conta:
            return True
        return False

    def _checa_agencia(self,conta):
        print('checando agencia')
        if conta.agencia in self.agencias:
            return True
        return False


    def _checa_cliente(self,cliente):
        print('checando cliente')
        if cliente in self.clientes:
            return True
        return False
        
    def _checa_conta(self,conta):
        print('checando conta')
        if conta in self.contas:
            return True
        return False

    def autenticar(self,cliente:pessoas.Pessoa ,conta: contas.Conta):

        return self._checa_agencia(conta) and \
                self._checa_cliente(cliente) and \
                self._checa_conta(conta) and  \
                self._checa_se_conta_e_do_cliente(cliente,conta)    


if __name__ =='__main__':
    c1 = pessoas.Cliente('Gabs',28)
    c1.conta = contas.ContaCorrente(111,222,0,0)
    conta2 = contas.ContaPoupanca(111,333,0)
    b1 = Banco()
    b1.clientes.extend([c1])
    b1.contas.extend([c1.conta])
    b1.agencias.extend([111,222])
    if b1.autenticar(c1,c1.conta):
        c1.conta.depositar(10)
        c1.conta.depositar(10)