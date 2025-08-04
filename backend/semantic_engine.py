import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from typing import Dict, List, Tuple, Any
import logging

# Tentar importar spaCy, mas tornar opcional
try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False
    print("⚠️ spaCy não disponível. Algumas funcionalidades podem ser limitadas.")

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SemanticEngine:
    """
    Motor principal para análise semântica de compatibilidade entre currículos e vagas
    """
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Inicializa o motor semântico
        
        Args:
            model_name: Nome do modelo de embedding a ser usado
        """
        self.model_name = model_name
        self.model = None
        self.nlp = None
        self.stop_words = set()
        
        # Configurações padrão
        self.config = {
            'similarity_threshold': 0.7,
            'weights': {
                'semantic': 0.4,
                'skills': 0.3,
                'experience': 0.2,
                'education': 0.05,
                'soft_skills': 0.05
            }
        }
        
        # Inicializar recursos
        self._initialize_resources()
    
    def _initialize_resources(self):
        """Inicializa os recursos necessários (modelo, spaCy, NLTK)"""
        try:
            logger.info(f"Carregando modelo: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            
            # Carregar spaCy para processamento de texto (opcional)
            if SPACY_AVAILABLE:
                try:
                    self.nlp = spacy.load("pt_core_news_sm")
                    logger.info("Modelo spaCy carregado com sucesso")
                except OSError:
                    logger.warning("Modelo spaCy pt_core_news_sm não encontrado. spaCy será usado em modo limitado.")
                    self.nlp = None
            else:
                logger.warning("spaCy não disponível. Usando processamento de texto básico.")
                self.nlp = None
            
            # Baixar recursos NLTK se necessário
            try:
                nltk.data.find('tokenizers/punkt')
            except LookupError:
                nltk.download('punkt')
            
            try:
                nltk.data.find('corpora/stopwords')
            except LookupError:
                nltk.download('stopwords')
            
            # Carregar stop words em português
            self.stop_words = set(stopwords.words('portuguese'))
            
            logger.info("Recursos inicializados com sucesso!")
            
        except Exception as e:
            logger.error(f"Erro ao inicializar recursos: {str(e)}")
            raise
    
    def preprocess_text(self, text: str) -> str:
        """
        Pré-processa o texto para análise
        
        Args:
            text: Texto a ser processado
            
        Returns:
            Texto processado
        """
        if not text:
            return ""
        
        # Converter para minúsculas
        text = text.lower()
        
        # Remover caracteres especiais mantendo acentos
        text = re.sub(r'[^\w\sáàâãéèêíìîóòôõúùûç]', ' ', text)
        
        # Remover espaços extras
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def extract_skills(self, text: str) -> List[str]:
        """
        Extrai skills técnicas do texto
        
        Args:
            text: Texto para extração de skills
            
        Returns:
            Lista de skills encontradas
        """
        # Lista de skills técnicas comuns
        technical_skills = [
            # Linguagens de programação
            'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust',
            'swift', 'kotlin', 'scala', 'r', 'matlab', 'perl', 'bash', 'powershell',
            
            # Frameworks e bibliotecas
            'react', 'angular', 'vue', 'node.js', 'express', 'django', 'flask', 'spring',
            'laravel', 'asp.net', 'jquery', 'bootstrap', 'tailwind', 'material-ui',
            
            # Bancos de dados
            'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle', 'sql server',
            'elasticsearch', 'cassandra', 'dynamodb',
            
            # Cloud e DevOps
            'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'gitlab', 'github',
            'terraform', 'ansible', 'prometheus', 'grafana',
            
            # Ferramentas e tecnologias
            'git', 'svn', 'jira', 'confluence', 'slack', 'teams', 'zoom', 'figma',
            'adobe', 'photoshop', 'illustrator', 'sketch', 'invision',
            
            # Metodologias
            'agile', 'scrum', 'kanban', 'lean', 'devops', 'ci/cd', 'tdd', 'bdd',
            
            # Outras tecnologias
            'html', 'css', 'sass', 'less', 'webpack', 'babel', 'npm', 'yarn',
            'rest', 'graphql', 'soap', 'microservices', 'api', 'json', 'xml'
        ]
        
        # Processar texto
        processed_text = self.preprocess_text(text)
        words = word_tokenize(processed_text)
        
        # Encontrar skills
        found_skills = []
        for word in words:
            if word in technical_skills and word not in found_skills:
                found_skills.append(word)
        
        return found_skills
    
    def extract_experience_info(self, text: str) -> Dict[str, Any]:
        """
        Extrai informações de experiência do texto
        
        Args:
            text: Texto para análise
            
        Returns:
            Dicionário com informações de experiência
        """
        # Padrões para encontrar anos de experiência
        experience_patterns = [
            r'(\d+)\s*(?:anos?|years?)\s*(?:de\s+)?(?:experiência|experience)',
            r'(?:experiência|experience)\s*(?:de\s+)?(\d+)\s*(?:anos?|years?)',
            r'(\d+)\s*(?:anos?|years?)\s*(?:no\s+)?(?:mercado|market)',
            r'(\d+)\s*(?:anos?|years?)\s*(?:trabalhando|working)'
        ]
        
        years_experience = 0
        for pattern in experience_patterns:
            matches = re.findall(pattern, text.lower())
            if matches:
                years_experience = max([int(match) for match in matches])
                break
        
        # Detectar nível de experiência baseado nos anos
        if years_experience == 0:
            experience_level = "Júnior"
        elif years_experience <= 3:
            experience_level = "Júnior"
        elif years_experience <= 6:
            experience_level = "Pleno"
        elif years_experience <= 10:
            experience_level = "Sênior"
        else:
            experience_level = "Especialista"
        
        return {
            'years': years_experience,
            'level': experience_level
        }
    
    def extract_education_info(self, text: str) -> Dict[str, Any]:
        """
        Extrai informações de educação do texto
        
        Args:
            text: Texto para análise
            
        Returns:
            Dicionário com informações de educação
        """
        # Padrões para encontrar formações
        education_patterns = {
            'graduação': r'(?:graduação|graduation|bacharelado|bachelor|licenciatura)',
            'pós_graduação': r'(?:pós\s*graduação|post\s*graduation|especialização|specialization)',
            'mestrado': r'(?:mestrado|master|m\.s\.|ms)',
            'doutorado': r'(?:doutorado|phd|doctorate|dr\.)',
            'técnico': r'(?:técnico|technical|curso\s*técnico)',
            'certificação': r'(?:certificação|certification|certificado|certificate)'
        }
        
        education_levels = []
        for level, pattern in education_patterns.items():
            if re.search(pattern, text.lower()):
                education_levels.append(level)
        
        # Determinar nível mais alto
        education_hierarchy = ['técnico', 'graduação', 'pós_graduação', 'mestrado', 'doutorado']
        highest_level = 'sem_formação'
        
        for level in education_hierarchy:
            if level in education_levels:
                highest_level = level
                break
        
        return {
            'levels': education_levels,
            'highest_level': highest_level
        }
    
    def extract_soft_skills(self, text: str) -> List[str]:
        """
        Extrai soft skills do texto
        
        Args:
            text: Texto para análise
            
        Returns:
            Lista de soft skills encontradas
        """
        soft_skills = [
            'liderança', 'leadership', 'comunicação', 'communication', 'trabalho em equipe',
            'teamwork', 'resolução de problemas', 'problem solving', 'criatividade',
            'creativity', 'adaptabilidade', 'adaptability', 'flexibilidade', 'flexibility',
            'proatividade', 'proactivity', 'organização', 'organization', 'gestão de tempo',
            'time management', 'negociação', 'negotiation', 'empatia', 'empathy',
            'resiliência', 'resilience', 'pensamento crítico', 'critical thinking',
            'inovação', 'innovation', 'colaboração', 'collaboration', 'autonomia',
            'autonomy', 'responsabilidade', 'responsibility', 'comprometimento',
            'commitment', 'motivação', 'motivation', 'aprendizado contínuo',
            'continuous learning', 'gestão de conflitos', 'conflict management'
        ]
        
        processed_text = self.preprocess_text(text)
        words = word_tokenize(processed_text)
        
        found_soft_skills = []
        for word in words:
            if word in soft_skills and word not in found_soft_skills:
                found_soft_skills.append(word)
        
        return found_soft_skills
    
    def calculate_semantic_similarity(self, text1: str, text2: str) -> float:
        """
        Calcula a similaridade semântica entre dois textos
        
        Args:
            text1: Primeiro texto
            text2: Segundo texto
            
        Returns:
            Score de similaridade (0-1)
        """
        try:
            # Gerar embeddings
            embedding1 = self.model.encode(text1, convert_to_tensor=True)
            embedding2 = self.model.encode(text2, convert_to_tensor=True)
            
            # Calcular similaridade cosseno
            similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
            
            return max(0, similarity)  # Garantir que não seja negativo
            
        except Exception as e:
            logger.error(f"Erro ao calcular similaridade semântica: {str(e)}")
            return 0.0
    
    def calculate_skills_match(self, resume_skills: List[str], job_skills: List[str]) -> float:
        """
        Calcula o match de skills entre currículo e vaga
        
        Args:
            resume_skills: Skills do currículo
            job_skills: Skills da vaga
            
        Returns:
            Score de match de skills (0-100)
        """
        if not job_skills:
            return 50.0  # Score neutro se não há skills especificadas
        
        if not resume_skills:
            return 0.0
        
        # Calcular interseção
        matching_skills = set(resume_skills) & set(job_skills)
        
        # Score baseado na proporção de skills encontradas
        match_percentage = len(matching_skills) / len(job_skills) * 100
        
        # Bonus para skills extras no currículo
        extra_skills_bonus = min(len(resume_skills) - len(matching_skills), 10) * 2
        
        return min(100, match_percentage + extra_skills_bonus)
    
    def calculate_experience_match(self, resume_exp: Dict, job_level: str) -> float:
        """
        Calcula o match de experiência
        
        Args:
            resume_exp: Informações de experiência do currículo
            job_level: Nível da vaga
            
        Returns:
            Score de match de experiência (0-100)
        """
        resume_level = resume_exp.get('level', 'Júnior')
        resume_years = resume_exp.get('years', 0)
        
        # Mapeamento de níveis para pontuação
        level_scores = {
            'Júnior': 1,
            'Pleno': 2,
            'Sênior': 3,
            'Especialista': 4
        }
        
        resume_score = level_scores.get(resume_level, 1)
        job_score = level_scores.get(job_level, 1)
        
        # Calcular diferença
        level_diff = abs(resume_score - job_score)
        
        if level_diff == 0:
            return 100.0  # Match perfeito
        elif level_diff == 1:
            return 75.0   # Próximo
        elif level_diff == 2:
            return 50.0   # Moderado
        else:
            return 25.0   # Distante
    
    def calculate_education_match(self, resume_edu: Dict, job_requirements: str) -> float:
        """
        Calcula o match de educação
        
        Args:
            resume_edu: Informações de educação do currículo
            job_requirements: Requisitos da vaga
            
        Returns:
            Score de match de educação (0-100)
        """
        highest_level = resume_edu.get('highest_level', 'sem_formação')
        
        # Mapeamento de níveis educacionais
        education_scores = {
            'sem_formação': 0,
            'técnico': 25,
            'graduação': 50,
            'pós_graduação': 75,
            'mestrado': 90,
            'doutorado': 100
        }
        
        base_score = education_scores.get(highest_level, 0)
        
        # Verificar se a vaga menciona requisitos educacionais específicos
        if any(word in job_requirements.lower() for word in ['graduação', 'bacharelado', 'mestrado', 'doutorado']):
            # Ajustar score baseado nos requisitos
            if 'doutorado' in job_requirements.lower() and highest_level != 'doutorado':
                base_score *= 0.7
            elif 'mestrado' in job_requirements.lower() and highest_level not in ['mestrado', 'doutorado']:
                base_score *= 0.8
            elif 'graduação' in job_requirements.lower() and highest_level in ['sem_formação', 'técnico']:
                base_score *= 0.6
        
        return min(100, base_score)
    
    def calculate_soft_skills_match(self, resume_soft_skills: List[str], job_description: str) -> float:
        """
        Calcula o match de soft skills
        
        Args:
            resume_soft_skills: Soft skills do currículo
            job_description: Descrição da vaga
            
        Returns:
            Score de match de soft skills (0-100)
        """
        if not resume_soft_skills:
            return 50.0  # Score neutro
        
        # Extrair soft skills da descrição da vaga
        job_soft_skills = self.extract_soft_skills(job_description)
        
        if not job_soft_skills:
            return 50.0  # Score neutro se não há soft skills mencionadas
        
        # Calcular match
        matching_skills = set(resume_soft_skills) & set(job_soft_skills)
        match_percentage = len(matching_skills) / len(job_soft_skills) * 100
        
        return min(100, match_percentage)
    
    def generate_recommendations(self, analysis_results: Dict) -> List[str]:
        """
        Gera recomendações baseadas na análise
        
        Args:
            analysis_results: Resultados da análise
            
        Returns:
            Lista de recomendações
        """
        recommendations = []
        
        # Recomendações baseadas no score geral
        overall_score = analysis_results.get('overall_score', 0)
        
        if overall_score >= 80:
            recommendations.append("Excelente compatibilidade! Este candidato é altamente recomendado para a vaga.")
        elif overall_score >= 60:
            recommendations.append("Boa compatibilidade. Considere entrevistar o candidato para avaliar melhor.")
        elif overall_score >= 40:
            recommendations.append("Compatibilidade moderada. Avalie se o candidato pode se desenvolver na posição.")
        else:
            recommendations.append("Compatibilidade baixa. Considere outros candidatos ou ajuste os requisitos da vaga.")
        
        # Recomendações específicas por categoria
        if analysis_results.get('skills_match', 0) < 50:
            recommendations.append("Considere treinamento em tecnologias específicas para melhorar a compatibilidade técnica.")
        
        if analysis_results.get('experience_match', 0) < 50:
            recommendations.append("O nível de experiência pode não estar alinhado com a posição. Considere ajustar expectativas.")
        
        if analysis_results.get('education_match', 0) < 50:
            recommendations.append("A formação acadêmica pode não atender aos requisitos. Avalie se é realmente necessária.")
        
        return recommendations
    
    def analyze_compatibility(self, resume_text: str, job_description: str, job_level: str = "Pleno") -> Dict[str, Any]:
        """
        Analisa a compatibilidade entre um currículo e uma vaga
        
        Args:
            resume_text: Texto do currículo
            job_description: Descrição da vaga
            job_level: Nível da vaga
            
        Returns:
            Dicionário com resultados da análise
        """
        try:
            logger.info("Iniciando análise de compatibilidade...")
            
            # Extrair informações do currículo
            resume_skills = self.extract_skills(resume_text)
            resume_experience = self.extract_experience_info(resume_text)
            resume_education = self.extract_education_info(resume_text)
            resume_soft_skills = self.extract_soft_skills(resume_text)
            
            # Extrair skills da vaga
            job_skills = self.extract_skills(job_description)
            
            # Calcular scores individuais
            semantic_similarity = self.calculate_semantic_similarity(resume_text, job_description) * 100
            skills_match = self.calculate_skills_match(resume_skills, job_skills)
            experience_match = self.calculate_experience_match(resume_experience, job_level)
            education_match = self.calculate_education_match(resume_education, job_description)
            soft_skills_match = self.calculate_soft_skills_match(resume_soft_skills, job_description)
            
            # Calcular score geral ponderado
            weights = self.config['weights']
            overall_score = (
                semantic_similarity * weights['semantic'] +
                skills_match * weights['skills'] +
                experience_match * weights['experience'] +
                education_match * weights['education'] +
                soft_skills_match * weights['soft_skills']
            )
            
            # Gerar pontos fortes e fracos
            strengths = []
            weaknesses = []
            
            if semantic_similarity >= 70:
                strengths.append("Alta compatibilidade semântica com a descrição da vaga")
            elif semantic_similarity < 40:
                weaknesses.append("Baixa compatibilidade semântica com a descrição da vaga")
            
            if skills_match >= 70:
                strengths.append("Excelente match de skills técnicas")
            elif skills_match < 40:
                weaknesses.append("Skills técnicas não atendem aos requisitos")
            
            if experience_match >= 70:
                strengths.append("Nível de experiência adequado para a posição")
            elif experience_match < 40:
                weaknesses.append("Nível de experiência pode não ser adequado")
            
            # Gerar recomendações
            recommendations = self.generate_recommendations({
                'overall_score': overall_score,
                'skills_match': skills_match,
                'experience_match': experience_match,
                'education_match': education_match
            })
            
            results = {
                'overall_score': overall_score,
                'semantic_similarity': semantic_similarity,
                'skills_match': skills_match,
                'experience_match': experience_match,
                'education_match': education_match,
                'soft_skills_match': soft_skills_match,
                'resume_skills': resume_skills,
                'job_skills': job_skills,
                'resume_experience': resume_experience,
                'resume_education': resume_education,
                'resume_soft_skills': resume_soft_skills,
                'strengths': strengths,
                'weaknesses': weaknesses,
                'recommendations': recommendations,
                'analysis_timestamp': pd.Timestamp.now().isoformat()
            }
            
            logger.info(f"Análise concluída. Score geral: {overall_score:.1f}%")
            return results
            
        except Exception as e:
            logger.error(f"Erro na análise de compatibilidade: {str(e)}")
            raise
    
    def batch_analyze(self, resumes: List[Dict], job_description: str, job_level: str = "Pleno") -> List[Dict]:
        """
        Analisa múltiplos currículos contra uma vaga
        
        Args:
            resumes: Lista de currículos (cada um com 'text' e 'filename')
            job_description: Descrição da vaga
            job_level: Nível da vaga
            
        Returns:
            Lista de resultados ordenados por score
        """
        results = []
        
        for resume in resumes:
            try:
                analysis = self.analyze_compatibility(
                    resume['text'],
                    job_description,
                    job_level
                )
                
                analysis['filename'] = resume['filename']
                results.append(analysis)
                
            except Exception as e:
                logger.error(f"Erro ao analisar {resume.get('filename', 'unknown')}: {str(e)}")
                results.append({
                    'filename': resume.get('filename', 'unknown'),
                    'overall_score': 0,
                    'error': str(e)
                })
        
        # Ordenar por score geral
        results.sort(key=lambda x: x.get('overall_score', 0), reverse=True)
        
        return results
    
    def update_config(self, new_config: Dict):
        """
        Atualiza a configuração do motor
        
        Args:
            new_config: Nova configuração
        """
        self.config.update(new_config)
        logger.info("Configuração atualizada") 