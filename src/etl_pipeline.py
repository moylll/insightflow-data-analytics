import pandas as pd
import sqlite3
import os

def executar_etl():
    print("Iniciando a faxina dos dados (ETL)...")
    
    # 1. INGESTÃO: Lendo o CSV da pasta certa
    caminho_csv = 'data/raw/ecom_data.csv' 
    
    try:
        df = pd.read_csv(caminho_csv)
        print(f"Dados carregados! Linhas originais: {len(df)}")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique se você moveu o CSV para a pasta data/raw/")
        return

    # 2. TRATAMENTO (Limpeza e Padronização)
    # Removendo valores vazios (nulos) e linhas duplicadas
    df = df.dropna()
    df = df.drop_duplicates()
    
    # Padronizando as colunas para os formatos corretos de data e número
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
    df['Valor_Unitario'] = pd.to_numeric(df['Valor_Unitario'])
    df['Quantidade'] = pd.to_numeric(df['Quantidade'])
    
    # BÔNUS: Criando a coluna de Valor Total (Preço x Quantidade) para ajudar na Análise
    df['Valor_Total'] = df['Valor_Unitario'] * df['Quantidade']

    print(f"Dados limpos e padronizados! Linhas finais: {len(df)}")

    # 3. CARGA (Salvando no SQLite)
    os.makedirs('data/processed', exist_ok=True)
    caminho_bd = 'data/processed/ecommerce.db'
    
    # Cria a conexão com o banco e salva a tabela lá dentro
    conexao = sqlite3.connect(caminho_bd)
    df.to_sql('vendas', conexao, if_exists='replace', index=False)
    conexao.close()
    
    print(f"Sucesso! Banco de dados salvo em: {caminho_bd}")

if __name__ == "__main__":
    executar_etl()