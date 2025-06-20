# app resultado de ações
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import timedelta

st.write("""
### App Preços Ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos
""")

@st.cache_data
def carregar_dados(empresas):
    textos_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(textos_tickers)
    cotacoes_acoes = dados_acao.history(period='1d', start='2010-01-01', end='2024-07-01')
    cotacoes_acoes = cotacoes_acoes["Close"]
    return cotacoes_acoes

@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv(r"C:\Users\silvalucasr\OneDrive - CEVA Logistics\Desktop\Python\Python Streamlit\IBOV.csv", sep=";")
    tickers = list(base_tickers["Código"])
    tickers = [item + ".SA" for item in tickers]
    return tickers

acoes = carregar_tickers_acoes()
dados  = carregar_dados(acoes)

#prepara as visualizações
st.sidebar.header("Filtros")

#Filtro de acoes
lista_acoes = st.sidebar.multiselect("Escolha as ações para Visualizar" , dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns = {acao_unica: "Close"})

#Filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_datas = st.sidebar.slider("Escolha o Periodo Desejado", 
                                    min_value=data_inicial, 
                                    max_value=data_final, 
                                    value=(data_inicial,data_final),
                                   step = timedelta(days=15))

dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]

        
grafico = st.line_chart(dados)

texto_perfomance_ativos = ""

if len(lista_acoes) ==0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns = {"Close" : acao_unica})

#Calculo de perfomance - Carteira
carteira = [1000 for acao in lista_acoes]
total_inicial_carteira = sum(carteira)
    
for i, acao in enumerate(lista_acoes):
    perfomance_acao = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    perfomance_acao = float(perfomance_acao)

    carteira[i] = carteira[i] * (1 + perfomance_acao)
    
    
    if perfomance_acao > 0:
        #cor: [texto]
        texto_perfomance_ativos = texto_perfomance_ativos + f"  \n{acao}: :green[{perfomance_acao:.1%}]"
    elif perfomance_acao < 0:
        texto_perfomance_ativos = texto_perfomance_ativos + f"  \n{acao}: :red[{perfomance_acao:.1%}]"
    else:
        texto_perfomance_ativos = texto_perfomance_ativos + f"  \n{acao}: {perfomance_acao:.1%}"

total_final_carteira  = sum(carteira)
perfomance_carteira = total_final_carteira / total_inicial_carteira - 1

if perfomance_carteira > 0:
    #cor: [texto]
    texto_perfomance_carteira = f"Performance da carteira com todos os ativos  :green[{perfomance_carteira:.1%}]"
elif perfomance_carteira < 0:
    texto_perfomance_carteira = f"Performance da carteira com todos os ativos  :red[{perfomance_carteira:.1%}]"
else:
    texto_perfomance_carteira = f"Performance da carteira com todos os ativos  {perfomance_carteira:.1%}"

st.write(f"""
### Performance dos Ativos
Ess foi a performance de cada ativo no periodo selecionado:
{texto_perfomance_ativos}

{texto_perfomance_carteira}
""")


st.write("""
### Fim do app
""")