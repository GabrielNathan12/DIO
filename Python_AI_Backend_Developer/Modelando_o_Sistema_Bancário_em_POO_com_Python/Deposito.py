from Transacao import Transacao
from Conta import Conta

class Deposito(Transacao):
    def __init__(self, valor:float) -> None:
        super().__init__()
        self._valor = valor

    @property 
    def valor(self) -> float:
        return self._valor
    
    def registar(self, conta: Conta) -> None:
        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)