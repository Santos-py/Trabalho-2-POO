from finances_code.finances import Client, Investment, Account, Transaction, future_value_report, generate_report
from datetime import datetime

cliente = Client('Cauã')
date = datetime(2025, 12, 13, 0, 0, 0)
cliente.add_account('conta inter')
cliente.add_account('conta BB')
cliente.accounts[0].add_transaction(100, 'Depósito', '')
cliente.accounts[1].add_transaction(220, 'Transferência', '')
cliente.add_investment(Investment('CDB', 1000, datetime.now(), 0.01, cliente))
cliente.add_investment(Investment('LCA', 500, datetime.now(), 0.02, cliente))

generate_report(cliente, date)