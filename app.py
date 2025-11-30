import random

import pandas as pd
import streamlit as st
from faker import Faker

fake = Faker("pt_BR")

st.set_page_config(page_title="Gerador de Dados Fakes", page_icon="📊")

st.title("Gerador de Dados Fakes")

area = st.selectbox("Escolha a área para gerar dados:", ["Vendas", "Saúde", "RH"])
qtd = st.slider("Quantas linhas deseja gerar?", min_value=10, max_value=1000, step=10)


def gerar_dados(area, qtd):
    dados = []

    if area == "Vendas":
        produtos = [
            "Camisa",
            "Calça",
            "Tênis",
            "Boné",
            "Jaqueta",
            "Meias",
            "Mochila",
            "Relógio",
        ]
        formas_pagamento = [
            "Cartão de Crédito",
            "Cartão de Débito",
            "Dinheiro",
            "Pix",
            "Boleto",
        ]

        for _ in range(qtd):
            dados.append(
                {
                    "Data": fake.date_this_year(),
                    "Cliente": fake.name(),
                    "Produto": random.choice(produtos),
                    "Quantidade": random.randint(1, 5),
                    "Valor Unitário": round(random.uniform(50, 500), 2),
                    "Pagamento": random.choice(formas_pagamento),
                    "Vendedor": fake.name(),
                }
            )

    elif area == "Saúde":
        especialidades = [
            "Clínico Geral",
            "Cardiologia",
            "Ortopedia",
            "Ginecologia",
            "Dermatologia",
            "Pediatria",
            "Neurologia",
            "Oftalmologia",
        ]
        convenios = [
            "Particular",
            "Plano A",
            "Plano B",
            "Plano Premium",
            "SUS",
        ]

        for _ in range(qtd):
            dados.append(
                {
                    "Data Consulta": fake.date_this_year(),
                    "Paciente": fake.name(),
                    "Idade": random.randint(1, 95),
                    "Especialidade": random.choice(especialidades),
                    "Convênio": random.choice(convenios),
                    "Médico": fake.name(),
                    "Valor": round(random.uniform(100, 800), 2),
                    "Retorno": random.choice(["Sim", "Não"]),
                }
            )

    elif area == "RH":
        cargos = [
            "Assistente",
            "Analista Júnior",
            "Analista Pleno",
            "Analista Sênior",
            "Coordenador",
            "Gerente",
            "Diretor",
            "Estagiário",
        ]
        departamentos = [
            "Financeiro",
            "Comercial",
            "Marketing",
            "TI",
            "RH",
            "Operações",
            "Logística",
        ]

        for _ in range(qtd):
            dados.append(
                {
                    "Funcionário": fake.name(),
                    "Departamento": random.choice(departamentos),
                    "Cargo": random.choice(cargos),
                    "Data Admissão": fake.date_between(
                        start_date="-5y", end_date="today"
                    ),
                    "Salário": round(random.uniform(2000, 20000), 2),
                    "Tipo Contrato": random.choice(
                        ["CLT", "PJ", "Estágio", "Temporário"]
                    ),
                    "Ativo": random.choice(["Sim", "Não"]),
                }
            )

    return pd.DataFrame(dados)


df = gerar_dados(area, qtd)
st.dataframe(df, width="stretch")


@st.cache_data
def convert_df(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


csv = convert_df(df)

# Centraliza o botão
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.download_button(
        label="Baixar CSV",
        data=csv,
        file_name=f"dados_{area.lower()}.csv",
        mime="text/csv",
        use_container_width=True,
    )
