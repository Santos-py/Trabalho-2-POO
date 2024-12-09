from finances_code.finances import Account, Transaction, Client
from datetime import datetime

DEFAULT_NAME =  "Conta de teste"
DEFAULT_BALANCE = 100.0
DEFAULT_TRANSACTIONS = [Transaction(100.0, "Transferência", "Mudança de uma conta para outra")]
DEFAULT_TRANSACTIONS[0].update(date = datetime(2024, 11, 12, 23,  54, 0))

def conta_padrao():
    """Cria objeto Account com valores padrão"""
    return Account(DEFAULT_NAME, DEFAULT_BALANCE, DEFAULT_TRANSACTIONS)

def test_account_instance():
    """Testa instanciação de contas."""
    conta = conta_padrao()
    assert isinstance(conta, Account), "Falha ao instanciar um objeto Transaction"

def test_conta_atributos():
    """Testa os tipos e valores dos atributos"""
    conta = conta_padrao()
    # Checa os tipos
    assert type(conta.name) is str, "Tipo incorreto para o nome."
    assert type(conta.balance) is float, "Tipo incorreto para o saldo."
    assert type(conta.transactions) is list, "Tipo incorreto para as transações."
    for transaction in conta.transactions:
        assert type(transaction) is Transaction, "Tipo incorreto da transação"
    # Checa os valores
    assert conta.name == DEFAULT_NAME, "Nome incorreto."
    assert conta.balance == DEFAULT_BALANCE, "Saldo incorreto."
    assert conta.transactions == DEFAULT_TRANSACTIONS, "Transações incorretas"

def test_conta_add_transaction():
    """Testa a função add_transaction."""
    conta = conta_padrao()
    assert type(conta.add_transaction(250.0, 'Depósito', 'Colocado em conta poupança')) is Transaction, "Tipo incorreto da transação adicionada."
    assert conta.transactions[1].amount == 250.0
    assert conta.transactions[1].category == 'Depósito'
    assert conta.transactions[1].description == 'Colocado em conta poupança'
    assert conta.balance == 350.0

def test_get_transactions():
    conta = conta_padrao()
    conta.add_transaction(250.0, 'Depósito', 'Colocado em conta poupança')
    conta.transactions[1].update(date=datetime(2024, 11, 13, 12, 34, 0))
    transacoes_antes = conta.get_transactions(end_date=datetime(2024, 11, 12, 0, 0, 0))
    transacoes_meio = conta.get_transactions(start_date=datetime(2024, 11, 12, 0, 0, 0), end_date=datetime(2024, 11, 12, 23, 59, 0))
    assert transacoes_meio == [conta.transactions[0]]
    assert transacoes_antes == []
