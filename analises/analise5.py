import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    permaneceram = df[df['Churn'] == 'No']

    contratos_ativos = permaneceram['Contract'].value_counts()
    num_contratos_ativos = len(contratos_ativos)
    mais_comum = contratos_ativos.idxmax()  
    
    
    month_to_month = df[df['Contract'] == 'Month-to-month'].shape[0]
    one_year = df[df['Contract'] == 'One year'].shape[0]
    two_year = df[df['Contract'] == 'Two year'].shape[0]
    
    
    plt.pie( x=[month_to_month*100/num_contratos_ativos, one_year*100/num_contratos_ativos, two_year*100/num_contratos_ativos],
        labels=['Por mês', 'Por ano','Por 2 anos'],
        autopct='%1.1f%%')
    plt.title('Contratos dos clientes ativos')
    plt.axis('equal')   
    plt.show()


    print("O tipo de contrato mais comum entre os clientes ativos é: '{}'".format(mais_comum))
    print('----------------------------------------------------------------------------------------------')