import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import time

# 1. Configuração de Estilo
st.set_page_config(page_title="Portal CPA UniFECAF", layout="wide", initial_sidebar_state="collapsed")

# Link da sua foto no GitHub para o fundo (Ajustado para o seu repositório)
foto_fundo = "https://raw.githubusercontent.com/Yago-Brito/cpa-unifecaf-portal/main/fundo.jpg"

# CSS Unificado - Modo Startup Dark
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), 
                    url("{foto_fundo}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #F8FAFC;
    }}
    [data-testid="stMetricValue"] {{ color: #38BDF8 !important; }}
    .stButton>button {{
        background-color: #1E293B;
        color: white;
        border-radius: 8px;
        border: 1px solid #38BDF8;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #38BDF8;
        color: #0F172A;
    }}
    .logo-container {{ text-align: center; padding-bottom: 20px; }}
    h1 {{ text-shadow: 2px 2px 4px #000000; }}
    </style>
    """, unsafe_allow_html=True)

# 2. Conexão com a Planilha
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df_cursos = conn.read(worksheet="Agrupamento")
    lista_cursos = sorted(df_cursos['Curso'].unique().tolist())
except:
    lista_cursos = ["Aguardando conexão com a planilha..."]

# 3. Gerenciamento de Navegação
if 'tela' not in st.session_state:
    st.session_state.tela = 'home'
if 'curso' not in st.session_state:
    st.session_state.curso = None

# --- TELAS ---

if st.session_state.tela == 'home':
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    # Tenta carregar a logo, se não existir mostra apenas o texto
    try:
        st.image("logo.png", width=100)
    except:
        st.subheader("UniFECAF")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>PORTAL DE GESTÃO CPA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Transformando feedbacks em planos de ação estratégicos.</p>", unsafe_allow_html=True)
    
    st.write("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        curso_selecionado = st.selectbox("Selecione o Curso para Auditoria:", ["Escolha..."] + lista_cursos)
        if curso_selecionado != "Escolha...":
            st.session_state.curso = curso_selecionado
            st.session_state.tela = 'dashboard'
            st.rerun()

elif st.session_state.tela == 'dashboard':
    if st.sidebar.button("← TROCAR CURSO / SAIR"):
        st.session_state.tela = 'home'
        st.session_state.curso = None
        st.rerun()

    st.title(f"🚀 Dashboard: {st.session_state.curso}")
    st.info("💡 Carregando dados da planilha... Configure os Secrets para visualizar os gráficos.")
