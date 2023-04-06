menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Deposito")
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: O valor informado é inválido.")

    elif opcao == "2":
        print("Saque")
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= limite_de_saques

        if excedeu_saldo:
            print("Operação falhou: Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou: O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou: Numero máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        
        else:
            print("Operação falhou: O valor informado é invalido")


    elif opcao == "3":
        menu_extrato = "Extrato"
        final_menu_extrato = "======="
        print(menu_extrato.center(16,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(final_menu_extrato.center(16, "="))

    elif opcao == "4":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada!")
