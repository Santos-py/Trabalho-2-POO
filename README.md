# Sistema financeiro pessoal em Python.

Autor: Cauã Felipe dos Santos Lima.
Objetivo: Trabalho de conclusão do curso de programação orientada a objetos.

_____
O sistema permite que você:


#### Crie e gerencie contas bancárias.
___________________
#### Adicione transações às suas contas, categorizando-as como Pagamento, Depósito ou Transferência.
_______________________________
#### Adicione e monitore investimentos.
_______________________________
#### Gere relatórios completos sobre a saúde financeira do cliente, incluindo:

Extrato bancário detalhado para cada conta.

Informações sobre os investimentos realizados.

Valor atual dos investimentos (considerando juros compostos).

Patrimônio líquido total (soma do saldo de todas as contas e valor dos investimentos).

Projeção de ganhos futuros para os investimentos até uma data específica.

## Classes do Sistema
O sistema é composto pelas seguintes classes principais:

### Transaction: 
Representa uma transação bancária (pagamento, depósito ou transferência).
### Account: 
Representa uma conta bancária do cliente.
### Investment:
Representa um investimento financeiro realizado pelo cliente.
### Client: 
Representa um cliente do sistema.

## Funções do Sistema
O sistema possui as seguintes funções principais:

### future_value_report(client, date):
 Calcula e imprime a projeção de ganhos futuros para todos os investimentos do cliente até a data limite informada.
### generate_report(client, date):
 Gera um relatório completo do cliente, incluindo extratos bancários, informações sobre investimentos, patrimônio líquido e projeção de ganhos futuros.

## Requisitos
Para executar o código, você precisa ter o Python instalado em sua máquina. É recomendável a utilização da versão 3.x.

## Como Utilizar
Clone este repositório.
Abra um terminal ou prompt de comando e navegue até a pasta do projeto.
Execute o código principal usando o comando python script.py (substitua "script.py" pelo nome do arquivo principal do seu sistema, caso seja diferente).
O sistema solicitará informações sobre o cliente e suas contas/investimentos. Forneça os dados necessários para a geração do relatório.

## Exemplo de Saída
O sistema irá gerar um relatório contendo informações como:

    Esta conta pertence a João Silva.
    As contas associadas a esse usuário são:

    Conta Corrente
    Transação: Compra no Supermercado
    R$ 123,45 (Pagamento)
    Transação: Salário
    R$ 5.000,00 (Depósito)

    Poupança
    Transação: Transferência da Conta Corrente
    R$ 1.000,00 (Transferência - Conta Corrente)

    Os investimentos feitos por esse usuário são:

    Investimento do tipo "Fundo de Renda Fixa", com capital inicial de R$ 10.000,00, a uma taxa de 1.0%.
    Ele foi aplicado pela primeira vez em 2023-12-01.

    O investimento Fundo de Renda Fixa valerá, até 2024-12-31, R$10.100.00.

    Juntando os valores em todas as contas e todos os seus investimentos, esse usuário tem R$6.076,55.

## Contribuindo
Sinta-se à vontade para enviar pull requests com melhorias e funcionalidades adicionais para o sistema.

Ademais, para informações epecíficas contate: caual8634@gmail.com ou +55 (82) 9 9673-7935.