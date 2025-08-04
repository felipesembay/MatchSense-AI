# 🎯 MatchSense AI - Sistema de Busca Semântica para Vagas

Sistema completo de análise semântica para compatibilidade entre currículos e vagas de trabalho, utilizando inteligência artificial e processamento de linguagem natural.

## 📋 Visão Geral

O MatchSense AI é uma solução inovadora que combina:

- **Frontend React** com interface moderna e responsiva
- **Backend Python** com motor de NLP avançado
- **Análise semântica** usando transformers (BERT)
- **Processamento inteligente** de documentos
- **Visualização interativa** de resultados

### 🎯 Objetivo

Automatizar e otimizar o processo de matching entre candidatos e vagas, fornecendo:

- **Scores de compatibilidade** precisos
- **Análise detalhada** por categoria
- **Recomendações inteligentes**
- **Visualização clara** dos resultados

## 🏗️ Arquitetura

```
busca_semantica/
├── match-sense-ai-jobs/     # Frontend React
│   ├── src/
│   ├── components/
│   └── pages/
└── backend/                 # Backend Python
    ├── app.py              # Aplicação Streamlit
    ├── semantic_engine.py  # Motor semântico
    ├── document_processor.py # Processador de docs
    └── utils.py            # Utilitários
```

### 🔧 Tecnologias Utilizadas

#### Frontend
- **React 18** com TypeScript
- **Vite** para build
- **Tailwind CSS** para estilização
- **Shadcn/ui** para componentes
- **React Router** para navegação
- **Plotly** para gráficos

#### Backend
- **Python 3.8+**
- **Streamlit** para protótipo
- **Transformers (HuggingFace)** para NLP
- **Sentence Transformers** para embeddings
- **spaCy** para processamento de texto
- **NLTK** para análise linguística
- **FAISS** para busca vetorial

## 🚀 Instalação e Configuração

### Pré-requisitos

- Node.js 18+ (para frontend)
- Python 3.8+ (para backend)
- Git

### 1. Clone o repositório

```bash
git clone <repository-url>
cd busca_semantica
```

### 2. Configurar Frontend

```bash
cd match-sense-ai-jobs
npm install
npm run dev
```

### 3. Configurar Backend

```bash
cd backend
python setup.py
streamlit run app.py
```

## 🎮 Como Usar

### Etapa 1: Upload de Documentos

1. **Currículo**: Faça upload de PDF, DOCX ou TXT
2. **Vaga**: Digite a descrição da vaga ou use o formulário
3. **Processamento**: O sistema extrai informações automaticamente

### Etapa 2: Análise Semântica

1. **Iniciar análise**: Clique em "Iniciar Análise Semântica"
2. **Processamento**: O motor analisa compatibilidade
3. **Resultados**: Visualize scores e métricas

### Etapa 3: Visualização

- **Score Geral**: Compatibilidade geral (0-100%)
- **Análise Detalhada**: Scores por categoria
- **Gráficos**: Visualizações interativas
- **Recomendações**: Sugestões personalizadas

## 📊 Funcionalidades

### 🔍 Análise Semântica

- **Similaridade de significado** entre currículo e vaga
- **Extração de skills** técnicas e soft skills
- **Análise de experiência** e nível profissional
- **Compatibilidade educacional**
- **Recomendações inteligentes**

### 📄 Processamento de Documentos

- **PDF**: Extração de texto com PyPDF2
- **DOCX**: Processamento com python-docx
- **TXT**: Suporte a múltiplos encodings
- **Extração estruturada** de informações

### 📈 Visualização

- **Dashboard interativo** com métricas
- **Gráficos de radar** para análise detalhada
- **Histogramas** de distribuição de scores
- **Tabelas comparativas** de resultados

### ⚙️ Configurações

- **Modelos de embedding** configuráveis
- **Pesos dos fatores** ajustáveis
- **Thresholds** personalizáveis
- **Cache** para performance

## 🧪 Testes

### Dados de Exemplo

O sistema inclui dados de exemplo para testes:

```python
from backend.utils import create_sample_resume, create_sample_job_description

# Currículo de exemplo
resume = create_sample_resume()

# Vaga de exemplo
job = create_sample_job_description()
```

