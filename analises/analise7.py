import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):

    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

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