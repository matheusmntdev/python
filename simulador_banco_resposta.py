# usar list(eval()) para converter a string para lista de volta

def criar_conta(contas):
    numero = input("Digite o número da nova conta (ex.: 1234): ").strip()
    for conta in contas:
        if conta["numero"] == numero:
            print("Essa conta já existe!")
            return
    titular = input("Digite o nome do titular: ").strip()
    if not titular:
        print("O nome do titular não pode ser vazio!")
        return
    contas.append({"numero": numero, "titular": titular, "saldo": 0.0})
    print(f"Conta {numero} criada para {titular} com sucesso!")


def buscar_conta(contas, numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None


def depositar(contas):
    numero = input("Digite o número da conta: ").strip()
    conta = buscar_conta(contas, numero)
    if conta:
        try:
            valor = float(input("Digite o valor a depositar: "))
            if valor > 0:
                conta["saldo"] += valor
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            else:
                print("O valor deve ser positivo!")
        except ValueError:
            print("Digite um valor numérico válido!")
    else:
        print("Conta não encontrada!")


def sacar(contas):
    numero = input("Digite o número da conta: ").strip()
    conta = buscar_conta(contas, numero)
    if conta:
        try:
            valor = float(input("Digite o valor a sacar: "))
            if valor > 0:
                if conta["saldo"] >= valor:
                    conta["saldo"] -= valor
                    print(f"Saque de R${valor:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente!")
            else:
                print("O valor deve ser positivo!")
        except ValueError:
            print("Digite um valor numérico válido!")
    else:
        print("Conta não encontrada!")


def transferir(contas):
    origem_num = input("Digite o número da conta de origem: ").strip()
    origem = buscar_conta(contas, origem_num)
    if origem:
        destino_num = input("Digite o número da conta de destino: ").strip()
        destino = buscar_conta(contas, destino_num)
        if destino:
            try:
                valor = float(input("Digite o valor a transferir: "))
                if valor > 0:
                    if origem["saldo"] >= valor:
                        origem["saldo"] -= valor
                        destino["saldo"] += valor
                        print(f"Transferência de R${valor:.2f} realizada com sucesso!")
                    else:
                        print("Saldo insuficiente na conta de origem!")
                else:
                    print("O valor deve ser positivo!")
            except ValueError:
                print("Digite um valor numérico válido!")
        else:
            print("Conta de destino não encontrada!")
    else:
        print("Conta de origem não encontrada!")


def consultar_saldo(contas):
    numero = input("Digite o número da conta: ").strip()
    conta = buscar_conta(contas, numero)
    if conta:
        print(f"Conta: {conta['numero']} | Titular: {conta['titular']} | Saldo: R${conta['saldo']:.2f}")
    else:
        print("Conta não encontrada!")


def menu():
    contas = []
    while True:
        print("\n--- Simulador de Banco ---")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Consultar saldo")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == '1':
            criar_conta(contas)
        elif opcao == '2':
            depositar(contas)
        elif opcao == '3':
            sacar(contas)
        elif opcao == '4':
            transferir(contas)
        elif opcao == '5':
            consultar_saldo(contas)
        elif opcao == '6':
            print("Saindo do simulador. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Iniciar o programa
if __name__ == "__main__":
    menu()
