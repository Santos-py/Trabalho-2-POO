from datetime import datetime

CATEGORIES = ["Pagamento", "Depósito", "Transferência"]

class Transaction:
    def __init__(self, amount: float, category: str, description: str = "") -> None:
        '''
        Inicializa um objeto da classe Transaction.
        Args:
            amount (float): Valor da transação;
            category (str): Identificador de uma categoria;
            description (str): Descrição da transação.
        '''

        if category not in CATEGORIES:
            raise ValueError("Categoria inválida.")

        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.description = description

    def update(
            self,
            amount: float | None = None,
            category: str | None = None,
            description: str | None = None,
            date: datetime | None = None,
            ) -> None:
        '''
        Atualiza um ou mais atributos de um objeto Transaction.
        **Args:
            amount (float): Valor da transação;
            category (str): Identificador de uma categoria;
            description (str): Descrição da transação.
            date (datetime): Momento da transação.            
        '''
        if amount is not None:
            self.amount = amount
        if category is not None:
            if category not in CATEGORIES:
                raise ValueError("Categoria inválida.")
            self.category = category
        if description is not None:
            self.description = description
        if date is not None:
            self.date = date

    def __str__(self) -> str:
        '''
        Retorna uma descrição da transação.
        Return:
            Mostra as informações da transação.
        '''
        return f"Transação: {self.description}\n R$ {self.amount:.2f}\n ({self.category})"


class Account:
    def __init__(self, name: str, balance: float, transactions: list[Transaction]) -> None:
        '''
        Inicializa um objeto Account com os atributos "name", "balance" e "transactions".
        Args:
            name (str): Nome da conta;
            balance (float): Saldo da conta;
            transactions (List[Transaction]): Lista de transações na conta, ordenadas por data;
        '''
        self.name = name
        self.balance = balance
        self.transactions = transactions

    def add_transaction(self, amount: float, category: str, description: str) -> Transaction:
        '''
        Cria uma transação na conta e atualiza o saldo da conta.
        Args:
            amount (float): Valor da transação;
            category (str): Identificador de uma categoria;
            description (str): Descrição da transação.
        Return:
            transacao_nova (Transaction): Nova transação a ser adicionada em "transactions".
        '''
        transacao_nova = Transaction(amount, category, description)
        self.balance += amount
        self.transactions.append(transacao_nova)
        return transacao_nova
    
    def get_transactions(
            self,
            start_date: datetime = None,
            end_date: datetime = None, 
            category: str = None
            ) -> list[Transaction]:
        '''
        Gera uma lista de transações ocorridas em um determinado espaço de tempo e de uma determinada categoria.
        Args:
            start_date (datetime): Início do período a ser analisado.
            end_date (datetime): Final do período a ser analisado.
            category (str): Categoria preferencial das transações a serem analisadas.
        Retuen:
            transactions_ordenadas (list(Transaction)): Lista com todas as transações ocorridas no período determinado e pertencentes a categoria escolhida.
        '''
        transactions_ordenadas = []

        for transaction in self.transactions:
            if end_date == None and start_date == None:
                if category != None and transaction.category == category:
                    transactions_ordenadas.append(transaction)
                if category == None:
                    transactions_ordenadas.append(transaction)

            if end_date != None and start_date == None:
                if transaction.date <= end_date:
                    if category != None and transaction.category == category:
                        transactions_ordenadas.append(transaction)
                    if category == None:
                        transactions_ordenadas.append(transaction)

            if end_date == None and start_date != None:
                if transaction.date >= start_date:
                    if category != None and transaction.category == category:
                        transactions_ordenadas.append(transaction)
                    if category == None:
                        transactions_ordenadas.append(transaction)

            if end_date != None and start_date != None:
                if start_date <= transaction.date <= end_date:
                    if category != None and transaction.category == category:
                        transactions_ordenadas.append(transaction)
                    if category == None:
                        transactions_ordenadas.append(transaction)

        transactions_ordenadas.sort(key=lambda transaction: transaction.date)

        return transactions_ordenadas

    def client(Cliente):
        '''Dono da conta'''
        pass


