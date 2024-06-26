def menu():

    menu = """
========== BANCO V.1 =========
|                            |
|    [d] - Deposito          |
|    [s] - Saque             |
|    [e] - Extrato           |
|    [nu] - Novo Usuario     |
|    [nc] - Nova Conta       |
|    [L] - Listar Usuario    |
|    [q] - Sair              |
|                            |
==============================

==> : """
    return input(menu).lower()


def cabecalho(texto):
    print("=" * 60)
    print(texto.center(60))
    print("=" * 60)


def leiaInt(msg):

    while True:
        num = input(msg)
        if num.isnumeric() and len(num) == 11:
            num = int(num)
            return num
        else:
            print('CPF INVALIDO DIGITE UM VALOR INTEIRO COM 11 DIGITOS')


def deposito(valor_deposito, saldo, extrato):

    saldo += valor_deposito
    texto_deposito = "Deposito: "
    extrato += f"{texto_deposito:<18} R${valor_deposito:.2f}\n"
    print()
    cabecalho("@@@ DEPOSITO FEITO COM SUCESSO")

    return saldo, extrato


def saque(*, saldo, valor, extrato, LIMITE_SAQUES, numero_saques, limite):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES
    if excedeu_saldo:
        print()
        cabecalho("OPERAÇÃO FALHOU! VOCÊ NÃO TEM SALDO SUFICIENTE!!!")
    elif excedeu_limite:
        print()
        cabecalho("OPERAÇÃO FALHOU! VOCÊ NÃO TEM LIMITE SUFICIENTE!!!")
    elif excedeu_saques:
        print()
        cabecalho("OPERAÇÃO FALHOU! VOCÊ EXCEDEU O LIMITE DE SAQUES!!!")

    elif valor > 0:
        saldo -= valor
        texto_saque = "Saque:"
        extrato += f" {texto_saque:<15}  R${valor:.2f}\n"
        numero_saques += 1
        print()
        cabecalho("SAQUE REALIZADO COM SUCESSO")

    return saldo, extrato


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf
    ]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = leiaInt('Digite seu CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print('@@@@ CPF JÁ CADASTRADOO @@@@@@')
        return
    nome = input('Digite seu nome: ')
    endereco = input("Digite seu endereço: (Logradouro, N. - Bairro): ")
    data_nascimento = input("Digite sua data de nascimento(dd-mm-aaaa): ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "endereco": endereco,
        "data_nascimento": data_nascimento
    })

    cabecalho("NOVO USUARIO CADASTRADO COM SUCESSO")


def criar_conta(usuarios, numero_conta, AGENCIA):
    cpf = input('Digite seu CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print('==@@ CONTA CRIADA COM SUCESSO @@@==')
        return ({
            "agencia": AGENCIA,
            "numero": numero_conta,
            "usuario": usuario
        })

    print("==@@ USUARIO NAO ENCONTRADO NA BASE DE DADOS @@@==")


def listar_usuarios(usuarios):
    num_usuarios = 1
    if len(usuarios) == 0:
        print("""
        @@@@@ NENHUM USUARIO CADASTRADO NO BANCO @@@@@
        """)
    else:
        for usuario in usuarios:
            print(f"USUARIO Nª{num_usuarios}")
            print('=' * 60)
            for k,v in usuario.items():
                print(f'{k.upper():45}{v}')
            print('='*60)
            num_usuarios = 1


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "d":
            cabecalho('DEPOSITO')
            valor_deposito = float(input("Digite o valor do deposito R$: "))

            saldo, extrato = deposito(valor_deposito, saldo, extrato)

        elif opcao == "s":
            cabecalho('SAQUE')
            valor = float(input("Digite o valor do saque R$: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                LIMITE_SAQUES=LIMITE_SAQUES,
                numero_saques=numero_saques,
                limite=limite,
            )
        elif opcao == "nu":
            cabecalho('NOVO USUARIO')
            criar_usuario(usuarios)

        elif opcao == 'nc':
            cabecalho('NOVA CONTA')
            numero_contas = len(contas) + 1
            conta = criar_conta(usuarios, numero_contas, AGENCIA)

            if conta:
                contas.append(conta)
        elif opcao == 'l':
            cabecalho('USUARIOS')
            listar_usuarios(usuarios)

        elif opcao == "e":
            print("=========== Extrato ==========")
            print(extrato)
            print("=============================")
            print(f"Saldo:             R${saldo:.2f}\n")
        elif opcao == "q":
            print("""
    ========= 123 SAINDOOOOO =======
    OBRIGADO POR UTILIZAR NOSSO BANCO.

    """)
            break

        else:
            print("Print opcao invalida digite um opcao valida novamente.")


main()
