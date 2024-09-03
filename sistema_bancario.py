import textwrap

def menu():
    menu = """\n
    -------------------- BEM-VINDO! --------------------
    Digite a opção que corresponde à operação desejada:
    [d] \tDepósito
    [s] \tSaque
    [e] \tExtrato
    [nu] \tNovo usuário
    [nc] \tNova conta
    [lc] \tListar contas
    [q] \tSair
    Opção: """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += "Depósito: \t\tR$ {:0.2f}\n".format(valor)
        print("\n\033[32mDepósito realizado com sucesso! Cheque seu extrato.\033[m\n\n")
    else:
        print("\n\033[31mA operação falhou! O valor informado é inválido.\033[m\n\n")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > 0:
            if valor <= limite:
                if valor <= saldo:
                    saldo -= valor
                    extrato += "Saque: \t\t\tR$ {:0.2f}\n".format(valor)
                    numero_saques += 1
                    print("\n\033[32mSaque realizado com sucesso! Cheque seu extrato.\033[m\n\n")
                else:
                    print("\n\033[31mA operação falhou! Seu saldo é insuficiente.\033[m\n\n")
            else:
                print("\n\033[31mA operação falhou! O limite máximo por saque é de R$ {:0.2f}.\033[m\n\n".format(limite))
        else:
            print("\n\033[31mA operação falhou! O valor informado é inválido.\033[m\n\n")
    else:
        print("\n\033[31mA operação falhou! Número máximo de saques diários atingido.\033[m\n\n")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n--------------- EXTRATO ---------------")
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print("\nSaldo atual: \t\tR$ {:0.2f}".format(saldo))
    print("---------------------------------------\n")

def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[31mCPF já cadastrado.\033[m\n\n")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade / UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n\033[32mUsuário criado com sucesso.\033[m\n\n")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[32mConta criada com sucesso.\033[m\n\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n\033[31mUsuário não encontrado.\033[m\n\n")

def listar_contas(contas):
    for contas in contas:
        linha = f"""\
            Agência:\t{contas['agencia']}
            CC:\t\t{contas['numero_conta']}
            Titular:\t{contas['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: R$ "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por usar o sistema!\n\n")
            break

        else:
            print("\n\033[31mA operação falhou! Escolha uma opção válida.\033[m\n\n")

main ()