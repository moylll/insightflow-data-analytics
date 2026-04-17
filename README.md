# InsightFlow - Análise de Dados de E-commerce

Este é o meu projeto final desenvolvido para o programa Desenvolve. O objetivo foi aplicar na prática um pipeline completo de dados, simulando o cenário de um e-commerce com produtos personalizados, passando pela engenharia de dados, análise exploratória e culminando em um modelo preditivo.

## Acesse o Dashboard
[Clique aqui para acessar o painel interativo no Streamlit](https://insightflow-data-analytics-xsxfonkocudt7wmzycfp53.streamlit.app/)

## Ferramentas Utilizadas
* Linguagem: Python
* Banco de Dados: SQLite3
* Manipulação e Limpeza: Pandas e NumPy
* Visualização: Matplotlib e Plotly
* Criação do Dashboard: Streamlit
* Machine Learning: Scikit-Learn (Regressão Linear)

## Storytelling e Insights
Durante a análise dos dados e a construção do dashboard, foi possível identificar os seguintes comportamentos na operação da loja:

1. Destaque de Vendas: A categoria de música foi a principal responsável por impulsionar a receita. Por conter produtos de maior valor agregado, um volume menor de conversões já resulta em um faturamento expressivo.
2. Comportamento de Compra: O ticket médio na casa dos R$ 285 indica um bom nível de confiança dos consumidores, que estão dispostos a gastar valores consistentes a cada carrinho fechado.
3. Fidelização: A taxa de retenção se mostrou bastante alta. Os dados indicam que a loja consegue converter compradores de primeira viagem em clientes recorrentes de forma eficiente.
4. Previsão de Futuro: A aplicação de um modelo de Regressão Linear sobre o histórico temporal gerou uma linha de tendência estável. Isso sugere que o negócio possui uma base sólida e um faturamento constante e seguro projetado para os próximos 30 dias.

## Estrutura do Repositório
* `data/`: Armazena o banco de dados final processado e as imagens dos gráficos estáticos gerados durante a análise.
* `notebooks/`: Contém os arquivos do Jupyter com as análises exploratórias (EDA) detalhadas passo a passo.
* `src/`: Reúne os scripts em Python responsáveis pela extração dos dados, pelo dashboard web e pelo modelo preditivo.