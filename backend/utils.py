import json
import os
import pandas as pd
from datetime import datetime
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

def save_analysis_results(results: Dict[str, Any], filename: str = None) -> str:
    """
    Salva os resultados da análise em arquivo JSON
    
    Args:
        results: Resultados da análise
        filename: Nome do arquivo (opcional)
        
    Returns:
        Caminho do arquivo salvo
    """
    try:
        # Criar diretório de resultados se não existir
        results_dir = "results"
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        
        # Gerar nome do arquivo se não fornecido
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"analysis_results_{timestamp}.json"
        
        filepath = os.path.join(results_dir, filename)
        
        # Salvar resultados
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Resultados salvos em: {filepath}")
        return filepath
        
    except Exception as e:
        logger.error(f"Erro ao salvar resultados: {str(e)}")
        raise

def load_analysis_results(filepath: str) -> Dict[str, Any]:
    """
    Carrega resultados de análise de arquivo JSON
    
    Args:
        filepath: Caminho do arquivo
        
    Returns:
        Resultados carregados
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            results = json.load(f)
        
        logger.info(f"Resultados carregados de: {filepath}")
        return results
        
    except Exception as e:
        logger.error(f"Erro ao carregar resultados: {str(e)}")
        raise

def export_to_excel(results: List[Dict[str, Any]], filename: str = None) -> str:
    """
    Exporta resultados para arquivo Excel
    
    Args:
        results: Lista de resultados
        filename: Nome do arquivo (opcional)
        
    Returns:
        Caminho do arquivo salvo
    """
    try:
        # Criar diretório de exportação se não existir
        export_dir = "exports"
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        
        # Gerar nome do arquivo se não fornecido
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"analysis_export_{timestamp}.xlsx"
        
        filepath = os.path.join(export_dir, filename)
        
        # Preparar dados para exportação
        export_data = []
        for result in results:
            row = {
                'Filename': result.get('filename', 'N/A'),
                'Overall Score (%)': round(result.get('overall_score', 0), 2),
                'Semantic Similarity (%)': round(result.get('semantic_similarity', 0), 2),
                'Skills Match (%)': round(result.get('skills_match', 0), 2),
                'Experience Match (%)': round(result.get('experience_match', 0), 2),
                'Education Match (%)': round(result.get('education_match', 0), 2),
                'Soft Skills Match (%)': round(result.get('soft_skills_match', 0), 2),
                'Resume Skills': ', '.join(result.get('resume_skills', [])),
                'Job Skills': ', '.join(result.get('job_skills', [])),
                'Strengths': '; '.join(result.get('strengths', [])),
                'Weaknesses': '; '.join(result.get('weaknesses', [])),
                'Recommendations': '; '.join(result.get('recommendations', [])),
                'Analysis Timestamp': result.get('analysis_timestamp', 'N/A')
            }
            export_data.append(row)
        
        # Criar DataFrame e exportar
        df = pd.DataFrame(export_data)
        df.to_excel(filepath, index=False, engine='openpyxl')
        
        logger.info(f"Resultados exportados para: {filepath}")
        return filepath
        
    except Exception as e:
        logger.error(f"Erro ao exportar resultados: {str(e)}")
        raise

def format_score(score: float) -> str:
    """
    Formata score para exibição
    
    Args:
        score: Score numérico
        
    Returns:
        Score formatado
    """
    if score >= 80:
        return f"🎯 {score:.1f}% (Excelente)"
    elif score >= 60:
        return f"✅ {score:.1f}% (Bom)"
    elif score >= 40:
        return f"⚠️ {score:.1f}% (Moderado)"
    else:
        return f"❌ {score:.1f}% (Baixo)"

def get_score_color(score: float) -> str:
    """
    Retorna cor baseada no score
    
    Args:
        score: Score numérico
        
    Returns:
        Código de cor
    """
    if score >= 80:
        return "#28a745"  # Verde
    elif score >= 60:
        return "#ffc107"  # Amarelo
    elif score >= 40:
        return "#fd7e14"  # Laranja
    else:
        return "#dc3545"  # Vermelho

def validate_file_format(filename: str) -> bool:
    """
    Valida formato de arquivo
    
    Args:
        filename: Nome do arquivo
        
    Returns:
        True se formato válido
    """
    allowed_extensions = ['.pdf', '.docx', '.txt']
    return any(filename.lower().endswith(ext) for ext in allowed_extensions)

def get_file_size_mb(file) -> float:
    """
    Obtém tamanho do arquivo em MB
    
    Args:
        file: Arquivo
        
    Returns:
        Tamanho em MB
    """
    try:
        # Salvar posição atual
        current_pos = file.tell()
        
        # Ir para o final para obter tamanho
        file.seek(0, 2)
        size_bytes = file.tell()
        
        # Voltar para posição original
        file.seek(current_pos)
        
        return size_bytes / (1024 * 1024)
        
    except Exception as e:
        logger.error(f"Erro ao obter tamanho do arquivo: {str(e)}")
        return 0.0

def clean_filename(filename: str) -> str:
    """
    Limpa nome de arquivo para uso seguro
    
    Args:
        filename: Nome original
        
    Returns:
        Nome limpo
    """
    # Remover caracteres especiais
    import re
    clean_name = re.sub(r'[^\w\s-]', '', filename)
    
    # Remover espaços extras
    clean_name = re.sub(r'\s+', '_', clean_name)
    
    # Limitar tamanho
    if len(clean_name) > 100:
        clean_name = clean_name[:100]
    
    return clean_name

def create_sample_resume() -> str:
    """
    Cria um currículo de exemplo para testes
    
    Returns:
        Texto do currículo de exemplo
    """
    return """
