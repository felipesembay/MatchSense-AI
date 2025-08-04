# 🎯 MatchSense AI - Backend

Sistema de busca semântica para análise de compatibilidade entre currículos e vagas de trabalho.

## 📋 Visão Geral

Este backend implementa um sistema completo de análise semântica que utiliza:

- **Transformers (HuggingFace)** para geração de embeddings
- **NLP avançado** para extração de informações estruturadas
- **Análise de similaridade** para cálculo de compatibilidade
- **Processamento de documentos** (PDF, DOCX, TXT)

## 🏗️ Arquitetura

```
backend/
├── app.py                 # Aplicação principal Streamlit
├── semantic_engine.py     # Motor de análise semântica
├── document_processor.py  # Processador de documentos
├── utils.py              # Utilitários e funções auxiliares
├── requirements.txt      # Dependências Python
└── README.md            # Esta documentação
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.8+
- pip ou conda

### 1. Clonar e navegar para o diretório

```bash
cd backend
```

### 2. Criar ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Baixar recursos adicionais

```bash
# Baixar modelo spaCy para português
python -m spacy download pt_core_news_sm

# Baixar recursos NLTK (será feito automaticamente na primeira execução)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## 🎮 Como Usar

### Executar a aplicação

```bash
streamlit run app.py
```

A aplicação estará disponível em: `http://localhost:8501`

### Funcionalidades Principais

#### 1. 📄 Upload de Documentos
- **Currículo**: Upload de PDF, DOCX ou TXT
- **Vaga**: Descrição manual da vaga
- **Upload em Lote**: Processamento de múltiplos currículos

#### 2. 🔍 Análise Semântica
- **Score Geral**: Compatibilidade geral (0-100%)
- **Similaridade Semântica**: Análise de significado
- **Match de Skills**: Compatibilidade técnica
- **Match de Experiência**: Alinhamento de nível
- **Match de Educação**: Compatibilidade acadêmica
- **Match de Soft Skills**: Competências comportamentais

#### 3. 📊 Visualização de Resultados
- **Gráficos interativos** com Plotly
- **Métricas detalhadas** por categoria
- **Pontos fortes e fracos**
- **Recomendações personalizadas**

#### 4. ⚙️ Configurações
- **Modelo de embedding** configurável
- **Pesos dos fatores** ajustáveis
- **Threshold de similaridade** personalizável

## 🔧 Configuração

### Modelos Disponíveis

- `sentence-transformers/all-MiniLM-L6-v2` (padrão)
- `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (multilíngue)

### Pesos Padrão

```python
weights = {
    'semantic': 0.4,      # Similaridade semântica
    'skills': 0.3,        # Skills técnicas
    'experience': 0.2,    # Experiência
    'education': 0.05,    # Educação
    'soft_skills': 0.05   # Soft skills
}
```

## 📁 Estrutura de Dados

### Currículo Processado

```python
{
    'name': 'João Silva',
    'email': 'joao@email.com',
    'phone': '(11) 99999-9999',
    'location': 'São Paulo, SP',
    'experience_years': '5 anos',
    'education': 'Bacharelado em Ciência da Computação',
    'skills': ['python', 'react', 'django'],
    'languages': ['Português', 'Inglês'],
    'linkedin': 'linkedin.com/in/joaosilva',
    'github': 'github.com/joaosilva'
}
```

### Resultado da Análise

```python
{
    'overall_score': 85.5,
    'semantic_similarity': 78.2,
    'skills_match': 90.0,
    'experience_match': 75.0,
    'education_match': 50.0,
    'soft_skills_match': 60.0,
    'resume_skills': ['python', 'react', 'django'],
    'job_skills': ['python', 'javascript', 'react'],
    'strengths': ['Excelente match de skills técnicas'],
    'weaknesses': ['Formação acadêmica pode não atender requisitos'],
    'recommendations': ['Este candidato é altamente recomendado para a vaga.']
}
```

## 🧪 Testes

### Dados de Exemplo

O sistema inclui dados de exemplo para testes:

```python
from utils import create_sample_resume, create_sample_job_description

# Criar currículo de exemplo
resume_text = create_sample_resume()

# Criar vaga de exemplo
job_description = create_sample_job_description()
```

### Teste Rápido

```python
from semantic_engine import SemanticEngine

# Inicializar motor
engine = SemanticEngine()

# Análise de compatibilidade
results = engine.analyze_compatibility(resume_text, job_description)
print(f"Score: {results['overall_score']:.1f}%")
```

## 📊 Exportação de Resultados

### JSON
```python
from utils import save_analysis_results

save_analysis_results(results, "meus_resultados.json")
```

### Excel
```python
from utils import export_to_excel

export_to_excel([results], "relatorio_analise.xlsx")
```

## 🔍 Análise em Lote

```python
# Lista de currículos
resumes = [
    {'text': resume1_text, 'filename': 'candidato1.pdf'},
    {'text': resume2_text, 'filename': 'candidato2.pdf'},
    # ...
]

# Análise em lote
batch_results = engine.batch_analyze(resumes, job_description)

# Ordenar por score
sorted_results = sorted(batch_results, key=lambda x: x['overall_score'], reverse=True)
```

## 🚨 Troubleshooting

### Erro: "Modelo spaCy não encontrado"
```bash
python -m spacy download pt_core_news_sm
```

### Erro: "Recursos NLTK não encontrados"
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Erro: "CUDA out of memory"
- Use modelo menor: `all-MiniLM-L6-v2`
- Reduza batch size
- Use CPU: `device='cpu'`

### Performance Lenta
- Use modelo mais leve
- Processe em lotes menores
- Considere usar GPU se disponível

## 🔄 Próximos Passos

### Integração com Frontend React
1. Converter para API FastAPI
2. Implementar endpoints REST
3. Integrar com frontend existente

### Melhorias Planejadas
- [ ] Suporte a mais idiomas
- [ ] Análise de sentimento
- [ ] Extração de entidades nomeadas
- [ ] Cache de embeddings
- [ ] Análise de tendências temporais

## 📝 Licença

Este projeto é parte do sistema MatchSense AI.

## 🤝 Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no repositório
- Consulte a documentação
- Entre em contato com a equipe de desenvolvimento 