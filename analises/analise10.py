import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    media_mensal = df['MonthlyCharges'].mean()
    print(f'Média mensal paga por cada cliente: R$ {media_mensal:.2f}')
