from users_data import users,last_insert_id
from History import History

class Cliente():

    User          = False
    User_id       = None
    account_id    = None
    History = History()
    
    def check_user():

        cpf      = input('Informe seu cpf: ')
        password = input('Informe sua senha: ')

        if not cpf in users:
            print("USUÁRIO NÃO ENCONTRADO")
            return False
        elif users[cpf]['password'] != password:
            print("USUÁRIO E SENHA NÃO CONFEREM")
            return False
        
        Cliente.User_id = cpf
        Cliente.User = users[cpf]

        return True
        
    def register_user():

        cpf = input('Informe seu CPF: ')
    
        while not validate_cpf(cpf):
            print('CPF INVÁLIDO')
            cpf = input('Informe seu CPF: ')
        while cpf in users:
            print('CPF JÁ CADASTRADO')
            cpf = input('Informe seu CPF: ')

        name = input('Informe seu nome: ')
        
        while not name:
            print('INSIRA SEU NOME')
            name = input('Informe seu nome: ')

        lastname = input('Informe seu sobrenome: ')

        while not lastname:
            print('INSIRA SEU SOBRENOME')
            lastname = input('Informe seu sobrenome: ')

        account_type= input('\n TIPO DE CONTA \n [1] CORRENTE [2] POUPANÇA \n')
        
        date =  input('Informe sua data de nascimento Ex 00/00/0000: ')

        while not validate_date(date):
            print('DATA INVÁLIDA')
            date =  input('Informe sua data de nascimento Ex 00/00/0000: ')

        while account_type not in ['1','2']:
            print("OPÇÃO INVÁLIDA")
            account_type= input('\n TIPO DE CONTA \n [1] CORRENTE [2] POUPANÇA \n ')

        address= {}        
        
        address['street']  = input("Endereço/rua: ")

        while not address['street']:
            print('INSIRA SUA RUA')
            address['street']  = input("Endereço/rua: ")

        address['number']  = input("Número: ")

        while not address['number']:
            print('INSIRA NÚMERO')    
            address['number']  = input("Número: ")

        address['district']  = input("Bairro: ")

        while not address['district']:
            print('INSIRA SEU BAIRRO')
            address['district']  = input("Bairro: ")

        address['city']  = input("Cidade: ")

        while not address['city']:
            print('INSIRA SUA CIDADE')
            address['district']  = input("CIdade: ")
        
        address['state']  = input("Estado(sigla): ")

        while not address['state']:
            print('INSIRA SEU ESTADO')    
            address['state']  = input("Estado(sigla): ")
        
        password  = input("Insira uma senha: ")

        while not password:
            print('INSIRA UMA SENHA')    
            password  = input("Insira uma senha: ")

        global last_insert_id
        last_insert_id += 1
        
        users.update({cpf:{'accounts': {int(last_insert_id):{ 'account_type': int(account_type), 'balance': 0.0, 'number_withdrawal': 0, 'statement':''}},   
        'name': name, 'lastname': lastname,'date': date,'password': password,'ag': '0001', 'address': f'{address["street"]}, {address["number"]} - {address["district"]} - {address["city"]}/{address["state"]}'}})
        print('Usuário registrado com sucesso!')
        Cliente.User = users[cpf]
        return True
    
    def logout():
        users[Cliente.User_id] = Cliente.User
        Cliente.User_id = None
        Cliente.account_id = None
        Cliente.User = None
        
    def add_account():
        
        if Cliente.User:

            account_type = input('POR FAVOR INSIRA O TIPO DE CONTA QUE DESEJA CRIAR \n TIPO DE CONTA: \n [1] CORRENTE [2] POUPANÇA \n')

            while account_type not in ['1','2']:
                print("OPÇÃO INVÁLIDA")
                account_type= input('\n TIPO DE CONTA \n [1] CORRENTE [2] POUPANÇA \n ')
            
            global last_insert_id
            last_insert_id += 1

            Cliente.User['accounts'].update({int(last_insert_id) : { 'account_type': int(account_type), 'balance': 0.0, 'number_withdrawal': 0, 'statement':''}})
  
    def get_account():

        account_types = {1:'Corrente',2:'Poupança'}

        while not Cliente.account_id:

            print('\nCONTAS REGISTRADAS NESTE USUÁRIO: ')
          
            for account in Cliente.User['accounts'].keys():
                if(int(account)):

                    print(f"CONTA: [{account}] {account_types[Cliente.User['accounts'][account]['account_type']]}",end=' ')
            
            account_id = int(input('\n\n SELECIONE UMA CONTA PARA CONTINUAR OU DIGITE "0" PARA CRIAR UMA NOVA CONTA: '))

            if account_id == 0:
                Cliente.add_account()
                continue
            elif account_id in Cliente.User['accounts']:
                Cliente.account_id = account_id
            else:
                continue

    def update_balance(option,value):

        if option in ['add','decrease']:
            if option == 'add':
                Cliente.User['accounts'][Cliente.account_id]['balance'] += value
            elif option == 'decrease':
                Cliente.User['accounts'][Cliente.account_id]['balance'] -= value
        else:
            return False
        
    def get_balance():
        if Cliente.User:
            return Cliente.User['accounts'][Cliente.account_id]['balance']

    def list_history(*,type,value):
        Cliente.History.add_action(type=type,value=value,user=Cliente.User_id,account=Cliente.account_id)

    def get_history():
        Cliente.History.get_history(user=Cliente.User_id,account=Cliente.account_id)

'''FUNÇÕES DE APOIO'''

def validate_cpf(cpf):
    
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    remainder = 11 - (total % 11)
    if remainder == 10 or remainder == 11:
        remainder = 0
    if remainder != int(cpf[9]):
        return False

    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    remainder = 11 - (total % 11)
    if remainder == 10 or remainder == 11:
        remainder = 0
    if remainder != int(cpf[10]):
        return False

    return True

def validate_date(date):
    
    date = date.split('/')

    if(len(date) < 3):
        return False
    if int(date[0]) > 31 or int(date[0]) < 1:
        return False
    if int(date[1]) > 12 or int(date[0]) < 1:
        return False
    if len(date[2]) < 4:
        return False
    
    return True

