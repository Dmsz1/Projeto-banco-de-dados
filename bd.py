class ContaBancaria:
    def __init__(self, nome, numero, saldo_inicial=0):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo_inicial
        self.historico = []

    def registrar_transacao(self, tipo, valor):
        self.historico.append({"tipo": tipo, "valor": valor})


class SistemaBancario:
    def __init__(self):
        self.contas = {}

    def criar_conta(self):
        nome = input("Digite o nome do cliente: ")
        numero = input("Digite o número da conta: ")
        if numero in self.contas:
            print("Erro: Já existe uma conta com esse número.")
            return

        saldo_inicial = float(input("Digite o saldo inicial: "))
        self.contas[numero] = ContaBancaria(nome, numero, saldo_inicial)
        print("Conta criada com sucesso!")

    def consultar_saldo(self):
        numero = input("Digite o número da conta: ")
        conta = self.contas.get(numero)
        if conta:
            print(f"O saldo atual da conta é: R${conta.saldo:.2f}")
        else:
            print("Erro: Conta não encontrada.")

    def depositar(self):
        numero = input("Digite o número da conta: ")
        conta = self.contas.get(numero)
        if conta:
            valor = float(input("Digite o valor do depósito: "))
            conta.saldo += valor
            conta.registrar_transacao("Depósito", valor)
            print(f"Depósito realizado com sucesso! Novo saldo: R${conta.saldo:.2f}")
        else:
            print("Erro: Conta não encontrada.")

    def sacar(self):
        numero = input("Digite o número da conta: ")
        conta = self.contas.get(numero)
        if conta:
            valor = float(input("Digite o valor do saque: "))
            if valor > conta.saldo:
                print("Erro: Saldo insuficiente para saque.")
            else:
                conta.saldo -= valor
                conta.registrar_transacao("Saque", valor)
                print(f"Saque realizado com sucesso! Novo saldo: R${conta.saldo:.2f}")
        else:
            print("Erro: Conta não encontrada.")

    def encerrar_conta(self):
        numero = input("Digite o número da conta: ")
        conta = self.contas.get(numero)
        if conta:
            if conta.saldo == 0:
                del self.contas[numero]
                print("Conta encerrada com sucesso!")
            else:
                print("Erro: A conta só pode ser encerrada com saldo zerado.")
        else:
            print("Erro: Conta não encontrada.")

    def exibir_historico(self):
        numero = input("Digite o número da conta: ")
        conta = self.contas.get(numero)
        if conta:
            print("Histórico de transações:")
            for transacao in conta.historico:
                print(f"{transacao['tipo']}: R${transacao['valor']:.2f}")
        else:
            print("Erro: Conta não encontrada.")

    def menu(self):
        while True:
            print("\nMenu de Opções:")
            print("1. Criar conta")
            print("2. Consultar saldo")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Encerrar conta")
            print("6. Exibir histórico de transações")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_conta()
            elif opcao == "2":
                self.consultar_saldo()
            elif opcao == "3":
                self.depositar()
            elif opcao == "4":
                self.sacar()
            elif opcao == "5":
                self.encerrar_conta()
            elif opcao == "6":
                self.exibir_historico()
            elif opcao == "7":
                print("Saindo do sistema bancário.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.menu()
