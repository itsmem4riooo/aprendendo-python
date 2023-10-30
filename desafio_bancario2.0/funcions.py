from users_data import users,last_insert_id,WITHDRAWAL_LIMIT,LIMIT

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

def register():
    
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
    
    users.update({cpf:{'accounts': {last_insert_id:{ 'account_type': account_type, 'balance': 0.0, 'number_withdrawal': 0, 'statement':''}},   
 'name': name, 'lastname': lastname,'date': date,'password': password,'ag': '0001', 'address': f'{address["street"]}, {address["number"]} - {address["district"]} - {address["city"]}/{address["state"]}'}})

def login():

    cpf = input('Informe seu cpf: ')
    password = input('Informe sua senha: ')

    if not cpf in users:
        print("USUÁRIO NÃO ENCONTRADO")
        return False
    elif users[cpf]['password'] != password:
        print("USUÁRIO E SENHA NÃO CONFEREM")
        return False
    return users[cpf],cpf

def deposit(value,account,user):
    if value > 0:

        users[user]['accounts'][account]['balance']+= value
        users[user]['accounts'][account]['statement']+= f"Depósido de R${value}\n"
        print(f"Depósito realizado com sucesso! Saldo atual: R${users[user]['accounts'][account]['balance']}")
        return users[user]['accounts'][account]
        
    else:
        print('Valor inválido!')

def withdrawal(*account,user):

    if users[user]['accounts'][account]['number_withdrawal'] == WITHDRAWAL_LIMIT:
        print("Você atingio o número máximo de saques diarios!")
    else:

        print(f"SALDO: R${users[user]['accounts'][account]['balance']} LIMITE DE SAQUE: R${LIMIT}\n SAQUES DISPONÍVEIS: {WITHDRAWAL_LIMIT-users[user]['accounts'][account]['number_withdrawal']}")
        value = float(input("Informe o valor que deseja sacar: "))
        
        if value <= users[user]['accounts'][account]['balance'] and value <= LIMIT:
            users[user]['accounts'][account]['balance']-= value
            users[user]['accounts'][account]['statement']+= f"Saque de R${value}\n"
            users[user]['accounts'][account]['number_withdrawal'] += 1
            print(f"Você sacou R${value}! Saldo atual: R${users[user]['accounts'][account]['balance']}\n")
        else:
            print("\nValor inválido ou insuficiente!")

def extract(account,/,*,user):

    print("EXTRATO".center(50,'='),end='\n\n')
    print("Não houve movimentações na conta".center(50) if not users[user]['accounts'][account]['statement'] else users[user]['accounts'][account]['statement'])
    print()
    print("".center(50,'='))
                                

def add_account():

    print('POR FAVOR EFETUE LOGIN PARA CONTINUAR')
    user,user_id = login()
    if user:
        print("\n"+"*" * 40,)
        print(f"\n     Bem-vindo {user['name']}\n")
        print("*" * 40, end="\n\n")

        account_type = input('POR FAVOR INSIRA O TIPO DE CONTA QUE DESEJA CRIAR \n TIPO DE CONTA: \n [1] CORRENTE [2] POUPANÇA \n')

        while account_type not in ['1','2']:
            print("OPÇÃO INVÁLIDA")
            account_type= input('\n TIPO DE CONTA \n [1] CORRENTE [2] POUPANÇA \n ')
        
        global last_insert_id
        last_insert_id += 1

        users[user_id]['accounts'][last_insert_id] = { 'account_type': account_type, 'balance': 0.0, 'numero_saques': 0, 'statement':''}
