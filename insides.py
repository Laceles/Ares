import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title='Ares')
with st.container():
    st.title('Ares')
    st.subheader('Ferramenta de operação em ciência de dados')
    st.write('Aplique os dados necessário para desenvolver o seu modelo.')
    st.write('Quem sou eu? [Clique aqui](https://www.linkedin.com/in/rodolfo-lima-datascientist/)')
    
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #333333; /* Substitua pela cor desejada */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header('Escolha seus parâmetros')
classe = st.sidebar.text_input('Digite a categoria do parâmetro')
st.write('Categoria: ', classe)

def get_data_user():
    parametro_1=st.sidebar.slider('parametro_1',0, 100, 90 )
    parametro_2=st.sidebar.slider('parametro_2',0, 100, 80 )
    parametro_3=st.sidebar.slider('parametro_3',0, 100, 70 )
    parametro_4=st.sidebar.slider('parametro_4',0, 100, 60 )
    parametro_5=st.sidebar.slider('parametro_5',0, 100, 50 )
    user_data = {'parametro_1': parametro_1,
                 'parametro_2': parametro_2,
                 'parametro_3': parametro_3,
                 'parametro_4': parametro_4,
                 'parametro_5': parametro_5}
    features = pd.DataFrame(user_data,index=[0])
    return features

user_input_variable=get_data_user()
    

graf = st.bar_chart(user_input_variable)

# @st.cache_data   
# def carregar_dados():
#     tabela = pd.read_csv('csv.csv')
#     return tabela

# with st.container:
#     st.write('---')
#     qtd_dias = st.selectbox("selecione o período de dias", ["7 dias","15 dias", "21 dias", "30 dias"])
#     num_dias = int(qtd_dias.replace("D",""))
#     dados = carregar_dados()
#     dados = dados[-num_dias:]    
#     st.area_chart(dados,x='Datas', y='contratos')