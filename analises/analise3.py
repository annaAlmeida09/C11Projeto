import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    cancelaram = df[df['Churn'] == 'Yes']

    generos = cancelaram['gender'].values
    mulher = np.sum(generos == 'Female')
    homem = np.sum(generos == 'Male')

    print('Mulheres que cancelaram: {}'.format(mulher))
    print('Homens que cancelaram: {}'.format(homem))

    print('----------------------------------------------------------------------------------------------')