from Cliente import Cliente

class Banco():
    
    Limit = 500
    Withdrawal_limit = 3

    def deposit():

        if Cliente.User:
            value = float(input('Insira o valor que deseja depositar:'))
            if value > 0:
                Cliente.update_balance('add',value)
                Cliente.list_history(type= 'Depósito',value= value)
                print(f"Depósito realidado com sucesso!\n Saldo atual: {Cliente.get_balance()}")
            else:
                print('Valor inserido inválido')
  
    def withdrawal():
        if Cliente.User:
            
            if Cliente.User['accounts'][Cliente.account_id]['number_withdrawal'] == Banco.Withdrawal_limit:
                print('Limite de saques atingidos!')
                return False
            
            print(f"SALDO: R${Cliente.get_balance()} LIMITE DE SAQUE: R${Banco.Limit}\n SAQUES DISPONÍVEIS: {(Banco.Withdrawal_limit - Cliente.User['accounts'][Cliente.account_id]['number_withdrawal'])}")    
            
            value = float(input('Insira o valor que deseja depositar:'))

            if value > 0 and value <= Cliente.get_balance() and value <= Banco.Limit:
                Cliente.update_balance('decrease',value)
                Cliente.list_history(type='Saque',value=value)
                Cliente.User['accounts'][Cliente.account_id]['number_withdrawal'] += 1
                print(f"Você sacou R${value}! Saldo atual: R${Cliente.get_balance()}\n")
            else:
                print("\nValor inválido ou insuficiente!")

        
    def main():
        
        print("\n"+"*" * 40,)
        print("\n     Bem-vindo ao Python Bank\n")
        print("     ESCOLHA UMA OPÇÃO PARA CONTINUAR:")
        print("     [1] REGISTRAR [2] LOGAR \n")
        print("*" * 40, end="\n\n")
        
        action = None
        exit_loop = False

        while True: 

            if action:
                print("\n"+"*" * 40,)
                print("\n     ESCOLHA UMA OPÇÃO PARA CONTINUAR:")
                print("     [1] REGISTRAR [2] LOGAR \n")
                print("*" * 40, end="\n\n")

            action = input("Digite uma opção para prosseguir:")

            if action == "1":
                Cliente.register_user()
            elif action == "2":
                Cliente.check_user()
                
                while True:

                    if exit_loop:
                        exit_loop = False
                        break

                    if Cliente.User:
                        
                        Cliente.get_account()
                        
                        print("\n"+"*" * 40,)
                        print(f"\n     Bem-vindo {Cliente.User['name']}\n")

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
                                Banco.deposit()   
                                continue 
                            if menu_option == "s":
                                Banco.withdrawal()
                            elif menu_option == "e":
                                Cliente.get_history()
                            elif menu_option == "q":
                                Cliente.logout()
                                exit_loop = True
                                break
                            else:
                                print("Opção inválida!")
                    else:
                        Cliente.check_user()
                        continue

Banco.main()