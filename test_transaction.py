from finances_code.finances import Transaction, CATEGORIES
from datetime import datetime

DEFAULT_AMOUNT = 100.0
DEFAULT_CATEGORY = 'Pagamento'
DEFAULT_DESCRIPTION = "Transação de teste"

def transacao_padrao():
    """Cria objeto Transaction com valores padrão"""
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

def test_transacao_instance():
    """Testa instanciação de transações"""
    trans = transacao_padrao()
    assert isinstance(trans, Transaction), "Falha ao instanciar um objeto Transaction"

def test_transacao_atributos():
    """Testa os tipos e valores dos atributos"""
    trans = transacao_padrao()
    # Checa os tipos
    assert type(trans.amount) is float, "Tipo incorreto para o valor."
    assert type(trans.date) is datetime, "Tipo incorreto para a data."
    assert type(trans.category) is str, "Tipo incorreto para a categoria."
    assert type(trans.description) is str, "Tipo incorreto para a descrição."
    # Checa os valores
    assert trans.amount == DEFAULT_AMOUNT, "Valore incorreto."
    assert trans.category == DEFAULT_CATEGORY, "Categoria incorreta."
    assert trans.description == DEFAULT_DESCRIPTION, "Descrição incorreta"

def test_transaction_update():
    """Checa se o comando update atualiza os atributos."""
    trans = transacao_padrao()
    trans.update(amount=200.0)
    assert trans.amount == 200.0, "Falha ao atualizar o valor."
    new_date = datetime.now()
    trans.update(date=new_date)
    assert trans.date == new_date, "Falha ao atualizar a data."
    trans.update(category='Pagamento')
    assert trans.category == 'Pagamento', "Falha ao atualizar a categoria."
    trans.update(description="Teste")
    assert trans.description == "Teste", "Falha ao atualizar a descrição."

def test_transaction_str():
    """Checa se o comando __str__ tem o retorno formatado correto."""
    trans = transacao_padrao()
    expected = f"Transação: {DEFAULT_DESCRIPTION}\n R$ {DEFAULT_AMOUNT:.2f}\n ({DEFAULT_CATEGORY})"
    assert str(trans) == expected, "Representação fora do formato esperado."
