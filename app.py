import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import time

# 1. Configuração de Estilo "Dark Mode Professional"
st.set_page_config(page_title="Portal CPA UniFECAF", layout="wide", initial_sidebar_state="collapsed")

# CSS Customizado para o visual de Startup
st.markdown("""
    <style>
    /* Fundo Escuro e Gradiente */
    .stApp {
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), 
                    url("NOME_DA_SUA_FOTO.jpg"); /* <--- COLOQUE O NOME DO SEU ARQUIVO AQUI */
        background-size: cover;
        background-attachment: fixed;
        color: #F8FAFC;
    }
    /* Estilização dos Cards */
    [data-testid="stMetricValue"] { color: #38BDF8 !important; }
    .stButton>button {
        background-color: #1E293B;
        color: white;
        border-radius: 8px;
        border: 1px solid #38BDF8;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #38BDF8;
        color: #0F172A;
    }
    /* Logo Centralizada e Menor */
    .logo-container { text-align: center; padding-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Conexão com a Planilha (Busca os cursos automaticamente)
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    # Lendo a aba Agrupamento para pegar a lista real de cursos
    df_cursos = conn.read(worksheet="Agrupamento")
    lista_cursos = sorted(df_cursos['Curso'].unique().tolist())
except:
    lista_cursos = ["Erro ao carregar planilha - Verifique os Secrets"]

# 3. Gerenciamento de Navegação (Consertando o botão Sair)
if 'tela' not in st.session_state:
    st.session_state.tela = 'home'
if 'curso' not in st.session_state:
    st.session_state.curso = None

# --- LÓGICA DE TELAS ---

if st.session_state.tela == 'home':
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("NOME_DA_SUA_LOGO.png", width=120) # <--- LOGO MENOR E NOME CORRETO AQUI
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>PORTAL DE GESTÃO CPA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Transformando feedbacks em planos de ação estratégicos.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        curso_selecionado = st.selectbox("Selecione o Curso para Auditoria:", ["Escolha..."] + lista_cursos)
        if curso_selecionado != "Escolha...":
            st.session_state.curso = curso_selecionado
            st.session_state.tela = 'dashboard'
            st.rerun()

elif st.session_state.tela == 'dashboard':
    # Botão Sair que funciona 100%
    if st.sidebar.button("← TROCAR CURSO / SAIR"):
        st.session_state.tela = 'home'
        st.session_state.curso = None
        st.rerun()

    st.title(f"🚀 Dashboard: {st.session_state.curso}")
    st.write(f"Visualizando dados consolidados e respostas subjetivas.")
    
    # Aqui entrarão seus gráficos e o formulário de resposta...
    st.info("Conecte o link da planilha nos Secrets para visualizar os gráficos reais.")
