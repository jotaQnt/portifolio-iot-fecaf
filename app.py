import streamlit as st
from supabase import create_client, Client
import pandas as pd
import os
from dotenv import load_dotenv
import plotly.express as px

# Carrega variáveis de ambiente
load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# Conecta ao Supabase
supabase: Client = create_client(url, key)

st.title(" Dashboards de Temperatura - Monitoramento de temperatura com IoT")

# Consulta os dados da tabela
data = supabase.table("IOT-temp").select("*").execute()
df = pd.DataFrame(data.data)

# Conversões de data
df["noted_date"] = pd.to_datetime(df["noted_date"], errors='coerce')
df["mes_dt"] = df["noted_date"].dt.to_period("M").dt.to_timestamp()
df["mes"] = df["mes_dt"].dt.strftime("%b %Y")

# 1.Temperatura Média por Mês
st.subheader("Média de Temperatura no Mês")
media_mensal = df.groupby(["mes_dt", "mes"])["temp"].mean().reset_index().sort_values("mes_dt")
fig1 = px.bar(media_mensal, x="mes", y="temp",
              labels={"mes": "Mês", "temp": "Temperatura Média (°C)"},
              title="Temperatura Média no Mês")
st.plotly_chart(fig1, use_container_width=True)

# 2. Temperatura Média Interna vs Externa
st.subheader("Temperatura Média Interna vs Externa")
media_in_out = df.groupby("out_in")["temp"].mean().reset_index()
fig2 = px.bar(media_in_out, x="out_in", y="temp",
              labels={"out_in": "Ambiente", "temp": "Temperatura Média (°C)"},
              color="out_in",
              title="Temperatura Média por Ambiente")
st.plotly_chart(fig2, use_container_width=True)

# 3.  Temperatura Mínima e Máxima por Mês
st.subheader("Temperatura Mínima e Máxima no Mês")
extremos = df.groupby(["mes_dt", "mes"])["temp"].agg(["min", "max"]).reset_index().sort_values("mes_dt")
fig3 = px.bar(extremos, x="mes", y=["min", "max"],
              barmode="group",
              labels={"value": "Temperatura (°C)", "mes": "Mês", "variable": "Extremo"},
              title="Temperatura Mínima e Máxima no Mês")
st.plotly_chart(fig3, use_container_width=True)