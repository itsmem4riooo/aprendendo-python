import functions

print("\n"+"*" * 40,)
print("\n     Bem-vindo ao Python Bank\n")
print("     ESCOLHA UMA OPÇÃO PARA CONTINUAR:")
print("     [1] REGISTRAR [2] CADASTRAR NOVA CONTA [3] LOGAR \n")
print("*" * 40, end="\n\n")

while True: 

    action = input("Digite uma opção para prosseguir:")

    if action == "1":
        functions.register()
    elif action == "2":
        functions.add_account()
    elif action == "3":
        while True:
            user,user_id = functions.login()
            if user:

                print('CONTAS REGISTRADAS NESTE USUÁRIO: ')
                for account in user['accounts'].keys():
                    if(int(account)):
                        print(f"CONTA: [{account}]",end=' ')

                account_id = int(input('\n SELECIONE UMA CONTA PARA CONTINUAR: '))

                while not account_id in user['accounts']:
                    account_id = int(input('SELECIONE UMA CONTA PARA CONTINUAR: '))
                
                print("\n"+"*" * 40,)
                print(f"\n     Bem-vindo {user['name']}\n")

                print("*" * 40, end="\n\n")

                while True:

                    menu = """
MENU

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


                    

                    menu_option = str(input(menu))

                    if menu_option == "d":
                            
                        functions.deposit(float(input("Informe o valor do depósito: ")),account_id,user_id)
                        continue                            

                    if menu_option == "s":
                            functions.withdrawal(account_id,user_id)
                    elif menu_option == "e":
                        functions.extract(account_id,user=user_id)
                    elif menu_option == "q":
                        break
                    else:
                        print("Opção inválida!")
