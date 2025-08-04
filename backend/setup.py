#!/usr/bin/env python3
"""
Script de setup para o MatchSense AI Backend
Automatiza a instalação e configuração inicial do sistema
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ é necessário. Versão atual:", sys.version)
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} - OK")

def install_package(package):
    """Instala um pacote via pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_packages():
    """Verifica e instala pacotes necessários"""
    print("\n📦 Verificando e instalando dependências...")
    
    # Lista de pacotes essenciais
    essential_packages = [
        "streamlit",
        "transformers",
        "torch",
        "sentence-transformers",
        "faiss-cpu",
        "numpy",
        "pandas",
        "scikit-learn",
        "nltk",
        "spacy"
    ]
    
    for package in essential_packages:
        print(f"Instalando {package}...")
        if install_package(package):
            print(f"✅ {package} instalado com sucesso")
        else:
            print(f"❌ Erro ao instalar {package}")
            return False
    
    return True

def download_spacy_model():
    """Baixa o modelo spaCy para português"""
    print("\n🌐 Baixando modelo spaCy para português...")
    
    try:
        # Tentar baixar o modelo
        subprocess.check_call([
            sys.executable, "-m", "spacy", "download", "pt_core_news_sm"
        ])
        print("✅ Modelo spaCy baixado com sucesso")
        return True
    except subprocess.CalledProcessError:
        print("⚠️ Erro ao baixar modelo spaCy. Tentando alternativa...")
        
        try:
            # Tentar modelo alternativo
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_sm"
            ])
            print("✅ Modelo alternativo baixado")
            return True
        except subprocess.CalledProcessError:
            print("❌ Erro ao baixar modelos spaCy")
            return False

def download_nltk_data():
    """Baixa dados necessários do NLTK"""
    print("\n📚 Baixando dados NLTK...")
    
    try:
        import nltk
        
        # Lista de recursos NLTK necessários
        nltk_resources = ['punkt', 'stopwords', 'averaged_perceptron_tagger']
        
        for resource in nltk_resources:
            try:
                nltk.data.find(f'tokenizers/{resource}')
                print(f"✅ {resource} já disponível")
            except LookupError:
                print(f"Baixando {resource}...")
                nltk.download(resource, quiet=True)
                print(f"✅ {resource} baixado")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao baixar dados NLTK: {e}")
        return False

def create_directories():
    """Cria diretórios necessários"""
    print("\n📁 Criando diretórios...")
    
    directories = [
        "results",
        "exports",
        "uploads",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Diretório {directory} criado")

def test_installation():
    """Testa se a instalação foi bem-sucedida"""
    print("\n🧪 Testando instalação...")
    
    try:
        # Testar imports principais
        import streamlit
        import transformers
        import torch
        import sentence_transformers
        import nltk
        import spacy
        
        print("✅ Todos os imports funcionando")
        
        # Testar modelo básico
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        
        # Teste simples
        sentences = ["Olá mundo", "Hello world"]
        embeddings = model.encode(sentences)
        
        print("✅ Modelo de embedding funcionando")
        print("✅ Instalação concluída com sucesso!")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        return False

def create_sample_files():
    """Cria arquivos de exemplo para teste"""
    print("\n📄 Criando arquivos de exemplo...")
    
    # Currículo de exemplo
    sample_resume = """
João Silva Santos
joao.silva@email.com
(11) 99999-9999
São Paulo, SP

RESUMO PROFISSIONAL
Desenvolvedor Full Stack com 5 anos de experiência em desenvolvimento web, especializado em Python, JavaScript e React.

EXPERIÊNCIA PROFISSIONAL
Desenvolvedor Full Stack Sênior
TechCorp - São Paulo, SP
2021 - Presente
• Desenvolvimento de aplicações web usando Python (Django), React e PostgreSQL
• Liderança técnica de equipe de 4 desenvolvedores

EDUCAÇÃO
Bacharelado em Ciência da Computação
Universidade de São Paulo (USP)
2015 - 2019

HABILIDADES TÉCNICAS
• Python, JavaScript, TypeScript, React, Django, PostgreSQL
• AWS, Docker, Git, Jira

IDIOMAS
• Português: Nativo
• Inglês: Fluente
"""
    
    # Salvar currículo de exemplo
    with open("sample_resume.txt", "w", encoding="utf-8") as f:
        f.write(sample_resume)
    
    print("✅ Arquivo de exemplo criado: sample_resume.txt")

def main():
    """Função principal do setup"""
    print("🎯 MatchSense AI - Setup do Backend")
    print("=" * 50)
    
    # Verificar versão do Python
    check_python_version()
    
    # Instalar pacotes
    if not check_and_install_packages():
        print("❌ Falha na instalação de pacotes")
        sys.exit(1)
    
    # Baixar modelo spaCy
    if not download_spacy_model():
        print("⚠️ Aviso: Modelo spaCy não foi baixado. Algumas funcionalidades podem não funcionar.")
    
    # Baixar dados NLTK
    if not download_nltk_data():
        print("⚠️ Aviso: Dados NLTK não foram baixados. Algumas funcionalidades podem não funcionar.")
    
    # Criar diretórios
    create_directories()
    
    # Criar arquivos de exemplo
    create_sample_files()
    
    # Testar instalação
    if test_installation():
        print("\n🎉 Setup concluído com sucesso!")
        print("\n📋 Próximos passos:")
        print("1. Execute: streamlit run app.py")
        print("2. Acesse: http://localhost:8501")
        print("3. Use o arquivo sample_resume.txt para testes")
    else:
        print("\n❌ Setup falhou. Verifique os erros acima.")
        sys.exit(1)

if __name__ == "__main__":
    main() 