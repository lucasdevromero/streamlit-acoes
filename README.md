# Projeto Streamlit Ações - Visualizador de Preços e Performance

Este projeto é um aplicativo web simples feito com Streamlit que permite visualizar a evolução dos preços das ações do índice IBOV (Ibovespa) ao longo dos anos, além de calcular a performance individual de cada ativo e da carteira como um todo.

## Funcionalidades

- Carregamento dinâmico dos tickers das ações do IBOV a partir de um arquivo CSV.
- Consulta de dados históricos via API do Yahoo Finance (`yfinance`).
- Filtros interativos para selecionar ações específicas e definir o período de análise.
- Visualização gráfica da evolução dos preços.
- Cálculo e exibição da performance percentual de cada ação e da carteira.
- Interface simples e intuitiva feita com Streamlit.

## Como usar

Execute os comandos abaixo no terminal para rodar o projeto:

```bash
git clone https://github.com/lucasdevromero/streamlit-acoes.git
cd streamlit-acoes
pip install -r requirements.txt
streamlit run gabarito_aula1.py
