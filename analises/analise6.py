import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def executar(df):
    df = pd.read_csv('.\datasets\Telecom Customers Churn.csv')

    permaneceram = df[df['Churn'] == 'No']

    eletronic_check = df[df['PaymentMethod'] == 'Electronic check'].shape[0]
    mailed_check = df[df['PaymentMethod'] == 'Mailed check'].shape[0]
    bank_transfer = df[df['PaymentMethod'] == 'Bank transfer (automatic)'].shape[0]
    credit_card = df[df['PaymentMethod'] == 'Credit card (automatic)'].shape[0]

    plt.pie( x=[eletronic_check, mailed_check, bank_transfer, credit_card],
        labels=['Cheque Eletrônico', 'Cheque Tradicional','Transferência Bancária','Cartão de Crédito'],
        autopct='%1.1f%%')
    plt.title('Métodos de pagamento dos clientes ativos')
    plt.axis('equal')   
    plt.show()

    contratos_ativos_pagamentos = permaneceram['PaymentMethod'].value_counts()
    mais_comum_pagamentos = contratos_ativos_pagamentos.idxmax()  
    print("O tipo de pagamento mais comum entre os clientes ativos é: '{}'".format(mais_comum_pagamentos))
    print('----------------------------------------------------------------------------------------------')