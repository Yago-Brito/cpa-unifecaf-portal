import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import time

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(page_title="Portal CPA UniFECAF", layout="wide")

# --- CONEXÃO COM A PLANILHA ---
# Usaremos a conexão nativa do Streamlit com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# --- ESTADO DO SITE (Navegação) ---
if 'tela' not in st.session_state:
    st.session_state.tela = 'home'
if 'curso' not in st.session_state:
    st.session_state.curso = None
if 'limite_comentarios' not in st.session_state:
    st.session_state.limite_comentarios = 10

# --- TELA INICIAL (Landing Page) ---
if st.session_state.tela == 'home':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("SUA_FOTO_DA_FACULDADE_AQUI");
            background-size: cover;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.image("SUA_LOGO_AQUI", width=200)
    st.title("BEM-VINDO AO PORTAL DE MELHORIA CPA")
    st.subheader("A voz do aluno transformando a UniFECAF")
    
    # Lista de cursos (Pode vir da sua aba 'Agrupamento')
    lista_cursos = ["Selecione seu curso...", "Administração", "Direito", "Psicologia", "Engenharia"]
    curso_selecionado = st.selectbox("Escolha o Curso para iniciar o Plano de Ação:", lista_cursos)
    
    if curso_selecionado != "Selecione seu curso...":
        st.session_state.curso = curso_selecionado
        st.session_state.tela = 'dashboard'
        st.rerun()

# --- TELA DE DASHBOARD (Interface de Dados) ---
elif st.session_state.tela == 'dashboard':
    st.sidebar.button("← Sair/Trocar Curso", on_click=lambda: st.session_state.update(tela='home', curso=None))
    st.title(f"📊 Gestão CPA: {st.session_state.curso}")
    
    # 1. Carregar os dados (Simulação de leitura das suas abas)
    # df_subjetiva = conn.read(worksheet="subjetiva")
    # dados_filtrados = df_subjetiva[df_subjetiva['Curso'] == st.session_state.curso]
    
    # 2. KPIs (Exemplo visual)
    col1, col2, col3 = st.columns(3)
    col1.metric("Nota Geral", "8.5", "+0.2")
    col2.metric("Respondentes", "145", "Eixo 2D")
    col3.metric("Status", "Pendente", delta_color="inverse")

    # 3. Respostas Subjetivas com "Carregar Mais"
    st.subheader("💬 O que os alunos disseram:")
    # Aqui simulamos a lista de comentários
    comentarios = [f"Comentário {i} do aluno de {st.session_state.curso}..." for i in range(50)]
    
    for i in range(st.session_state.limite_comentarios):
        if i < len(comentarios):
            st.info(comentarios[i])
            
    if st.session_state.limite_comentarios < len(comentarios):
        if st.button("Ver +10 comentários"):
            st.session_state.limite_comentarios += 10
            st.rerun()

    # 4. FORMULÁRIO DE RESPOSTA DO COORDENADOR
    st.divider()
    st.subheader("📝 Seu Plano de Ação")
    with st.form("form_plano"):
        acao = st.text_area("O que será feito para melhorar este ponto?")
        prazo = st.date_input("Prazo de conclusão")
        responsavel = st.text_input("Responsável pela execução")
        
        if st.form_submit_state("Enviar Plano para a CPA"):
            # LÓGICA PARA SALVAR NA ABA 'resposta_coord'
            # nova_linha = pd.DataFrame([[st.session_state.curso, acao, prazo, responsavel]], columns=['Curso', 'Ação', 'Prazo', 'Responsável'])
            # conn.update(worksheet="resposta_coord", data=nova_linha)
            st.success("Plano enviado com sucesso! A CPA agradece.")
            time.sleep(2)