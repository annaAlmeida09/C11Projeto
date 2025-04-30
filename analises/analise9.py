import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    open('.\\datasets\\clientes.csv', 'w').close()

    opcoes = {
        '1': 'Partner',
        '2': 'PhoneService',
        '3': 'MultipleLines',
        '4': 'OnlineSecurity',
        '5': 'OnlineBackup',
        '6': 'DeviceProtection',
        '7': 'TechSupport',
        '8': 'StreamingTV',
        '9': 'StreamingMovies',
        '10': 'PaperlessBilling',
        '11': 'Churn'
    }

    print('Escolha uma opção para filtrar clientes com valor "Yes" e salvá-los no arquivo "clientes.csv"')
    for chave, valor in opcoes.items():
        print(f'{chave} - {valor}')

    escolha = input("Digite o número da opção desejada: ")

    if escolha in opcoes:
        coluna = opcoes[escolha]
        clientes_filtrados = df[df[coluna] == 'Yes']
        clientes_filtrados.to_csv('.\datasets\clientes.csv', index=False)
        print("Arquivo 'clientes.csv' salvo com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")
    print('----------------------------------------------------------------------------------------------')