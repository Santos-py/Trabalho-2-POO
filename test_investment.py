from finances_code.finances import Investment, Client, Account, Transaction
from datetime import datetime

DEFAULT_TYPE = 'CDB' 
DEFAULT_INITIAL_AMOUNT = 1000.0
DEFAULT_DATE_PURCHASED = datetime(2023, 12, 13, 0, 0, 0)
DEFAULT_RATE_RETURN = 0.01
DEFAULT_CLIENT = Client('Cauã Santos')
DEFAULT_ACCOUNT = Account('Conta_inicial', 1000.0, [])

def investimento_padrao():
    """Cria objeto Investment com valores padrão"""
    return Investment(DEFAULT_TYPE, DEFAULT_INITIAL_AMOUNT, DEFAULT_DATE_PURCHASED, DEFAULT_RATE_RETURN, DEFAULT_CLIENT)

def test_account_instance():
    """Testa instanciação de investimentos."""
    investimento = investimento_padrao()
    assert isinstance(investimento, Investment), "Falha ao instanciar um objeto Investment"

def test_conta_atributos():
    """Testa os tipos e valores dos atributos"""
    investimento = investimento_padrao()
    # Checa os tipos
    assert type(investimento.type) is str, "Tipo incorreto para o tipo de investimento."
    assert type(investimento.initial_amount) is float, "Tipo incorreto para o valor inicial."
    assert type(investimento.date_purchased) is datetime, "Tipo incorreto para a data de compra."
    assert type(investimento.rate_of_return) is float, "Tipo incorreto para a taxa de retorno."
    assert type(investimento.client) is Client, "Tipo incorreto para o cliente."
    # Checa os valores
    assert investimento.type == DEFAULT_TYPE, "Tipo de investimento incorreto."
    assert investimento.initial_amount == DEFAULT_INITIAL_AMOUNT, "Valor inicial incorreto."
    assert investimento.date_purchased == DEFAULT_DATE_PURCHASED, "Data de compra incorreta."
    assert investimento.rate_of_return == DEFAULT_RATE_RETURN, "Taxa de retorno incorreta."
    assert investimento.client == DEFAULT_CLIENT, "Cliente incorreto."

def test_calculate_value():
    investment =  investimento_padrao()
    assert investment.calculate_value() == 1115

def test_sell():
    investment = investimento_padrao()
    investment.sell(DEFAULT_ACCOUNT)
    assert DEFAULT_ACCOUNT.balance == 2115
