from Transacao import Transacao

class Cliente:
    def __init__(self, endereco:str) -> None:
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self) -> list:
        return self._contas
    @property
    def endereco(self)-> str:
        return self._endereco
    
    def adicionar_conta(self, conta) -> None:
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao: Transacao) -> None:
        transacao.registar(conta)


