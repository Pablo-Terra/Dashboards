import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# --- Título ---
st.title("📊 Dashboard de Contabilidade")

# --- Carregamento dos dados ---
df = pd.read_csv("contabilidade.csv", parse_dates=["Data"])

# --- Filtros ---
st.sidebar.header("Filtros")
tipo_filtro = st.sidebar.multiselect("Tipo", df["Tipo"].unique(), default=df["Tipo"].unique())
data_inicio = st.sidebar.date_input("Data Inicial", df["Data"].min())
data_fim = st.sidebar.date_input("Data Final", df["Data"].max())

# --- Filtragem ---
df_filtrado = df[
    (df["Tipo"].isin(tipo_filtro)) &
    (df["Data"] >= pd.to_datetime(data_inicio)) &
    (df["Data"] <= pd.to_datetime(data_fim))
]

# --- KPIs ---
receitas = df_filtrado[df_filtrado["Tipo"] == "Receita"]["Valor"].sum()
despesas = df_filtrado[df_filtrado["Tipo"] == "Despesa"]["Valor"].sum()
saldo = receitas - despesas

col1, col2, col3 = st.columns(3)
col1.metric("Receitas", f"R$ {receitas:,.2f}")
col2.metric("Despesas", f"R$ {despesas:,.2f}")
col3.metric("Saldo", f"R$ {saldo:,.2f}", delta=f"R$ {saldo:,.2f}")

# --- Gráfico de linha (evolução) ---
st.subheader("📈 Evolução Diária")
df_diario = df_filtrado.groupby(["Data", "Tipo"])["Valor"].sum().unstack().fillna(0)
st.line_chart(df_diario)

# --- Gráfico de pizza ---
st.subheader("📊 Distribuição por Conta")
df_contas = df_filtrado.groupby("Conta")["Valor"].sum().sort_values(ascending=False)
fig, ax = plt.subplots()
ax.pie(df_contas, labels=df_contas.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# --- Tabela de detalhes ---
st.subheader("📄 Detalhes das Transações")
st.dataframe(df_filtrado.sort_values("Data", ascending=False))
