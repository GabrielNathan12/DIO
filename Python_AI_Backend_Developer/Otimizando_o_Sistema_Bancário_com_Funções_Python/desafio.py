import textwrap


class Menu:
    def __init__(self):
        self.LIMITE_SAQUES = 3
        self.AGENCIA = "0001"
        self.usuarios = []

    def exibir(self):
        menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu))

    def criar_conta(self, /, *, usuario):
        numero_conta = len(usuario.contas) + 1
        conta = Conta(self.AGENCIA, numero_conta, usuario)
        usuario.contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
        return conta

    def listar_contas(self, usuario):
        for conta in usuario.contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero_conta}
                Titular:\t{conta.usuario.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))


class Usuario:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []


class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0


def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return usuario

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = Usuario(cpf, nome, data_nascimento, endereco)
    menu.usuarios.append(novo_usuario)
    print("=== Usuário criado com sucesso! ===")
    return novo_usuario


def filtrar_usuario(cpf,/):
    for usuario in menu.usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


def depositar(conta,/):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        conta.saldo += valor
        conta.extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def sacar(conta,/):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > conta.saldo
    excedeu_limite = valor > 500
    excedeu_saques = conta.numero_saques >= menu.LIMITE_SAQUES

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        conta.saldo -= valor
        conta.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        conta.numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")


menu = Menu()

while True:
    opcao = menu.exibir()

    if opcao == "d":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)
        if usuario:
            menu.listar_contas(usuario)
            numero_conta = int(input("Informe o número da conta: "))
            for conta in usuario.contas:
                if conta.numero_conta == numero_conta:
                    depositar(conta)
        else:
            print("\n@@@ Usuário não encontrado! @@@")

    elif opcao == "s":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)
        if usuario:
            menu.listar_contas(usuario)
            numero_conta = int(input("Informe o número da conta: "))
            for conta in usuario.contas:
                if conta.numero_conta == numero_conta:
                    sacar(conta)
        else:
            print("\n@@@ Usuário não encontrado! @@@")

    elif opcao == "e":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)
        if usuario:
            menu.listar_contas(usuario)
            numero_conta = int(input("Informe o número da conta: "))
            for conta in usuario.contas:
                if conta.numero_conta == numero_conta:
                    exibir_extrato(conta)
        else:
            print("\n@@@ Usuário não encontrado! @@@")

    elif opcao == "nu":
        criar_usuario()

    elif opcao == "nc":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)
        if usuario:
            menu.criar_conta(usuario)
        else:
            print("\n@@@ Usuário não encontrado! @@@")

    elif opcao == "lc":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)
        if usuario:
            menu.listar_contas(usuario)
        else:
            print("\n@@@ Usuário não encontrado! @@@")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
