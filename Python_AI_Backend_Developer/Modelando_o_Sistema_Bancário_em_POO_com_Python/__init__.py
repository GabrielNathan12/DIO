from Saque import Saque
from Transacao import Transacao
from Cliente import Cliente
import textwrap
from Deposito import Deposito
from ContaCorrente import ContaCorrente
from PessoaFisica import PessoaFisica

def menu():
    menu = '''\n
        =========== MENU ==========
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Contas
        [nu]\tNovo cliente
        [q]\t Sair 
        ==>
        '''
    return input(textwrap.dedent(menu))

def filtrar_clientes(cpf, clientes):
    cli_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cli_filtrados[0] if cli_filtrados else None

def recupear_conta_corrente(cliente:Cliente):
    if not cliente.contas:
        print('\n Esse cliente não possui contas no nosso sistema')
        return 
    return cliente.contas[0]

def depositar(clientes:Cliente):
    cpf = input('Informe o CPF: ')
    cliente = filtrar_clientes(cpf=cpf, clientes=clientes)

    if not cliente:
        print('\n Cliente não foi encontrado')
        return 
    valor = float(input('Informe o valor a ser depositado: '))
    transacao = Deposito(valor=valor)

    conta = recupear_conta_corrente(cliente=cliente)

    if not conta:
        return 
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes:Cliente):
    cpf = input('Informe o CPF: ')
    cliente = filtrar_clientes(cpf=cpf, clientes=clientes)

    if not cliente:
        print('\n Cliente não foi encontrado')
        return 
    valor = float(input('Informe o valor a ser sacado: '))
    transacao = Saque(valor=valor)

    conta = recupear_conta_corrente(cliente=cliente)

    if not conta:
        return 
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes: Cliente):
    cpf = input('Informe o CPF: ')
    cliente = filtrar_clientes(cpf=cpf, clientes=clientes)

    if not cliente:
        print('\n Cliente não foi encontrado')
        return
    
    conta = recupear_conta_corrente(cliente=cliente)

    if not conta:
        return
    
    print('\n ========== EXTRATO ========== ')
    transacoes = conta.historico._transacoes

    extrato = ''

    if not transacoes:
        extrato = 'Não foram relizadas movimentações nessa conta'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao["tipo"]}:\n\t R$ {transacao["valor"]:.2f}'

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('====================')

def criar_novo_cliente(clientes):
    cpf = input('Informe o CPF: ')
    cliente = filtrar_clientes(cpf=cpf, clientes=clientes)

    if cliente:
        print('\n Cliente já cadastrado encontrado')
        return
    nome = input('Informe seu nome: ')
    data_nasc = input('Informe a data de nascimento: ')
    endereco = input('Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ')

    cliente = PessoaFisica(nome=nome, data_nasc=data_nasc, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print('\n === Cliente Criado com Sucesso')

def criar_conta(numero_conta:int, clientes:Cliente, contas):
    cpf = input('Informe o CPF: ')
    cliente = filtrar_clientes(cpf=cpf, clientes=clientes)
    
    if not cliente:
        print('\n Cliente não foi encontrado')
        return
    
    conta = ContaCorrente.criar_nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('\n === Conta Criada com Sucesso')    

def listar(contas:list):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nu':
            criar_novo_cliente(clientes)
        elif opcao == 'nc':
            num_conta = len(contas) + 1
            criar_conta(num_conta, clientes, contas)
        elif opcao == 'lc':
            listar(contas)
        elif opcao == 'q':
            break

if __name__ == '__main__':
    main()