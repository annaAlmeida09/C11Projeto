import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

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