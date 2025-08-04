import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import json
import os

from semantic_engine import SemanticEngine
from document_processor import DocumentProcessor
from utils import *

# Configuração da página
st.set_page_config(
    page_title="MatchSense AI - Busca Semântica de Vagas",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização do motor semântico
@st.cache_resource
def load_semantic_engine():
    """Carrega o motor semântico uma única vez"""
    return SemanticEngine()

# Inicialização do processador de documentos
@st.cache_resource
def load_document_processor():
    """Carrega o processador de documentos uma única vez"""
    return DocumentProcessor()

def main():
    # Título principal
    st.title("🎯 MatchSense AI - Busca Semântica de Vagas")
    st.markdown("### Sistema Inteligente de Compatibilidade entre Currículos e Vagas")
    
    # Sidebar para navegação
    st.sidebar.title("📋 Menu")
    page = st.sidebar.selectbox(
        "Escolha uma opção:",
        ["🏠 Dashboard", "📄 Upload de Documentos", "🔍 Análise Semântica", "📊 Comparação de Candidatos", "📈 Resultados", "⚙️ Configurações"]
    )
    
    # Carregar recursos
    semantic_engine = load_semantic_engine()
    doc_processor = load_document_processor()
    
    if page == "🏠 Dashboard":
        show_dashboard()
    elif page == "📄 Upload de Documentos":
        show_upload_page(semantic_engine, doc_processor)
    elif page == "🔍 Análise Semântica":
        show_analysis_page(semantic_engine)
    elif page == "📊 Comparação de Candidatos":
        show_comparison_page(semantic_engine, doc_processor)
    elif page == "📈 Resultados":
        show_results_page()
    elif page == "⚙️ Configurações":
        show_settings_page(semantic_engine)

def show_dashboard():
    """Página principal do dashboard"""
    st.header("📊 Dashboard de Análise Semântica")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Currículos Processados",
            value="0",
            delta="+0"
        )
    
    with col2:
        st.metric(
            label="Vagas Analisadas",
            value="0",
            delta="+0"
        )
    
    with col3:
        st.metric(
            label="Matches Encontrados",
            value="0",
            delta="+0"
        )
    
    with col4:
        st.metric(
            label="Score Médio",
            value="0%",
            delta="0%"
        )
    
    # Gráficos de exemplo
    st.subheader("📈 Estatísticas de Compatibilidade")
    
    # Dados de exemplo para demonstração
    scores = np.random.normal(75, 15, 100)
    scores = np.clip(scores, 0, 100)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Histograma de scores
        fig_hist = px.histogram(
            x=scores,
            nbins=20,
            title="Distribuição de Scores de Compatibilidade",
            labels={'x': 'Score (%)', 'y': 'Frequência'}
        )
        fig_hist.update_layout(showlegend=False)
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Gráfico de pizza por categoria
        categories = ['Alto (80-100%)', 'Médio (60-79%)', 'Baixo (40-59%)', 'Muito Baixo (0-39%)']
        values = [
            len(scores[scores >= 80]),
            len(scores[(scores >= 60) & (scores < 80)]),
            len(scores[(scores >= 40) & (scores < 60)]),
            len(scores[scores < 40])
        ]
        
        fig_pie = px.pie(
            values=values,
            names=categories,
            title="Distribuição por Categoria de Compatibilidade"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Últimas análises
    st.subheader("🕒 Últimas Análises Realizadas")
    
    # Tabela de exemplo
    data = {
        'Data': ['2024-01-15', '2024-01-14', '2024-01-13'],
        'Currículo': ['João Silva.pdf', 'Maria Santos.pdf', 'Pedro Costa.pdf'],
        'Vaga': ['Desenvolvedor Full Stack', 'Analista de Dados', 'UX Designer'],
        'Score': ['85%', '72%', '68%'],
        'Status': ['✅ Match', '⚠️ Parcial', '❌ Não Match']
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def show_upload_page(semantic_engine, doc_processor):
    """Página de upload de documentos"""
    st.header("📄 Upload de Documentos")
    
    # Tabs para diferentes tipos de upload
    tab1, tab2, tab3 = st.tabs(["📋 Currículo", "💼 Descrição de Vaga", "📁 Upload em Lote"])
    
    with tab1:
        st.subheader("Upload de Currículo")
        
        uploaded_resume = st.file_uploader(
            "Selecione o arquivo do currículo:",
            type=['pdf', 'docx', 'txt'],
            help="Formatos suportados: PDF, DOCX, TXT"
        )
        
        if uploaded_resume is not None:
            with st.spinner("Processando currículo..."):
                try:
                    # Processar o documento
                    resume_text = doc_processor.extract_text(uploaded_resume)
                    
                    # Extrair informações estruturadas
                    resume_data = doc_processor.extract_resume_info(resume_text)
                    
                    st.success("✅ Currículo processado com sucesso!")
                    
                    # Mostrar informações extraídas
                    with st.expander("📋 Informações Extraídas do Currículo"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write("**Informações Pessoais:**")
                            st.write(f"- Nome: {resume_data.get('name', 'Não identificado')}")
                            st.write(f"- Email: {resume_data.get('email', 'Não identificado')}")
                            st.write(f"- Telefone: {resume_data.get('phone', 'Não identificado')}")
                        
                        with col2:
                            st.write("**Resumo:**")
                            st.write(f"- Experiência: {resume_data.get('experience_years', 'Não identificado')} anos")
                            st.write(f"- Educação: {resume_data.get('education', 'Não identificado')}")
                            st.write(f"- Skills: {', '.join(resume_data.get('skills', []))}")
                    
                    # Salvar no session state
                    st.session_state['current_resume'] = {
                        'text': resume_text,
                        'data': resume_data,
                        'filename': uploaded_resume.name
                    }
                    
                except Exception as e:
                    st.error(f"❌ Erro ao processar currículo: {str(e)}")
    
    with tab2:
        st.subheader("Descrição de Vaga")
        
        # Input para título da vaga
        job_title = st.text_input("Título da Vaga:", placeholder="Ex: Desenvolvedor Full Stack")
        
        # Textarea para descrição
        job_description = st.text_area(
            "Descrição da Vaga:",
            height=300,
            placeholder="Cole aqui a descrição completa da vaga..."
        )
        
        # Campos adicionais
        col1, col2 = st.columns(2)
        
        with col1:
            required_skills = st.text_input(
                "Skills Obrigatórias:",
                placeholder="Ex: Python, React, SQL"
            )
            experience_level = st.selectbox(
                "Nível de Experiência:",
                ["Júnior", "Pleno", "Sênior", "Especialista"]
            )
        
        with col2:
            salary_range = st.text_input(
                "Faixa Salarial:",
                placeholder="Ex: R$ 5.000 - R$ 8.000"
            )
            work_model = st.selectbox(
                "Modelo de Trabalho:",
                ["Presencial", "Híbrido", "Remoto"]
            )
        
        if st.button("💾 Salvar Vaga", type="primary"):
            if job_title and job_description:
                job_data = {
                    'title': job_title,
                    'description': job_description,
                    'required_skills': required_skills.split(',') if required_skills else [],
                    'experience_level': experience_level,
                    'salary_range': salary_range,
                    'work_model': work_model,
                    'created_at': datetime.now().isoformat()
                }
                
                st.session_state['current_job'] = job_data
                st.success("✅ Vaga salva com sucesso!")
            else:
                st.warning("⚠️ Preencha pelo menos o título e descrição da vaga.")
    
    with tab3:
        st.subheader("Upload em Lote")
        
        uploaded_files = st.file_uploader(
            "Selecione múltiplos arquivos:",
            type=['pdf', 'docx', 'txt'],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            st.write(f"📁 {len(uploaded_files)} arquivos selecionados")
            
            if st.button("🔄 Processar Todos", type="primary"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                processed_files = []
                
                for i, file in enumerate(uploaded_files):
                    status_text.text(f"Processando {file.name}...")
                    
                    try:
                        text = doc_processor.extract_text(file)
                        data = doc_processor.extract_resume_info(text)
                        
                        processed_files.append({
                            'filename': file.name,
                            'text': text,
                            'data': data
                        })
                        
                    except Exception as e:
                        st.error(f"Erro ao processar {file.name}: {str(e)}")
                    
                    progress_bar.progress((i + 1) / len(uploaded_files))
                
                status_text.text("✅ Processamento concluído!")
                st.session_state['batch_files'] = processed_files
                st.success(f"✅ {len(processed_files)} arquivos processados com sucesso!")

def show_analysis_page(semantic_engine):
    """Página de análise semântica"""
    st.header("🔍 Análise Semântica")
    
    # Verificar se temos dados para análise
    if 'current_resume' not in st.session_state or 'current_job' not in st.session_state:
        st.warning("⚠️ Faça upload de um currículo e uma vaga primeiro!")
        return
    
    resume_data = st.session_state['current_resume']
    job_data = st.session_state['current_job']
    
    # Mostrar informações dos documentos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Currículo")
        st.write(f"**Arquivo:** {resume_data['filename']}")
        st.write(f"**Nome:** {resume_data['data'].get('name', 'Não identificado')}")
        
        with st.expander("Ver texto completo"):
            st.text_area("Texto do currículo:", resume_data['text'], height=200, disabled=True)
    
    with col2:
        st.subheader("💼 Vaga")
        st.write(f"**Título:** {job_data['title']}")
        st.write(f"**Nível:** {job_data['experience_level']}")
        st.write(f"**Modelo:** {job_data['work_model']}")
        
        with st.expander("Ver descrição completa"):
            st.text_area("Descrição da vaga:", job_data['description'], height=200, disabled=True)
    
    # Botão para iniciar análise
    if st.button("🚀 Iniciar Análise Semântica", type="primary"):
        with st.spinner("Realizando análise semântica..."):
            try:
                # Realizar análise
                analysis_results = semantic_engine.analyze_compatibility(
                    resume_data['text'],
                    job_data['description']
                )
                
                # Salvar resultados
                st.session_state['analysis_results'] = analysis_results
                
                st.success("✅ Análise concluída!")
                
                # Mostrar resultados principais
                show_analysis_results(analysis_results)
                
            except Exception as e:
                st.error(f"❌ Erro na análise: {str(e)}")

def show_analysis_results(results):
    """Mostra os resultados da análise"""
    st.subheader("📊 Resultados da Análise")
    
    # Score principal
    overall_score = results['overall_score']
    
    # Determinar cor baseada no score
    if overall_score >= 80:
        color = "green"
        status = "🎯 Excelente Match!"
    elif overall_score >= 60:
        color = "orange"
        status = "✅ Bom Match"
    elif overall_score >= 40:
        color = "yellow"
        status = "⚠️ Match Parcial"
    else:
        color = "red"
        status = "❌ Match Baixo"
    
    # Métricas principais
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Score Geral",
            value=f"{overall_score:.1f}%",
            delta=status
        )
    
    with col2:
        st.metric(
            label="Similaridade Semântica",
            value=f"{results['semantic_similarity']:.1f}%"
        )
    
    with col3:
        st.metric(
            label="Compatibilidade de Skills",
            value=f"{results['skills_match']:.1f}%"
        )
    
    # Gráfico de radar
    st.subheader("📈 Análise Detalhada")
    
    categories = ['Semântica', 'Skills', 'Experiência', 'Educação', 'Soft Skills']
    values = [
        results['semantic_similarity'],
        results['skills_match'],
        results['experience_match'],
        results['education_match'],
        results['soft_skills_match']
    ]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Compatibilidade',
        line_color='rgb(32, 201, 151)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        title="Perfil de Compatibilidade"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detalhes da análise
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Pontos Fortes")
        strengths = results.get('strengths', [])
        for strength in strengths:
            st.write(f"✅ {strength}")
    
    with col2:
        st.subheader("⚠️ Pontos de Atenção")
        weaknesses = results.get('weaknesses', [])
        for weakness in weaknesses:
            st.write(f"⚠️ {weakness}")
    
    # Recomendações
    st.subheader("💡 Recomendações")
    recommendations = results.get('recommendations', [])
    for i, rec in enumerate(recommendations, 1):
        st.write(f"{i}. {rec}")

def show_comparison_page(semantic_engine, doc_processor):
    """Página de comparação de candidatos"""
    st.header("📊 Comparação de Candidatos")
    st.markdown("### Compare múltiplos currículos contra uma vaga")
    
    # Seção 1: Upload da Vaga
    st.subheader("📋 Descrição da Vaga")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        job_description = st.text_area(
            "Cole aqui a descrição da vaga:",
            height=200,
            placeholder="Ex: Desenvolvedor Full Stack Senior com experiência em Python, React, AWS...",
            key="job_desc_comparison"
        )
    
    with col2:
        st.markdown("**📊 Estatísticas da Descrição**")
        if job_description:
            words = len(job_description.split())
            chars = len(job_description)
            st.write(f"Palavras: {words}")
            st.write(f"Caracteres: {chars}")
            st.write(f"Adequado para análise: {'✔ Sim' if words > 50 else '❌ Não'}")
        else:
            st.write("Aguardando descrição...")
    
    # Seção 2: Upload de Múltiplos Currículos
    st.subheader("👥 Currículos dos Candidatos")
    
    # Opção 1: Upload de arquivos
    uploaded_files = st.file_uploader(
        "Upload de currículos (PDF, DOCX, TXT)",
        type=['pdf', 'docx', 'txt'],
        accept_multiple_files=True,
        help="Selecione múltiplos arquivos de currículo",
        key="upload_files_comparison"
    )
    
    # Opção 2: Input manual
    st.markdown("**Ou adicione currículos manualmente:**")
    
    num_manual_resumes = st.number_input(
        "Número de currículos para adicionar manualmente:",
        min_value=1,
        max_value=10,
        value=3,
        key="num_manual_resumes"
    )
    
    manual_resumes = []
    for i in range(num_manual_resumes):
        with st.expander(f"Currículo {i+1}"):
            resume_text = st.text_area(
                f"Cole o currículo {i+1}:",
                height=150,
                key=f"resume_{i}_comparison"
            )
            candidate_name = st.text_input(
                f"Nome do candidato {i+1}:",
                value=f"Candidato {i+1}",
                key=f"name_{i}_comparison"
            )
            if resume_text and candidate_name:
                manual_resumes.append({
                    'name': candidate_name,
                    'text': resume_text
                })
    
    # Seção 3: Configurações da Análise
    st.subheader("⚙️ Configurações da Análise Inteligente")
    
    col1, col2 = st.columns(2)
    
    with col1:
        semantic_weight = st.slider(
            "Peso Análise Semântica",
            min_value=0.0,
            max_value=1.0,
            value=0.8,
            step=0.05,
            help="Peso da análise semântica no score final",
            key="semantic_weight_comparison"
        )
    
    with col2:
        show_explanations = st.checkbox(
            "Mostrar Explicações",
            value=True,
            help="Exibe explicações detalhadas dos resultados",
            key="show_explanations"
        )
    
    # Botão de análise
    if st.button("🚀 Analisar com Inteligência Artificial", type="primary", key="analyze_comparison"):
        if job_description and (uploaded_files or manual_resumes):
            with st.spinner("🔍 Analisando candidatos..."):
                # Processar currículos
                all_resumes = []
                
                # Processar arquivos uploadados
                for uploaded_file in uploaded_files:
                    try:
                        resume_text = doc_processor.extract_text(uploaded_file)
                        resume_info = doc_processor.extract_resume_info(resume_text)
                        candidate_name = resume_info.get('name', uploaded_file.name)
                        all_resumes.append({
                            'name': candidate_name,
                            'text': resume_text,
                            'file': uploaded_file.name
                        })
                    except Exception as e:
                        st.error(f"Erro ao processar {uploaded_file.name}: {str(e)}")
                
                # Adicionar currículos manuais
                all_resumes.extend(manual_resumes)
                
                # Realizar análises
                results = []
                for resume in all_resumes:
                    try:
                        analysis = semantic_engine.analyze_compatibility(
                            resume['text'], 
                            job_description,
                            "Senior"
                        )
                        results.append({
                            'candidate': resume['name'],
                            'analysis': analysis,
                            'resume_text': resume['text']
                        })
                    except Exception as e:
                        st.error(f"Erro na análise de {resume['name']}: {str(e)}")
                
                # Salvar resultados na sessão
                st.session_state.comparison_results = results
                st.session_state.job_description = job_description
                st.session_state.comparison_show_explanations = show_explanations
                
                st.success(f"✅ Análise concluída para {len(results)} candidatos!")
                st.rerun()
        else:
            st.error("❌ Por favor, adicione uma descrição de vaga e pelo menos um currículo.")
    
    # Exibir resultados se disponíveis
    if 'comparison_results' in st.session_state and st.session_state.comparison_results:
        show_explanations_value = st.session_state.get('comparison_show_explanations', True)
        show_comparison_results(st.session_state.comparison_results, st.session_state.job_description, show_explanations_value)

def show_comparison_results(results, job_description, show_explanations):
    """Exibe os resultados da comparação"""
    st.header("🎯 Resultados da Análise Inteligente")
    
    # Ordenar resultados por score
    sorted_results = sorted(results, key=lambda x: x['analysis']['overall_score'], reverse=True)
    
    # Métricas gerais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Candidatos", len(results))
    
    with col2:
        avg_score = sum(r['analysis']['overall_score'] for r in results) / len(results)
        st.metric("Score Médio", f"{avg_score:.1f}%")
    
    with col3:
        max_score = max(r['analysis']['overall_score'] for r in results)
        st.metric("Melhor Score", f"{max_score:.1f}%")
    
    with col4:
        min_score = min(r['analysis']['overall_score'] for r in results)
        st.metric("Pior Score", f"{min_score:.1f}%")
    
    # Gráfico de ranking
    st.subheader("📊 Ranking de Candidatos")
    
    candidates = [r['candidate'] for r in sorted_results]
    scores = [r['analysis']['overall_score'] for r in sorted_results]
    
    fig = px.bar(
        x=candidates,
        y=scores,
        title="Score de Compatibilidade por Candidato",
        labels={'x': 'Candidatos', 'y': 'Score (%)'},
        color=scores,
        color_continuous_scale='RdYlGn'
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabela detalhada
    st.subheader("📋 Análise Detalhada")
    
    # Criar DataFrame para a tabela
    data = []
    for result in sorted_results:
        analysis = result['analysis']
        data.append({
            'Candidato': result['candidate'],
            'Score Geral': f"{analysis['overall_score']:.1f}%",
            'Semântica': f"{analysis['semantic_similarity']:.1f}%",
            'Skills': f"{analysis['skills_match']:.1f}%",
            'Experiência': f"{analysis['experience_match']:.1f}%",
            'Educação': f"{analysis['education_match']:.1f}%",
            'Soft Skills': f"{analysis['soft_skills_match']:.1f}%",
            'Categoria': get_score_category(analysis['overall_score'])
        })
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    # Análise individual dos candidatos
    if show_explanations:
        st.subheader("🔍 Análise Individual")
        
        for i, result in enumerate(sorted_results):
            with st.expander(f"📋 {result['candidate']} - Score: {result['analysis']['overall_score']:.1f}%"):
                show_candidate_analysis(result, job_description)

def show_candidate_analysis(result, job_description):
    """Exibe análise detalhada de um candidato"""
    analysis = result['analysis']
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Score principal
        st.subheader("🎯 Score de Compatibilidade")
        
        # Gauge chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = analysis['overall_score'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Score Inteligente"},
            delta = {'reference': 0},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 35], 'color': "lightgray"},
                    {'range': [35, 65], 'color': "yellow"},
                    {'range': [65, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        st.plotly_chart(fig, use_container_width=True)
        
        # Detalhes do score
        st.write(f"**Score Inteligente:** {analysis['overall_score']:.3f}")
        st.write(f"**Percentual:** {analysis['overall_score']:.1f}%")
        st.write(f"**Categoria:** {get_score_category(analysis['overall_score'])}")
    
    with col2:
        # Análise de skills
        st.subheader("🔧 Análise de Skills")
        
        # Extrair skills do currículo e da vaga
        resume_skills = analysis.get('resume_skills', [])
        job_skills = analysis.get('job_skills', [])
        
        # Skills compatíveis
        compatible_skills = [skill for skill in resume_skills if skill.lower() in [js.lower() for js in job_skills]]
        missing_skills = [skill for skill in job_skills if skill.lower() not in [rs.lower() for rs in resume_skills]]
        
        st.write("**✅ Habilidades Compatíveis:**")
        for skill in compatible_skills[:5]:  # Mostrar apenas as primeiras 5
            st.write(f"• {skill}")
        
        st.write("**❌ Habilidades em Falta:**")
        for skill in missing_skills[:5]:  # Mostrar apenas as primeiras 5
            st.write(f"• {skill}")
        
        # Barra de progresso de skills
        skills_match = analysis['skills_match']
        st.write(f"**Match de Skills:** {skills_match:.1f}%")
        st.progress(skills_match / 100)
    
    # Recomendação
    st.subheader("💡 Recomendação")
    
    if analysis['overall_score'] >= 80:
        recommendation = "Excelente candidato. Recomendado para entrevista."
        color = "success"
    elif analysis['overall_score'] >= 60:
        recommendation = "Bom candidato. Considere treinamento para skills em falta."
        color = "info"
    else:
        recommendation = "Candidato com baixa compatibilidade. Avalie outros aspectos."
        color = "warning"
    
    st.info(recommendation)

def get_score_category(score):
    """Retorna a categoria baseada no score"""
    if score >= 80:
        return "Excelente compatibilidade"
    elif score >= 60:
        return "Boa compatibilidade"
    elif score >= 40:
        return "Compatibilidade moderada"
    else:
        return "Baixa compatibilidade"

def show_results_page():
    """Página de resultados históricos"""
    st.header("📊 Histórico de Resultados")
    
    # Aqui você pode implementar a visualização de resultados históricos
    st.info("🔧 Funcionalidade em desenvolvimento - Aqui serão exibidos os resultados históricos das análises.")

def show_settings_page(semantic_engine):
    """Página de configurações"""
    st.header("⚙️ Configurações")
    
    st.subheader("🔧 Configurações do Motor Semântico")
    
    # Configurações do modelo
    model_name = st.selectbox(
        "Modelo de Embedding:",
        ["sentence-transformers/all-MiniLM-L6-v2", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"],
        help="Modelo usado para gerar embeddings"
    )
    
    # Threshold de similaridade
    similarity_threshold = st.slider(
        "Threshold de Similaridade:",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.05,
        help="Valor mínimo para considerar uma correspondência válida"
    )
    
    # Peso dos diferentes fatores
    st.subheader("⚖️ Pesos dos Fatores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        semantic_weight = st.slider("Peso Semântico:", 0.0, 1.0, 0.4, 0.1)
        skills_weight = st.slider("Peso Skills:", 0.0, 1.0, 0.3, 0.1)
        experience_weight = st.slider("Peso Experiência:", 0.0, 1.0, 0.2, 0.1)
    
    with col2:
        education_weight = st.slider("Peso Educação:", 0.0, 1.0, 0.05, 0.05)
        soft_skills_weight = st.slider("Peso Soft Skills:", 0.0, 1.0, 0.05, 0.05)
    
    # Verificar se a soma dos pesos é 1
    total_weight = semantic_weight + skills_weight + experience_weight + education_weight + soft_skills_weight
    
    if abs(total_weight - 1.0) > 0.01:
        st.warning(f"⚠️ A soma dos pesos deve ser 1.0. Atual: {total_weight:.2f}")
    else:
        st.success("✅ Pesos configurados corretamente!")
    
    # Botão para salvar configurações
    if st.button("💾 Salvar Configurações", type="primary"):
        config = {
            'model_name': model_name,
            'similarity_threshold': similarity_threshold,
            'weights': {
                'semantic': semantic_weight,
                'skills': skills_weight,
                'experience': experience_weight,
                'education': education_weight,
                'soft_skills': soft_skills_weight
            }
        }
        
        st.session_state['config'] = config
        st.success("✅ Configurações salvas!")

if __name__ == "__main__":
    main() 