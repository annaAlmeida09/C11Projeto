import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    permaneceram = df[df['Churn'] == 'No']

    internet_ativos = permaneceram['InternetService']
    dsl = (internet_ativos == 'DSL').sum()
    fiber = (internet_ativos == 'Fiber optic').sum()
    sem_internet = (internet_ativos == 'No').sum()

    print('Clientes sem internet:', sem_internet, 'clientes.')
    print('Clientes que usam fibra ótica:', fiber, 'clientes.')
    print('Clientes que usam DSL:', dsl, 'clientes.')

    categorias_internet = ['DSL', 'Fibra Ótica', 'Sem Internet']
    valores = [dsl, fiber, sem_internet]

    plt.bar(categorias_internet, valores, color='skyblue')
    plt.title('Tipo de conexão de internet dos clientes ativos')
    plt.ylabel('Quantidade de clientes')
    plt.xlabel('Tipo de conexão')
    plt.show()
    print('----------------------------------------------------------------------------------------------')