class Investment():
    def __init__(
            self, 
            type: str, 
            initial_amount: float, 
            date_purchased: datetime,
            rate_of_return: float, 
            client = None,
            ) -> None:
        '''
        Inicializa um objeto da classe Investment.
        Args:
            type (str): Identificador de um tipo de investimento;
            initial_amount (float): Valor inicial do investimento;
            date_purchased (datetime): Data da compra do investimento;
            rate_of_return (float): Taxa mensal de retorno (somente aplicada a mês cheio de investimento);
            client (Client): Cliente dono do investimento.
        '''
        self.type = type
        self.initial_amount = initial_amount
        self.date_purchased = date_purchased
        self.rate_of_return = rate_of_return
        self.client = client
    
    def calculate_value(self) -> float:
        '''
        Calcula o valor do investimento (Supondo que ele é aplicado por meio de juros compostos).
        '''
        investment_value = 0
        hoje = datetime.now()
        meses = (hoje.year - self.date_purchased.year) * 12 + (hoje.month - self.date_purchased.month) # Ajusta para considerar apenas meses completos
        if hoje.day < self.date_purchased.day:
            meses -= 1
        investment_value = (self.initial_amount)*((1 + self.rate_of_return)**meses)
        return int(investment_value)
    
    def sell(self, account: Account) -> None:
        '''
        Vende um investimento e deposita na conta.
        Args:
            account (Account): Conta onde será feita o depósito. 
        '''
        account.balance += self.calculate_value()


class Client():
    def __init__(self, name: str) -> None:
        '''
        Inicializa um objeto do tipo Client.
        Args:
            name (str): Nome do cliente.
        '''
        self.name = name
        self.accounts = []
        self.investments = []

    def add_account(self, account_name: str) -> Account:
        '''
        Cria uma conta para o cliente e adiciona a lista de contas.
        Args:
            account_name (str): Nome da conta.
        '''
        conta_nova = Account(account_name, 0, [])
        self.accounts.append(conta_nova)
        return conta_nova
    
    def add_investment(self, investment) -> None:
        '''Adiciona um investimento para o cliente.'''
        self.investments.append(investment)
    
    def get_net_worth(self) -> float:
        '''
        Calcula a soma do valor atual de todas as contas e investimentos do cliente.
        Return:
            (float): Dinheiro total do cliente.
        '''
        valor_total = 0
        for account in self.accounts:
            valor_total += account.balance
        for investment in self.investments:
            valor_total += investment.calculate_value()
        return valor_total

def future_value_report(client: Client, date: datetime) -> None:
    '''
    Calcula a projeção dos ganhos futuros.
    Args:
        client (Client): Cliente cujos ganhos serão analisados.
        date (datetime): Data limite da projeção.
    '''
    for investment in client.investments:
        investment_value = 0
        meses = (date.year - investment.date_purchased.year) * 12 + (date.month - investment.date_purchased.month) # Ajusta para considerar apenas meses completos
        if date.day < investment.date_purchased.day:
            meses -= 1
        investment_value = (investment.initial_amount)*((1 + investment.rate_of_return)**meses)
        print(f'O investimento {investment.type} valerá, até {date}, R${round(investment_value, 2)}.')

def generate_report(client: Client, date:datetime) -> None:
    """
    Gera um relatório completo de um cliente.
    Args:
        client (Client): Cliente cuja conta será analisada
        date (datetime): Data limite para analisarmos seus próximos lucros.
    """
    print(f'Esta conta pertence a {client.name}.')
    print('As contas associadas a esse usuário são:')
    for conta in client.accounts:
        print('')
        print(f'{conta.name}')
        for transaction in conta.get_transactions():
            print(transaction)
    print('')
    print('Os investimentos feitos por esse usuário são:')
    for investment in client.investments:
        print('')
        print(f'Investimento do tipo "{investment.type}", com capital inicial de R${investment.initial_amount}, a uma taxa de {investment.rate_of_return}.')
        print(f'Ele foi aplicado pela primeira vez em {investment.date_purchased}.')
    print('')
    print(f'{future_value_report(client, date)}')
    print('')
    print(f'Juntando os valores em todas as contas e todos os seus investimentos, esse usuário tem R${client.get_net_worth()}.')
