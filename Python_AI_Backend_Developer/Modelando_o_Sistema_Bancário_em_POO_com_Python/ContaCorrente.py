from Conta import Conta
from Cliente import Cliente
from Historico import Historico

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite=500, lim_saques=3) -> None:
        super().__init__(numero, cliente)
        self._limite = limite
        self.lim_saques = lim_saques

    def sacar(self, valor:float) -> bool: 
        num_saques = len([transacao for transacao in self.historico.transacao if transacao['tipo'] == 'Saque'])
        passou_limite = valor > self._limite
        passou_num_saques = num_saques >= self.lim_saques


        if passou_limite:
            print('\n Operação não concluída !!! O valor do saque passou do limite permitido')

        elif passou_num_saques:
            print('\n Operação não concluída !!! Número de saques excedidos')
        
        else:
            return super().sacar(valor=valor)
        
        return False
    
    def __str__(self) -> str:
        return f'''\
                    Agência: \t{self.agencia} 
                    C\C:\t\t{self.numero}
                    Titular: \t{self.cliente.nome}'''