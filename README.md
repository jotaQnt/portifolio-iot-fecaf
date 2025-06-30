## Pipeline de Dados com IoT e Docker

Este projeto consiste em um painel interativo desenvolvido com **Streamlit** que consome dados de temperatura de dispositivos **IoT**, armazenados em um banco de dados **PostgreSQL no Supabase**. Ele permite analisar as condições térmicas **internas e externas** de uma sala ao longo do tempo.

---

## Estrutura do Projeto

- app.py # Código principal da aplicação Streamlit

- .env # Contém as variáveis de ambiente (URL e KEY do Supabase)

- requirements.txt # Lista de bibliotecas necessárias

- IOT-temp.csv # Dados originais que foram convertidos e transformados em tabela no Supabase

---

## Configuração do Ambiente

1. **Crie um ambiente virtual**
O projeto foi criado pelo ambiente "Codespaces"

2. **Instale as dependências**
pip install -r requirements.txt

3. Executar o Dashboard Streamlit
Para visualizar os gráficos, execute:

streamlit run app.py

## Dashboards Criados no Streamlit

*Média de Temperatura por Mês*

- Gráfico de barras.

- Permite observar tendências sazonais.

*Temperatura Média Interna vs Externa*

- Gráfico de barras comparando "in" e "out".

- Avalia o isolamento térmico da sala.

*Temperatura Mínima e Máxima por Mês*

- Gráfico de barras agrupadas.

- Identifica extremos térmicos mensais.

**Requisitos e Suas Funções**

streamlit - Framework web para visualizações interativas
pandas - Manipulação e análise dos dados

numpy - Suporte matemático

supabase - Conexão com o banco PostgreSQL do Supabase

matplotlib - Geração de gráficos 

plotly - Criação de gráficos interativos

python-dotenv - Carregamento das variáveis de ambiente do arquivo .env

