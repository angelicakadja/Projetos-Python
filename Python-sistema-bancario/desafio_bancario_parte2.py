def menu():
    menu = '''
    ============================================================
          SEJA MUITO(A) BEM-VINDO(A) AO NOSSO 🏦 VIRTUAL!   
    ============================================================
              👋 Olá! Como podemos lhe ajudar hoje?
               👇 Por gentileza escolha um número:
    ------------------------------------------------------------\n
                    ╔═════════════════════════╗
                               MENU         
                    ---------------------------
                        [0] - 💰  Depositar    
                        [1] - 💸  Sacar       
                        [2] - 📄  Extrato   
                        [3] - 💻  Novo cliente
                        [4] - ✒️   Nova conta
                        [5] - 🚪  Sair       
                    ╚═════════════════════════╝
    => '''
    return input(menu)
    # Se quiser remover remove espaços em branco antes de cada linha, usar (textwrap.dedent(menu)).
    # Fazer também a importação import textwrap.


def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        confirm = int(input(f"Por gentileza, confirma o valor de R$ {valor} para depósito?\n [1] - SIM\n [2] - NÃO\n"))
        if confirm == 1:
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\n✔️  Depósito efetuado com sucesso! Seu saldo atual é de R$ {saldo:.2f}.")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("💢 Operação falhou! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print(f"\n💢 Operação falhou! O valor do saque excede o limite de R$ {limite:.2f} por transação.")

    elif excedeu_saques:
        print(f"Você já atingiu o limite de {limite_saques} saques por dia.")    

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n👍 Saque realizado com sucesso!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato): # argumento (positional only 'saldo', /,) argumento (keyword only 'nomeada, /, *, 'extrato')
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n✔ Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n🔎 Usuário não encontrado, fluxo de criação de conta encerrado!")


def main():
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

        if opcao == '0': #depositar
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '1': #sacar
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '2': #extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '3': #novo cliente
            criar_usuario(usuarios)

        elif opcao == '4': #nova conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5': #sair
            print("              Obrigado por usar nossos serviços. 🤝")
            print("                        Até breve! 👋\n")
            break

        else:
            print("\n Opção inválida! Por favor, selecione novamente uma opção pelo menu acima.")

main()