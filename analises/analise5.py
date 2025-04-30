import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    permaneceram = df[df['Churn'] == 'No']

    contratos_ativos = permaneceram['Contract'].value_counts()
    mais_comum = contratos_ativos.idxmax()  

    print("O tipo de contrato mais comum entre os clientes ativos é: '{}'".format(mais_comum))
    print('----------------------------------------------------------------------------------------------')