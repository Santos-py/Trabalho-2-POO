from finances_code.finances import Investment, Client, Account, Transaction
from datetime import datetime

DEFAULT_NAME = 'Cauã Santos'

def cliente_padrao():
    """Cria objeto Client com valores padrão"""
    return Client(DEFAULT_NAME)

def test_account_instance():
    """Testa instanciação de clientes."""
    cliente = cliente_padrao()
    assert isinstance(cliente, Client), "Falha ao instanciar um objeto Investment"

def test_cliente_atributos():
    """Testa os tipos e valores dos atributos"""
    cliente = cliente_padrao()
    # Checa os tipos
    assert type(cliente.name) is str, "Tipo incorreto para o nome do cliente."
    assert type(cliente.accounts) is list, "Tipo incorreto para as contas do cliente."
    assert type(cliente.investments) is list, "Tipo incorreto para os investimentos do cliente."
    # Checa os valores
    assert cliente.name == DEFAULT_NAME, "Nome do investimento incorreto."
    assert cliente.accounts == [], "Lista de clientes está incorreta."
    assert cliente.investments == [], "Lista de investimentos está incorreta."

def test_add_account():
    """Testa a propriedade add_account."""
    cliente = cliente_padrao()
    cliente.add_account('conta1')
    cliente.add_account('conta2')
    i = 1
    for account in cliente.accounts:
        assert account.name == 'conta' + f'{i}', "Erro nos nomes de novas contas."
        assert account.balance == 0.0, "Erro no saldo das contas novas."
        assert account.transactions == [], "Erro nas transações das contas adicionadas"
        i += 1

def test_add_investment():
    """Testa a propriedade add_investment."""
    cliente = cliente_padrao()
    cliente.add_investment(Investment('CDB', 100.0, datetime(2015, 12, 1, 0, 0, 0), 0.01, cliente))
    cliente.add_investment(Investment('LCI', 250.0, datetime(2020, 4, 12, 0, 0, 0), 0.02, cliente))
    assert cliente.investments[0].type == 'CDB'
    assert cliente.investments[0].date_purchased == datetime(2015, 12, 1, 0, 0, 0)
    assert cliente.investments[1].initial_amount == 250.0
    assert cliente.investments[1].rate_of_return == 0.02
    assert cliente.investments[1].client == cliente

def test_get_net_worth():
    cliente = cliente_padrao()
    investment1 = Investment('LCI', 250.0, datetime(2024, 4, 12, 0, 0, 0), 0.02, cliente)
    investment2 = Investment('CDB', 100.0, datetime(2023, 12, 1, 0, 0, 0), 0.01, cliente)
    cliente.add_account('conta1')
    cliente.add_account('conta2')
    assert cliente.get_net_worth() == 0
    cliente.add_investment(investment1)
    cliente.add_investment(investment2)
    assert cliente.investments[0] == investment1
    assert cliente.investments[1] == investment2