João Silva Santos
joao.silva@email.com
(11) 99999-9999
São Paulo, SP

RESUMO PROFISSIONAL
Desenvolvedor Full Stack com 5 anos de experiência em desenvolvimento web, especializado em Python, JavaScript e React. Experiência em projetos de e-commerce e aplicações empresariais.

EXPERIÊNCIA PROFISSIONAL

Desenvolvedor Full Stack Sênior
TechCorp - São Paulo, SP
2021 - Presente
• Desenvolvimento de aplicações web usando Python (Django), React e PostgreSQL
• Liderança técnica de equipe de 4 desenvolvedores
• Implementação de arquitetura de microserviços
• Otimização de performance e escalabilidade

Desenvolvedor Full Stack Pleno
StartupXYZ - São Paulo, SP
2019 - 2021
• Desenvolvimento de aplicações React e Node.js
• Integração com APIs REST e GraphQL
• Trabalho com metodologias ágeis (Scrum)

EDUCAÇÃO
Bacharelado em Ciência da Computação
Universidade de São Paulo (USP)
2015 - 2019

HABILIDADES TÉCNICAS
• Linguagens: Python, JavaScript, TypeScript, Java
• Frontend: React, Angular, HTML5, CSS3, Bootstrap
• Backend: Django, Flask, Node.js, Express
• Bancos de Dados: PostgreSQL, MySQL, MongoDB
• Cloud: AWS, Docker, Kubernetes
• Ferramentas: Git, Jira, Jenkins

IDIOMAS
• Português: Nativo
• Inglês: Fluente
• Espanhol: Intermediário

CERTIFICAÇÕES
• AWS Certified Developer Associate
• Scrum Master Certified (SMC)

PROJETOS DESTACADOS
• Sistema de E-commerce com 10k+ usuários
• Plataforma de Gestão Empresarial
• API de Pagamentos Integrada

LINKEDIN: linkedin.com/in/joaosilva
GITHUB: github.com/joaosilva
"""

def create_sample_job_description() -> str:
    """
    Cria uma descrição de vaga de exemplo para testes
    
    Returns:
        Descrição da vaga de exemplo
    """
    return """
DESENVOLVEDOR FULL STACK SENIOR

Sobre a Empresa:
Somos uma empresa de tecnologia inovadora, focada em soluções digitais para o mercado financeiro. Buscamos um desenvolvedor experiente para integrar nossa equipe de desenvolvimento.

Responsabilidades:
• Desenvolver aplicações web escaláveis e de alta performance
• Trabalhar com arquitetura de microserviços
• Liderar projetos técnicos e mentorar desenvolvedores júnior
• Colaborar com equipes de produto e design
• Participar de code reviews e definição de padrões de desenvolvimento

Requisitos Obrigatórios:
• 5+ anos de experiência em desenvolvimento web
• Conhecimento sólido em Python e JavaScript/TypeScript
• Experiência com frameworks React e Django
• Conhecimento em bancos de dados PostgreSQL
• Experiência com AWS e Docker
• Conhecimento em metodologias ágeis

Diferencial:
• Experiência com GraphQL
• Conhecimento em Kubernetes
• Experiência no setor financeiro
• Certificações AWS

Benefícios:
• Salário competitivo
• Plano de saúde
• Vale refeição
• Home office híbrido
• Plano de carreira

Localização: São Paulo, SP
Modelo de Trabalho: Híbrido
"""

def calculate_statistics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calcula estatísticas dos resultados
    
    Args:
        results: Lista de resultados
        
    Returns:
        Estatísticas calculadas
    """
    if not results:
        return {}
    
    scores = [r.get('overall_score', 0) for r in results]
    
    stats = {
        'total_analyses': len(results),
        'average_score': sum(scores) / len(scores),
        'max_score': max(scores),
        'min_score': min(scores),
        'high_matches': len([s for s in scores if s >= 80]),
        'good_matches': len([s for s in scores if 60 <= s < 80]),
        'moderate_matches': len([s for s in scores if 40 <= s < 60]),
        'low_matches': len([s for s in scores if s < 40])
    }
    
    return stats

def generate_report(results: List[Dict[str, Any]], job_title: str = "Vaga") -> str:
    """
    Gera relatório em texto dos resultados
    
    Args:
        results: Lista de resultados
        job_title: Título da vaga
        
    Returns:
        Relatório em texto
    """
    if not results:
        return "Nenhum resultado para gerar relatório."
    
    stats = calculate_statistics(results)
    
    report = f"""
RELATÓRIO DE ANÁLISE SEMÂNTICA
Vaga: {job_title}
Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}

RESUMO EXECUTIVO:
• Total de currículos analisados: {stats['total_analyses']}
• Score médio: {stats['average_score']:.1f}%
• Melhor score: {stats['max_score']:.1f}%
• Pior score: {stats['min_score']:.1f}%

DISTRIBUIÇÃO POR CATEGORIA:
• Excelente Match (80-100%): {stats['high_matches']} currículos
• Bom Match (60-79%): {stats['good_matches']} currículos
• Match Moderado (40-59%): {stats['moderate_matches']} currículos
• Match Baixo (0-39%): {stats['low_matches']} currículos

TOP 5 CANDIDATOS:
"""
    
    # Ordenar por score e pegar top 5
    top_candidates = sorted(results, key=lambda x: x.get('overall_score', 0), reverse=True)[:5]
    
    for i, candidate in enumerate(top_candidates, 1):
        filename = candidate.get('filename', 'N/A')
        score = candidate.get('overall_score', 0)
        report += f"{i}. {filename}: {score:.1f}%\n"
    
    return report 