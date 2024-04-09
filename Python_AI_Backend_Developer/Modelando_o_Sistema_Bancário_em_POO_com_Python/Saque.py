from Transacao import Transacao
from Conta import Conta

class Saque(Transacao):
    def __init__(self, valor:float) -> None:
        super().__init__()
        self._valor = valor

    @property 
    def valor(self):
        return self._valor
    
    def registar(self, conta: Conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)