import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

def treinar_modelo():
    print("Iniciando o treinamento do modelo de previsão...")

    # 1. Puxando os dados
    conexao = sqlite3.connect('data/processed/ecommerce.db')
    df_vendas = pd.read_sql_query("SELECT * FROM vendas", conexao)
    df_vendas['Data_Venda'] = pd.to_datetime(df_vendas['Data_Venda'])
    conexao.close()

    # 2. Preparando os dados (Agrupando faturamento por dia)
    df_dia = df_vendas.groupby(df_vendas['Data_Venda'].dt.date)['Valor_Total'].sum().reset_index()
    df_dia['Data_Venda'] = pd.to_datetime(df_dia['Data_Venda'])
    
    # O modelo de IA gosta de números puros, não de datas formatadas. 
    # Então transformamos as datas em "Dias desde o dia 1"
    df_dia['Dias'] = (df_dia['Data_Venda'] - df_dia['Data_Venda'].min()).dt.days

    # 3. Treinando o Robô
    X = df_dia[['Dias']] # O que ele vai usar para aprender (o passar do tempo)
    y = df_dia['Valor_Total'] # O que ele precisa adivinhar (o dinheiro)

    modelo = LinearRegression()
    modelo.fit(X, y) # É aqui que a mágica do aprendizado acontece!

    # 4. Fazendo a previsão para os próximos 30 dias
    ultimo_dia = df_dia['Dias'].max()
    proximos_dias = np.array([[ultimo_dia + i] for i in range(1, 31)])
    previsao = modelo.predict(proximos_dias)

    # 5. Desenhando o gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(df_dia['Dias'], df_dia['Valor_Total'], color='#A2D2FF', label='Vendas Diárias Reais', alpha=0.6)
    plt.plot(df_dia['Dias'], modelo.predict(X), color='#FFCDB2', linewidth=2, label='Linha de Tendência Atual')
    plt.plot(proximos_dias, previsao, color='#CDB4DB', linestyle='--', linewidth=3, label='Previsão (Próximos 30 dias)')
    
    plt.title('Previsão de Vendas com Machine Learning (Regressão Linear)')
    plt.xlabel('Dias de Operação')
    plt.ylabel('Faturamento (R$)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    
    # Salvando a imagem
    os.makedirs('data/processed/graficos', exist_ok=True)
    plt.savefig('data/processed/graficos/previsao_vendas.png')
    plt.close()

    print("Sucesso! Gráfico de previsão salvo na pasta de gráficos.")

if __name__ == "__main__":
    treinar_modelo()