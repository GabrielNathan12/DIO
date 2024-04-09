from Cliente import Cliente
from Historico import Historico


class Conta:
    def __init__(self, numero:int, cliente:Cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar_nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia
    
    @property
    def cliente(self) -> Cliente:
        return self._cliente
    
    @property
    def historico(self) -> Historico:
        return self._historico
    
    def depositar(self, valor:float) -> bool:
        if valor > 0:
            self._saldo += valor
            print('\n Depósito realizado com Sucesso')
            return True
        print('\n Operação não foi concluída !!! Valor passado é inválido')
        return False
    
    def sacar(self, valor: float) -> bool:
        saldo = self._saldo
        passou_saldo = valor > saldo

        if passou_saldo:
            print('\n Operação não foi concluída !!! Você não possui saldo suficiente.')

        elif valor > 0:
            self._saldo -= valor
            print('\n Saque realizado com sucesso')
            return True
        else:
            print('\n Operação não foi concluída !!! Valor informado é inválido ')

        return False
    