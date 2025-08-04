import PyPDF2
import docx
import re
import io
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)

class DocumentProcessor:
    """
    Processador de documentos para extração de texto e informações estruturadas
    """
    
    def __init__(self):
        """Inicializa o processador de documentos"""
        pass
    
    def extract_text(self, file) -> str:
        """
        Extrai texto de um arquivo
        
        Args:
            file: Arquivo carregado (PDF, DOCX, TXT)
            
        Returns:
            Texto extraído do arquivo
        """
        try:
            filename = file.name.lower()
            
            if filename.endswith('.pdf'):
                return self._extract_from_pdf(file)
            elif filename.endswith('.docx'):
                return self._extract_from_docx(file)
            elif filename.endswith('.txt'):
                return self._extract_from_txt(file)
            else:
                raise ValueError(f"Formato de arquivo não suportado: {filename}")
                
        except Exception as e:
            logger.error(f"Erro ao extrair texto do arquivo {file.name}: {str(e)}")
            raise
    
    def _extract_from_pdf(self, file) -> str:
        """
        Extrai texto de um arquivo PDF
        
        Args:
            file: Arquivo PDF
            
        Returns:
            Texto extraído
        """
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            return text.strip()
            
        except Exception as e:
            logger.error(f"Erro ao extrair texto do PDF: {str(e)}")
            raise
    
    def _extract_from_docx(self, file) -> str:
        """
        Extrai texto de um arquivo DOCX
        
        Args:
            file: Arquivo DOCX
            
        Returns:
            Texto extraído
        """
        try:
            doc = docx.Document(file)
            text = ""
            
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            return text.strip()
            
        except Exception as e:
            logger.error(f"Erro ao extrair texto do DOCX: {str(e)}")
            raise
    
    def _extract_from_txt(self, file) -> str:
        """
        Extrai texto de um arquivo TXT
        
        Args:
            file: Arquivo TXT
            
        Returns:
            Texto extraído
        """
        try:
            # Decodificar o arquivo
            content = file.read()
            
            # Tentar diferentes encodings
            encodings = ['utf-8', 'latin-1', 'cp1252']
            
            for encoding in encodings:
                try:
                    text = content.decode(encoding)
                    return text.strip()
                except UnicodeDecodeError:
                    continue
            
            # Se nenhum encoding funcionar, usar utf-8 com tratamento de erros
            return content.decode('utf-8', errors='ignore').strip()
            
        except Exception as e:
            logger.error(f"Erro ao extrair texto do TXT: {str(e)}")
            raise
    
    def extract_resume_info(self, text: str) -> Dict[str, Any]:
        """
        Extrai informações estruturadas de um currículo
        
        Args:
            text: Texto do currículo
            
        Returns:
            Dicionário com informações extraídas
        """
        try:
            info = {
                'name': self._extract_name(text),
                'email': self._extract_email(text),
                'phone': self._extract_phone(text),
                'location': self._extract_location(text),
                'experience_years': self._extract_experience_years(text),
                'education': self._extract_education(text),
                'skills': self._extract_skills(text),
                'languages': self._extract_languages(text),
                'linkedin': self._extract_linkedin(text),
                'github': self._extract_github(text)
            }
            
            return info
            
        except Exception as e:
            logger.error(f"Erro ao extrair informações do currículo: {str(e)}")
            return {}
    
    def _extract_name(self, text: str) -> str:
        """
        Extrai o nome do candidato
        
        Args:
            text: Texto do currículo
            
        Returns:
            Nome extraído
        """
        # Padrões comuns para nomes
        patterns = [
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)',  # Nome no início
            r'(?:Nome|Name):\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)',  # Nome após label
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\s*\n',  # Nome seguido de quebra de linha
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.MULTILINE)
            if match:
                return match.group(1).strip()
        
        return "Não identificado"
    
    def _extract_email(self, text: str) -> str:
        """
        Extrai o email do candidato
        
        Args:
            text: Texto do currículo
            
        Returns:
            Email extraído
        """
        # Padrão para email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        match = re.search(email_pattern, text)
        if match:
            return match.group(0)
        
        return "Não identificado"
    
    def _extract_phone(self, text: str) -> str:
        """
        Extrai o telefone do candidato
        
        Args:
            text: Texto do currículo
            
        Returns:
            Telefone extraído
        """
        # Padrões para telefone brasileiro
        phone_patterns = [
            r'\(?(\d{2})\)?\s*(\d{4,5})-?(\d{4})',  # (11) 99999-9999
            r'(\d{2})\s*(\d{4,5})\s*(\d{4})',  # 11 99999 9999
            r'\+55\s*(\d{2})\s*(\d{4,5})\s*(\d{4})',  # +55 11 99999 9999
        ]
        
        for pattern in phone_patterns:
            match = re.search(pattern, text)
            if match:
                if len(match.groups()) == 3:
                    return f"({match.group(1)}) {match.group(2)}-{match.group(3)}"
                else:
                    return match.group(0)
        
        return "Não identificado"
    
    def _extract_location(self, text: str) -> str:
        """
        Extrai a localização do candidato
        
        Args:
            text: Texto do currículo
            
        Returns:
            Localização extraída
        """
        # Padrões para localização
        location_patterns = [
            r'(?:Localização|Location|Endereço|Address):\s*([^\n]+)',
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*),\s*[A-Z]{2}',  # Cidade, Estado
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*-\s*[A-Z]{2}',  # Cidade - Estado
        ]
        
        for pattern in location_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return "Não identificado"
    
    def _extract_experience_years(self, text: str) -> str:
        """
        Extrai anos de experiência
        
        Args:
            text: Texto do currículo
            
        Returns:
            Anos de experiência
        """
        # Padrões para anos de experiência
        experience_patterns = [
            r'(\d+)\s*(?:anos?|years?)\s*(?:de\s+)?(?:experiência|experience)',
            r'(?:experiência|experience)\s*(?:de\s+)?(\d+)\s*(?:anos?|years?)',
            r'(\d+)\s*(?:anos?|years?)\s*(?:no\s+)?(?:mercado|market)',
        ]
        
        for pattern in experience_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                years = match.group(1)
                return f"{years} anos"
        
        return "Não identificado"
    
    def _extract_education(self, text: str) -> str:
        """
        Extrai informações de educação
        
        Args:
            text: Texto do currículo
            
        Returns:
            Educação extraída
        """
        # Padrões para educação
        education_patterns = [
            r'(?:Formação|Education|Graduação|Graduation):\s*([^\n]+)',
            r'(?:Bacharelado|Bachelor|Licenciatura|Mestrado|Master|Doutorado|PhD):\s*([^\n]+)',
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*-\s*(?:Universidade|University|Faculdade|College)',
        ]
        
        for pattern in education_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return "Não identificado"
    
    def _extract_skills(self, text: str) -> List[str]:
        """
        Extrai skills técnicas
        
        Args:
            text: Texto do currículo
            
        Returns:
            Lista de skills
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
        
        # Converter texto para minúsculas para busca
        text_lower = text.lower()
        
        # Encontrar skills mencionadas
        found_skills = []
        for skill in technical_skills:
            if skill in text_lower:
                found_skills.append(skill)
        
        return found_skills[:10]  # Limitar a 10 skills mais relevantes
    
    def _extract_languages(self, text: str) -> List[str]:
        """
        Extrai idiomas
        
        Args:
            text: Texto do currículo
            
        Returns:
            Lista de idiomas
        """
        # Padrões para idiomas
        language_patterns = [
            r'(?:Idiomas|Languages):\s*([^\n]+)',
            r'(?:Português|Inglês|Espanhol|Francês|Alemão|Italiano|Chinês|Japonês):\s*(?:Fluente|Avançado|Intermediário|Básico)',
        ]
        
        languages = []
        for pattern in language_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                languages.append(match.group(1).strip())
        
        return languages if languages else ["Não especificado"]
    
    def _extract_linkedin(self, text: str) -> str:
        """
        Extrai perfil do LinkedIn
        
        Args:
            text: Texto do currículo
            
        Returns:
            URL do LinkedIn
        """
        # Padrão para LinkedIn
        linkedin_pattern = r'https?://(?:www\.)?linkedin\.com/in/[a-zA-Z0-9-]+'
        
        match = re.search(linkedin_pattern, text)
        if match:
            return match.group(0)
        
        return "Não identificado"
    
    def _extract_github(self, text: str) -> str:
        """
        Extrai perfil do GitHub
        
        Args:
            text: Texto do currículo
            
        Returns:
            URL do GitHub
        """
        # Padrão para GitHub
        github_pattern = r'https?://(?:www\.)?github\.com/[a-zA-Z0-9-]+'
        
        match = re.search(github_pattern, text)
        if match:
            return match.group(0)
        
        return "Não identificado"
    
    def clean_text(self, text: str) -> str:
        """
        Limpa e normaliza o texto
        
        Args:
            text: Texto a ser limpo
            
        Returns:
            Texto limpo
        """
        # Remover caracteres especiais desnecessários
        text = re.sub(r'[^\w\sáàâãéèêíìîóòôõúùûç.,!?;:()]', ' ', text)
        
        # Remover espaços extras
        text = re.sub(r'\s+', ' ', text)
        
        # Remover quebras de linha desnecessárias
        text = re.sub(r'\n\s*\n', '\n', text)
        
        return text.strip()
    
    def extract_sections(self, text: str) -> Dict[str, str]:
        """
        Extrai seções do currículo
        
        Args:
            text: Texto do currículo
            
        Returns:
            Dicionário com seções extraídas
        """
        sections = {}
        
        # Padrões para seções comuns
        section_patterns = {
            'experiencia': r'(?:Experiência|Experience|Histórico Profissional)(.*?)(?=\n\s*[A-Z][a-z]+:|$)',
            'educacao': r'(?:Educação|Education|Formação Acadêmica)(.*?)(?=\n\s*[A-Z][a-z]+:|$)',
            'skills': r'(?:Skills|Habilidades|Competências|Tecnologias)(.*?)(?=\n\s*[A-Z][a-z]+:|$)',
            'projetos': r'(?:Projetos|Projects)(.*?)(?=\n\s*[A-Z][a-z]+:|$)',
            'certificacoes': r'(?:Certificações|Certifications)(.*?)(?=\n\s*[A-Z][a-z]+:|$)',
            'idiomas': r'(?:Idiomas|Languages)(.*?)(?=\n\s*[A-Z][a-z]+:|$)',
        }
        
        for section_name, pattern in section_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                sections[section_name] = match.group(1).strip()
        
        return sections 