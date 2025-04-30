import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    cancelaram = df[df['Churn'] == 'Yes']
    permaneceram = df[df['Churn'] == 'No']

    top_ativos = permaneceram.nlargest(5, 'tenure')
    print("Top 5 clientes com contrato ativo há mais tempo:")
    print(top_ativos[['customerID', 'tenure']])

    print('              ')

    top_cancelados = cancelaram.nlargest(5, 'tenure')
    print("Top 5 clientes que cancelaram após maior tempo de fidelidade:")
    print(top_cancelados[['customerID', 'tenure']])
    print('----------------------------------------------------------------------------------------------')