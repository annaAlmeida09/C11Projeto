import pandas as pd
import importlib

df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')  # ajuste conforme o nome correto

analises = {
    '1': 'analise1',
    '2': 'analise2',
    '3': 'analise3',
    '4': 'analise4',
    '5': 'analise5',
    '6': 'analise6',
    '7': 'analise7',
    '8': 'analise8',
    '9': 'analise9',
    '10': 'analise10'
}
print('Seja bem-vindo ao sistema de análise de dados do dataset: "Telecom Custumers Churn".')
print('Uma empresa de telecomunicações está com problemas de desligamentos de contratos e a ideia é encontrar possíveis causas para esses desligamentos.')


print("Menu de Análises:")
print('1 - Porcentagem de clientes que cancelaram e permaneceram.', end ="\n")
print('2 - Total de receita gerada pelos clientes que continuam com contrato ativo.' , end ="\n")
print('3 - Entre os clientes que cancelaram, quantos homens e quantas mulheres.',end ="\n")
print('4 - Clientes com contrato ativo há mais tempo e clientes que cancelaram o contrato após o maior tempo de fidelidade.', end ="\n")
print('5 - Tipo de contrato mais comum entre os clientes ativos.', end ="\n")
print('6 - Método de pagamento preferido dos clientes ativos.', end ="\n")
print('7 - Porcentagem de uso dos serviços adicionais.',end ="\n")
print('8 - Quantidade de planos de internet dos clientes ativos.', end ="\n")
print('9 - Criar um novo dataset baseado em serviços oferecidos pela empresa.', end ="\n")
print('10 - Média mensal paga por todos os clientes que já tiveram contrato com a empresa.', end ="\n")
print('11 - Finaliza.')

i = 0

while(i == 0):
    escolha = input("Escolha uma análise (1 a 10): ")

    if escolha == '11':
        i = -1
   
    if escolha in analises:
        nome_modulo = f"analises.{analises[escolha]}"
        modulo = importlib.import_module(nome_modulo)
        modulo.executar(df)
    else:
        print("Opção inválida.")

