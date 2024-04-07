LIMITE_SAQUES = 3

class Conta:

    def __init__(self):
        self.__saldo = 0
        self.__limite = 500
        self.__extrato = ''
        self.__num_saques = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def sacar(self, valor):

        passou_saldo = valor > self.__saldo
        passou_limite = valor > self.__limite
        passou_n_saques = self.__num_saques >= LIMITE_SAQUES

        if passou_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif passou_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif passou_n_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.__saldo -= valor
            self.__extrato += f"Saque: R$ {valor:.2f}\n"
            self.__num_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    def extrato (self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.__extrato else self.__extrato)
        print(f"\nSaldo: R$ {self.__saldo:.2f}")
        print("==========================================")

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

conta = Conta()

while True:

    opcao = input(menu)

    if opcao == "1":
       valor = float(input("Informe o valor do depósito: "))
       conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")