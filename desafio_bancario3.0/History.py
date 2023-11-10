from datetime import datetime

class History():

    def __init__(self):
        
        self.history = []

    def add_action(self,*,type,value,user,account):

        Date = datetime.now()
        Date_format = "%d/%m/%Y %H:%M:%S"
        if not type in ['Depósito','Saque']:
            print('Tipo inválido')
            return False
        
        self.history = [
            {'date': Date.strftime(Date_format) ,'client': user,'account':account,'type':type,'value':value}
        ]

    def get_history(self,user,account):

        print("EXTRATO".center(50,'='),end='\n\n')

        for entry in self.history:
            if entry['client'] == user and entry['account'] == account:
                print(f'{entry["type"]} de R${entry["value"]} realizado no dia {entry["date"]}')
        print('')
        print("".center(50,'='))

