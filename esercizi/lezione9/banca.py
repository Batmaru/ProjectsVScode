'''Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

'''

class Account:
    def __init__(self, account_id: str, balance: float):
        self.account_id=account_id
        self.balance=balance
    
    def deposit(self, amount: float)->float:
        self.balance= self.balance+amount
        
    def get_balance(self):
        return self.balance
    
class Bank:
    def __init__(self, accounts: dict[str,Account]):
        self.bankdict=accounts
    
    def create_account(self, account_id: str):
        self.account_id=account_id
        if account_id not in self.bankdict:
            self.bankdict[account_id]= Account(account_id,0)
    
    def deposit(self, account_id, amount):
        if account_id  in self.bankdict:
            self.bankdict[account_id]= Account(account_id,amount)

    

    