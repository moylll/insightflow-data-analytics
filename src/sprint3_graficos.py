import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

def gerar_graficos():
    print("Gerando gráficos da Sprint 3...")

    # 1. Conecta ao banco de dados (Caminho corrigido!)
    conexao = sqlite3.connect('data/processed/ecommerce.db')
    df_vendas = pd.read_sql_query("SELECT * FROM vendas", conexao)
    df_vendas['Data_Venda'] = pd.to_datetime(df_vendas['Data_Venda'])
    conexao.close()

    # Cria uma pasta para salvar as imagens (Caminho corrigido!)
    os.makedirs('data/processed/graficos', exist_ok=True)

    # 2. Gráfico 1: Receita por Categoria
    df_categoria = df_vendas.groupby('Categoria_Produto')['Valor_Total'].sum().sort_values()
    
    plt.figure(figsize=(10, 6))
    df_categoria.plot(kind='barh', color='skyblue')
    plt.title('Faturamento Total por Categoria (R$)')
    plt.xlabel('Faturamento (R$)')
    plt.ylabel('Categoria')
    plt.tight_layout()
    plt.savefig('data/processed/graficos/faturamento_por_categoria.png') # Caminho corrigido!
    plt.close()
    print("Gráfico de categorias salvo com sucesso!")

    # 3. Gráfico 2: Tendência de Vendas Mensal
    df_vendas['Mes'] = df_vendas['Data_Venda'].dt.to_period('M')
    df_mes = df_vendas.groupby('Mes')['Valor_Total'].sum()
    
    plt.figure(figsize=(10, 6))
    df_mes.plot(kind='line', marker='o', color='coral')
    plt.title('Evolução do Faturamento Mensal')
    plt.xlabel('Mês')
    plt.ylabel('Faturamento (R$)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('data/processed/graficos/tendencia_mensal.png') # Caminho corrigido!
    plt.close()
    print("Gráfico de tendência mensal salvo com sucesso!")

if __name__ == "__main__":
    gerar_graficos()