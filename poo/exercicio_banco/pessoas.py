class Pessoa:
    def __init__(self, nome,idade):
        self._nome = nome
        self._idade = idade
    @property
    def nome(self):
            return self._nome
    @property
    def idade(self):
        return self._idade
    
    @nome.setter 
    def nome(self,nome):
        self._nome = nome
    @idade.setter 
    def idade(self,idade):
        self._idade = idade
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self,nome, idade):
        super().__init__(nome,idade)
        self.conta = None

if __name__ =='__main__':
    import contas
    c1 = Cliente('Gabs',28)
    c1.conta = contas.ContaCorrente(111,222,0,0)
    print(c1)
    print(c1.conta)