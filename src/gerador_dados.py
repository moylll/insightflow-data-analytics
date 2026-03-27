import pandas as pd
import random
from datetime import datetime, timedelta
import os

def gerar_dados_ecommerce(num_linhas=5200):
    print(f"Iniciando a fabricação de {num_linhas} vendas...")

    # Catálogo de produtos da loja
    catalogo = {
        'Moletom BTS Tour': {'categoria': 'Vestuário', 'preco': 150.00},
        'Panetone Trufado de Chocolate': {'categoria': 'Alimentos', 'preco': 85.90},
        'Pelúcia Freddy Fazbear': {'categoria': 'Brinquedos', 'preco': 120.50},
        'Box Anne with an E (DVD)': {'categoria': 'Entretenimento', 'preco': 99.90},
        'Álbum Sabrina Carpenter': {'categoria': 'Música', 'preco': 180.00},
        'Mousepad Genshin Impact': {'categoria': 'Acessórios Gamer', 'preco': 45.00},
        'Camiseta Rick and Morty': {'categoria': 'Vestuário', 'preco': 60.00},
        'Livro Ordem Paranormal: Hextombe': {'categoria': 'Livros', 'preco': 75.00},
        'Vinil de Blues Clássico': {'categoria': 'Música', 'preco': 210.00}
    }
    
    nomes_produtos = list(catalogo.keys())
    
    dados = []
    data_inicial = datetime(2025, 1, 1)

    # Gerando as linhas uma por uma
    for i in range(1, num_linhas + 1):
        id_transacao = f"TRX{i:05d}"
        
        # Sorteia uma data aleatória no último ano
        dias_aleatorios = random.randint(0, 365)
        data_venda = data_inicial + timedelta(days=dias_aleatorios)
        
        # Sorteia um cliente (de 1 a 500)
        id_cliente = f"CUST{random.randint(1, 500):03d}"
        
        # Sorteia um produto e pega os detalhes dele
        produto_escolhido = random.choice(nomes_produtos)
        categoria = catalogo[produto_escolhido]['categoria']
        valor_unit = catalogo[produto_escolhido]['preco']
        
        # Quantidade comprada (de 1 a 4)
        quantidade = random.randint(1, 4)
        
        # Adiciona a linha na nossa lista
        dados.append([
            id_transacao, 
            data_venda.strftime('%Y-%m-%d'), 
            id_cliente, 
            produto_escolhido, 
            categoria, 
            valor_unit, 
            quantidade
        ])

    # Transforma a lista em uma tabela do Pandas
    colunas = ['ID_Transacao', 'Data_Venda', 'ID_Cliente', 'Nome_Produto', 'Categoria_Produto', 'Valor_Unitario', 'Quantidade']
    df = pd.DataFrame(dados, columns=colunas)

    # Garante que a pasta data/raw existe antes de salvar
    os.makedirs('../data/raw', exist_ok=True)
    
    # Salva o arquivo CSV
    caminho_arquivo = '../data/raw/ecom_data.csv'
    df.to_csv(caminho_arquivo, index=False)
    
    print(f"Sucesso! Arquivo gerado em: {caminho_arquivo}")

# Executa a função
if __name__ == "__main__":
    gerar_dados_ecommerce()