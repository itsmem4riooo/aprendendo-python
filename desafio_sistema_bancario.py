menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = str(input(menu))

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))
        
        if(valor > 0):
            saldo += valor
            extrato += f"Depósido de R${valor}\n"
            continue
        else:
            print('Valor inválido')
            continue

    if opcao == "s":
        
        if numero_saques == LIMITE_SAQUES:

            print("Você atingio o número máximo de saques diarios!")

        else:

            print(f"SALDO: R${saldo} LIMITE DE SAQUE: R${limite}\n SAQUES DISPONÍVEIS: {LIMITE_SAQUES-numero_saques}")
            valor = float(input("Informe o valor que deseja sacar: "))

            if valor <= (saldo and limite):
                saldo -= valor
                extrato += f"Saque de R${valor}\n"
                numero_saques += 1
                print(f"Você sacou R${valor}\n")
            else:
                print("\nValor inválido ou insuficiente!")

    elif opcao == "e":
        print("EXTRATO".center(50,'='),end='\n\n')
        print("Não houve movimentações na conta".center(50) if not extrato else extrato)
        print()
        print("".center(50,'='))
    elif opcao == "q":
        break
    else:
        print("Opção inválida!")
    