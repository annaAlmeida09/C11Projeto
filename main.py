import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('Telecom Customers Churn.csv')

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

print('Mulheres que cancelaram:', mulher)
print('Homens que cancelaram:', homem)
print('----------------------------------------------------------------------------------------------')
# 4
top_ativos = permaneceram.nlargest(5, 'tenure')
print("Top 5 clientes com contrato ativo há mais tempo:")
print(top_ativos[['customerID', 'tenure']])

print('----------------------------------------------------------------------------------------------')
# 4
top_cancelados = cancelaram.nlargest(5, 'tenure')
print("Top 5 clientes que cancelaram após maior tempo de fidelidade:")
print(top_cancelados[['customerID', 'tenure']])
