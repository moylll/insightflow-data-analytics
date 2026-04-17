import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Dashboard InsightFlow", layout="wide")
st.title("📊 Dashboard de Vendas - InsightFlow")

@st.cache_data
def carregar_dados():
    conexao = sqlite3.connect('data/processed/ecommerce.db')
    df = pd.read_sql_query("SELECT * FROM vendas", conexao)
    conexao.close()
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
    return df

df_vendas = carregar_dados()
# Corrigindo o erro de digitação no nome do produto
df_vendas['Nome_Produto'] = df_vendas['Nome_Produto'].str.replace('Hextombe', 'Hexatombe')

# --- FILTROS DINÂMICOS (Exigência da Sprint 3) ---
st.sidebar.header("Filtros Dinâmicos")
categorias = ["Todas"] + list(df_vendas['Categoria_Produto'].unique())
categoria_selecionada = st.sidebar.selectbox("Selecione a Categoria", categorias)

# Aplicando o filtro
if categoria_selecionada != "Todas":
    df_filtrado = df_vendas[df_vendas['Categoria_Produto'] == categoria_selecionada]
else:
    df_filtrado = df_vendas

# --- KPIs (Exigência da Sprint 3) ---
st.subheader("Indicadores Principais (KPIs)")
col1, col2, col3 = st.columns(3)

faturamento = df_filtrado['Valor_Total'].sum()
# Cálculo do Ticket Médio
ticket_medio = faturamento / len(df_filtrado) if len(df_filtrado) > 0 else 0

# Cálculo da Taxa de Retenção (Clientes com > 1 compra)
contagem_clientes = df_filtrado['ID_Cliente'].value_counts()
clientes_recorrentes = len(contagem_clientes[contagem_clientes > 1])
total_clientes = len(contagem_clientes)
taxa_retencao = (clientes_recorrentes / total_clientes) * 100 if total_clientes > 0 else 0

col1.metric("Faturamento Total", f"R$ {faturamento:,.2f}")
col2.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
col3.metric("Taxa de Retenção", f"{taxa_retencao:.1f}%")

st.divider()

# --- GRÁFICOS INTERATIVOS ---
col_grafico1, col_grafico2 = st.columns(2)

with col_grafico1:
    st.subheader("Série Temporal (Sazonalidade)")
    df_filtrado['Mes'] = df_filtrado['Data_Venda'].dt.to_period('M').astype(str)
    df_mes = df_filtrado.groupby('Mes')['Valor_Total'].sum().reset_index()
    fig_linha = px.area(df_mes, x='Mes', y='Valor_Total', markers=True,
                    color_discrete_sequence=['#FFCDB2'])
    st.plotly_chart(fig_linha, use_container_width=True)

with col_grafico2:
    st.subheader("Faturamento por Produto")
    df_prod = df_filtrado.groupby('Nome_Produto')['Valor_Total'].sum().reset_index().sort_values('Valor_Total', ascending=True)
    fig_bar = px.bar(df_prod, x='Valor_Total', y='Nome_Produto', orientation='h',
                 color_discrete_sequence=['#FFCDB2'])
    st.plotly_chart(fig_bar, use_container_width=True)