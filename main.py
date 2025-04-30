import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

# 1
cancelaram = df[df['Churn'] == 'Yes']
permaneceram = df[df['Churn'] == 'No']


cancelados = len(cancelaram)
ativos = len(permaneceram)
total = len(df)
pc = (cancelados / total) * 100
pa = (ativos / total) * 100

print("Total de clientes: {}".format(total))
print("Cancelaram: {:.2f}%".format(pc))
print("Permaneceram: {:.2f}%".format(pa))


plt.pie(x=[ativos, cancelados],labels=['Clientes Ativos', 'Clientes Cancelados'],autopct='%1.1f%%')
plt.title('Porcentagem de Clientes Ativos vs Cancelados')
plt.axis('equal')
plt.show()

print('----------------------------------------------------------------------------------------------')

# 2
receita_ativos = permaneceram['MonthlyCharges'].sum()
receita_cancelados = cancelaram['MonthlyCharges'].sum()
receita_total = df['MonthlyCharges'].sum()
impacto = (receita_cancelados / receita_total) * 100

print("Total de receita gerada pelos clientes ativos: R${:.2f}".format(receita_ativos))
print("Total de receita deixada de arrecadar com os contratos cancelados: R${:.2f}".format(receita_cancelados))
print("O impacto financeiro dos cancelamentos em relação à receita total é: {:.2f}%".format(impacto))

categorias = ['Ativos', 'Cancelados']
valores = [receita_ativos, receita_cancelados]

bars = plt.bar(categorias, valores, color=['green', 'red'])
plt.title('Receita: Clientes Ativos vs Cancelados')
plt.ylabel('Receita em R$')
plt.show()

print('----------------------------------------------------------------------------------------------')

#3
generos = cancelaram['gender'].values
mulher = np.sum(generos == 'Female')
homem = np.sum(generos == 'Male')

print('Mulheres que cancelaram: {}'.format(mulher))
print('Homens que cancelaram: {}'.format(homem))

print('----------------------------------------------------------------------------------------------')

#4
top_ativos = permaneceram.nlargest(5, 'tenure')
print("Top 5 clientes com contrato ativo há mais tempo:")
print(top_ativos[['customerID', 'tenure']])

print('              ')

top_cancelados = cancelaram.nlargest(5, 'tenure')
print("Top 5 clientes que cancelaram após maior tempo de fidelidade:")
print(top_cancelados[['customerID', 'tenure']])
print('----------------------------------------------------------------------------------------------')

#5
contratos_ativos = permaneceram['Contract'].value_counts()
mais_comum = contratos_ativos.idxmax()  

print("O tipo de contrato mais comum entre os clientes ativos é: '{}'".format(mais_comum))
print('----------------------------------------------------------------------------------------------')

#---------------------------------#

#6 Tipo de pagamento favorito entre os clientes ativos.

eletronic_check = df[df['PaymentMethod'] == 'Electronic check'].shape[0]
mailed_check = df[df['PaymentMethod'] == 'Mailed check'].shape[0]
bank_transfer = df[df['PaymentMethod'] == 'Bank transfer (automatic)'].shape[0]
credit_card = df[df['PaymentMethod'] == 'Credit card (automatic)'].shape[0]

plt.pie( x=[eletronic_check, mailed_check, bank_transfer, credit_card],
    labels=['Cheque Eletrônico', 'Cheque Tradicional','Transferência Bancária','Cartão de Crédito'],
    autopct='%1.1f%%')
plt.title('Métodos de pagamento dos clientes ativos')
plt.axis('equal')   
plt.show()

contratos_ativos_pagamentos = permaneceram['PaymentMethod'].value_counts()
mais_comum_pagamentos = contratos_ativos_pagamentos.idxmax()  
print("O tipo de pagamento mais comum entre os clientes ativos é: '{}'".format(mais_comum_pagamentos))
print('----------------------------------------------------------------------------------------------')

#7 Entre os clientes que possuem internet, qual é a média de uso dos serviços adicionais (OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies)? 
internet_possuem = df[df['InternetService'] != 'No']
total = len(internet_possuem)

servicos = {
    'OnlineSecurity': round(float((internet_possuem['OnlineSecurity'] == 'Yes').mean() * 100), 2),
    'OnlineBackup': round(float((internet_possuem['OnlineBackup'] == 'Yes').mean() * 100), 2),
    'DeviceProtection': round(float((internet_possuem['DeviceProtection'] == 'Yes').mean() * 100), 2),
    'TechSupport': round(float((internet_possuem['TechSupport'] == 'Yes').mean() * 100), 2),
    'StreamingTV': round(float((internet_possuem['StreamingTV'] == 'Yes').mean() * 100), 2),
    'StreamingMovies': round(float((internet_possuem['StreamingMovies'] == 'Yes').mean() * 100), 2),
}

print('As porcentagens de uso dos serviços adicionais de clientes que possuem internet são:', servicos)
print('----------------------------------------------------------------------------------------------')

#8 Entre os clientes que não cancelaram o contrato, qual é o tipo de conexão de internet mais utilizado?
# Exiba a quantidade de clientes de cada tipo (DSL, Fiber optic, No), em um gráfico de barras.

internet_ativos = permaneceram['InternetService']
dsl = (internet_ativos == 'DSL').sum()
fiber = (internet_ativos == 'Fiber optic').sum()
sem_internet = (internet_ativos == 'No').sum()

# Prepara os dados para o gráfico
categorias_internet = ['DSL', 'Fibra Ótica', 'Sem Internet']
valores = [dsl, fiber, sem_internet]

# Cria o gráfico de barras
plt.bar(categorias_internet, valores, color='skyblue')
plt.title('Tipo de conexão de internet dos clientes ativos')
plt.ylabel('Quantidade de clientes')
plt.xlabel('Tipo de conexão')
plt.show()

#9 Liste todos os clientes que utilizam múltiplas linhas telefônicas (MultipleLines == 'Yes') e salve essas informações em um novo arquivo chamado clientesMultiplasLinhas.csv.

clientes_multiplas_linhas = df[df['MultipleLines'] == 'Yes']
clientes_multiplas_linhas.to_csv('.\datasets\clientesMultiplasLinhas.csv', index=False)
print("Arquivo 'clientesMultiplasLinhas.csv' salvo com sucesso!")

#10 Qual é a média mensal paga por todos os clientes que já tiveram contrato com a empresa?

media_mensal = df['MonthlyCharges'].mean()
print(f'Média mensal paga por todos os clientes: R$ {media_mensal:.2f}')
