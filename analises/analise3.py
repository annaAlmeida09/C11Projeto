import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    cancelaram = df[df['Churn'] == 'Yes']
    cancelaram_num = len(cancelaram)

    generos = cancelaram['gender'].values
    mulher = np.sum(generos == 'Female')
    homem = np.sum(generos == 'Male')

    print('Mulheres que cancelaram: {}'.format(mulher), 'clientes.')
    print('Homens que cancelaram: {}'.format(homem), 'clientes.')

    labels = ['Mulheres', 'Homens']
    sizes = [mulher*100/cancelaram_num, homem*100/cancelaram_num]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
    plt.title('Porcentagem de Mulheres e Homens que Cancelaram o Contrato')
    plt.axis('equal')
    plt.show()


    print('----------------------------------------------------------------------------------------------')