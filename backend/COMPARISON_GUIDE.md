# 📊 Guia da Funcionalidade de Comparação de Candidatos

## 🎯 Visão Geral

A funcionalidade de **Comparação de Candidatos** permite analisar múltiplos currículos contra uma vaga específica, fornecendo um ranking detalhado e comparações visuais dos resultados.

## 🚀 Como Usar

### 1. Acesse a Funcionalidade
- Vá para o menu lateral
- Selecione **"📊 Comparação de Candidatos"**

### 2. Adicione a Descrição da Vaga
- Cole a descrição da vaga no campo de texto
- O sistema mostrará estatísticas automáticas:
  - Número de palavras
  - Número de caracteres
  - Adequação para análise

### 3. Adicione os Currículos

#### Opção A: Upload de Arquivos
- Clique em "Upload de currículos"
- Selecione múltiplos arquivos (PDF, DOCX, TXT)
- Os nomes dos candidatos serão extraídos automaticamente

#### Opção B: Input Manual
- Defina o número de currículos a adicionar
- Para cada currículo:
  - Cole o texto do currículo
  - Digite o nome do candidato

### 4. Configure a Análise
- **Usar Sumarização SBART**: Melhora a qualidade da análise
- **Peso Análise Semântica**: Define a importância da análise semântica (0.0 - 1.0)
- **Mostrar Explicações**: Exibe análises detalhadas individuais

### 5. Execute a Análise
- Clique em **"🚀 Analisar com Inteligência Artificial"**
- Aguarde o processamento
- Visualize os resultados

## 📊 Resultados da Análise

### Métricas Gerais
- **Total de Candidatos**: Número de currículos analisados
- **Score Médio**: Média dos scores de compatibilidade
- **Melhor Score**: Maior score obtido
- **Pior Score**: Menor score obtido

### Ranking de Candidatos
- Gráfico de barras colorido por score
- Ordenação automática do melhor para o pior candidato
- Escala de cores: Verde (alto) → Amarelo (médio) → Vermelho (baixo)

### Tabela Detalhada
- **Candidato**: Nome do candidato
- **Score Geral**: Score final de compatibilidade
- **Semântica**: Similaridade semântica
- **Skills**: Match de habilidades técnicas
- **Experiência**: Compatibilidade de experiência
- **Educação**: Match de formação acadêmica
- **Soft Skills**: Compatibilidade de habilidades comportamentais
- **Categoria**: Classificação automática

### Análise Individual (se habilitada)
Para cada candidato, você verá:

#### 🎯 Score de Compatibilidade
- Gauge chart visual com pontuação
- Detalhes do score em formato numérico
- Categoria de compatibilidade

#### 🔧 Análise de Skills
- **Habilidades Compatíveis**: Skills que o candidato possui
- **Habilidades em Falta**: Skills requeridas mas não encontradas
- **Match de Skills**: Percentual de compatibilidade de skills

#### 💡 Recomendação
- **Excelente candidato** (≥80%): Recomendado para entrevista
- **Bom candidato** (60-79%): Considere treinamento para skills em falta
- **Baixa compatibilidade** (<60%): Avalie outros aspectos

## 📈 Interpretação dos Scores

### Categorias de Compatibilidade
- **80-100%**: Excelente compatibilidade
- **60-79%**: Boa compatibilidade
- **40-59%**: Compatibilidade moderada
- **0-39%**: Baixa compatibilidade

### Fatores Analisados
1. **Similaridade Semântica** (40%): Compatibilidade textual geral
2. **Skills Técnicas** (30%): Habilidades técnicas específicas
3. **Experiência** (20%): Nível e relevância da experiência
4. **Educação** (5%): Formação acadêmica
5. **Soft Skills** (5%): Habilidades comportamentais

## 🎯 Casos de Uso

### Recrutamento e Seleção
- Compare candidatos para uma vaga específica
- Identifique os melhores perfis rapidamente
- Tome decisões baseadas em dados objetivos

### Análise de Mercado
- Entenda o perfil dos candidatos disponíveis
- Identifique gaps de skills no mercado
- Ajuste descrições de vagas baseado nos candidatos

### Desenvolvimento de Equipe
- Identifique candidatos com potencial de crescimento
- Planeje treinamentos baseado em skills em falta
- Avalie compatibilidade cultural e técnica

## 💡 Dicas de Uso

### Para Melhores Resultados
1. **Descrição da Vaga**: Seja específico sobre requisitos e responsabilidades
2. **Currículos**: Use currículos completos e atualizados
3. **Configurações**: Ajuste os pesos conforme a importância de cada fator
4. **Análise**: Use as explicações detalhadas para entender os scores

### Interpretação dos Resultados
- Scores altos não garantem sucesso, mas indicam boa compatibilidade
- Considere outros fatores como cultura da empresa e fit cultural
- Use os resultados como ferramenta de apoio, não decisão única
- Analise as habilidades em falta para planejar treinamentos

## 🔧 Configurações Avançadas

### Peso da Análise Semântica
- **Alto (0.8-1.0)**: Prioriza compatibilidade textual geral
- **Médio (0.5-0.7)**: Equilibra todos os fatores
- **Baixo (0.0-0.4)**: Prioriza skills específicas e experiência

### Sumarização SBART
- **Habilitada**: Melhora a qualidade da análise para textos longos
- **Desabilitada**: Análise mais rápida para textos curtos

## 📋 Exemplo de Uso

### Cenário: Vaga de Desenvolvedor Full Stack
1. **Descrição da Vaga**: Cole a descrição completa da vaga
2. **Currículos**: Adicione 5-10 currículos de candidatos
3. **Configuração**: Use peso semântico de 0.8
4. **Análise**: Execute e analise os resultados
5. **Decisão**: Selecione os 3 melhores para entrevista

### Resultado Esperado
- Ranking claro dos candidatos
- Identificação de skills em falta
- Recomendações específicas para cada candidato
- Base objetiva para decisões de contratação

## 🚀 Próximas Funcionalidades

- **Exportação de Relatórios**: PDF e Excel
- **Histórico de Comparações**: Salvar e comparar análises anteriores
- **Análise de Equipe**: Comparar perfis de equipes existentes
- **Integração com ATS**: Conectar com sistemas de recrutamento
- **Análise de Diversidade**: Métricas de diversidade e inclusão 