### Teste Rápido

```python
from backend.semantic_engine import SemanticEngine

# Inicializar motor
engine = SemanticEngine()

# Análise
results = engine.analyze_compatibility(resume, job)
print(f"Score: {results['overall_score']:.1f}%")
```

## 📁 Estrutura de Dados

### Currículo Processado

```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "phone": "(11) 99999-9999",
  "location": "São Paulo, SP",
  "experience_years": "5 anos",
  "education": "Bacharelado em Ciência da Computação",
  "skills": ["python", "react", "django"],
  "languages": ["Português", "Inglês"]
}
```

### Resultado da Análise

```json
{
  "overall_score": 85.5,
  "semantic_similarity": 78.2,
  "skills_match": 90.0,
  "experience_match": 75.0,
  "education_match": 50.0,
  "soft_skills_match": 60.0,
  "strengths": ["Excelente match de skills técnicas"],
  "weaknesses": ["Formação acadêmica pode não atender requisitos"],
  "recommendations": ["Este candidato é altamente recomendado para a vaga."]
}
```

## 🔄 Roadmap

### Fase 1: Protótipo ✅
- [x] Backend com Streamlit
- [x] Motor semântico básico
- [x] Processamento de documentos
- [x] Interface de teste

### Fase 2: Integração 🔄
- [ ] API FastAPI
- [ ] Integração com frontend React
- [ ] Autenticação e autorização
- [ ] Banco de dados

### Fase 3: Produção 📋
- [ ] Deploy em cloud
- [ ] Monitoramento e logs
- [ ] Otimizações de performance
- [ ] Testes automatizados

### Fase 4: Melhorias 🚀
- [ ] Suporte multilíngue
- [ ] Análise de sentimento
- [ ] Machine Learning avançado
- [ ] Integração com ATS

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
busca_semantica/
├── match-sense-ai-jobs/          # Frontend React
│   ├── src/
│   │   ├── components/           # Componentes reutilizáveis
│   │   ├── pages/               # Páginas da aplicação
│   │   ├── hooks/               # Custom hooks
│   │   └── lib/                 # Utilitários
│   ├── public/                  # Arquivos estáticos
│   └── package.json
├── backend/                     # Backend Python
│   ├── app.py                  # Aplicação principal
│   ├── semantic_engine.py      # Motor semântico
│   ├── document_processor.py   # Processador de docs
│   ├── utils.py                # Utilitários
│   ├── config.py               # Configurações
│   └── requirements.txt
└── README.md
```

### Scripts Úteis

```bash
# Frontend
npm run dev          # Desenvolvimento
npm run build        # Build de produção
npm run lint         # Linting

# Backend
python setup.py      # Setup inicial
streamlit run app.py # Executar aplicação
python -m pytest     # Executar testes
```

## 🤝 Contribuição

### Como Contribuir

1. **Fork** o repositório
2. **Clone** seu fork
3. **Crie** uma branch para sua feature
4. **Desenvolva** e teste suas mudanças
5. **Commit** suas alterações
6. **Push** para sua branch
7. **Abra** um Pull Request

### Padrões de Código

- **Python**: PEP 8, type hints
- **JavaScript/TypeScript**: ESLint, Prettier
- **Commits**: Conventional Commits
- **Documentação**: Docstrings, README atualizado

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

### Canais de Ajuda

- **Issues**: Para bugs e problemas
- **Discussions**: Para dúvidas e discussões
- **Wiki**: Documentação detalhada
- **Email**: contato@matchsense.ai

### Troubleshooting

#### Problemas Comuns

**Erro: "Modelo spaCy não encontrado"**
```bash
python -m spacy download pt_core_news_sm
```

**Erro: "CUDA out of memory"**
- Use modelo menor
- Reduza batch size
- Use CPU se necessário

**Performance lenta**
- Verifique recursos do sistema
- Use cache quando possível
- Considere otimizações

## 🎉 Agradecimentos

- **HuggingFace** pelos modelos transformers
- **Streamlit** pela plataforma de desenvolvimento
- **React** pela biblioteca frontend
- **Comunidade open source** pelo suporte

---

**MatchSense AI** - Transformando o recrutamento com inteligência artificial 🚀 