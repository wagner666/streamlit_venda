import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('vendas.xlsx')

# Título do aplicativo
st.title('Análise de Vendas com Gráficos')
st.write('Analista de Dados: Wagner Oliveira Indio do Brasil')
st.write('Bem-vindo à análise interativa de vendas com gráficos.')

# Função para mostrar tabela com número ajustável de linhas
def mostra_tabela(dataframe):
    # Slider para selecionar quantidade de linhas a serem exibidas
    qntd_linhas = st.sidebar.slider(
        'Quantidade de linhas a serem exibidas:',
        min_value=1, max_value=len(dataframe), step=1
    )
    # Exibir a tabela
    st.dataframe(dataframe.head(qntd_linhas))

# Função para exibir gráficos
def mostra_grafico(dataframe, categoria):
    st.write(f"Gráficos para a Loja: **{categoria}**")

    # Gráfico de barras: Total de Vendas por Produto
    fig, ax = plt.subplots()
    dataframe.groupby('Produto')['Quantidade'].sum().plot(kind='bar', ax=ax)
    ax.set_title('Total de Vendas por Produto')
    ax.set_xlabel('Produto')
    ax.set_ylabel('Quantidade')
    st.pyplot(fig)

    # Gráfico de line Total de Loja e Valor Final
    fig, ax = plt.subplots()
    dataframe.groupby('ID Loja')['Valor Final'].sum().plot(kind='line', ax=ax)
    ax.set_title('Total de Vendas por Produto')
    ax.set_xlabel('ID Loja')
    ax.set_ylabel('Valor Final')
    st.pyplot(fig)

    # Gráfico de pizza: Participação por Loja
    fig, ax = plt.subplots()
    dataframe.groupby('ID Loja')['Quantidade'].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_title('Participação de Vendas por Loja')
    st.pyplot(fig)

# Sidebar com opções interativas
if st.sidebar.checkbox('Exibir Tabela e Gráficos'):
    st.sidebar.markdown('### Filtros para a tabela e gráficos')

    # Criar filtro por categoria (ID Loja)
    categorias = list(df['ID Loja'].unique())
    categorias.append('Todas')

    # Selectbox para escolher a categoria
    categoria = st.sidebar.selectbox('Selecione a loja:', options=categorias)

    # Filtrar dados com base na categoria
    if categoria != 'Todas':
        df_filtrado = df[df['ID Loja'] == categoria]
        mostra_tabela(df_filtrado)
        mostra_grafico(df_filtrado, categoria)
    else:
        mostra_tabela(df)
        mostra_grafico(df, "Todas")
else:
    st.write('Marque a opção "Exibir Tabela e Gráficos" na barra lateral para visualizar os dados.')



