"""
Configurações centralizadas para o MatchSense AI Backend
"""

import os
from typing import Dict, Any

class Config:
    """Configurações do sistema"""
    
    # Configurações do modelo
    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    MULTILINGUAL_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    
    # Configurações de similaridade
    DEFAULT_SIMILARITY_THRESHOLD = 0.7
    
    # Pesos padrão para análise
    DEFAULT_WEIGHTS = {
        'semantic': 0.4,      # Similaridade semântica
        'skills': 0.3,        # Skills técnicas
        'experience': 0.2,    # Experiência
        'education': 0.05,    # Educação
        'soft_skills': 0.05   # Soft skills
    }
    
    # Configurações de processamento
    MAX_FILE_SIZE_MB = 10.0
    SUPPORTED_FORMATS = ['.pdf', '.docx', '.txt']
    
    # Configurações de diretórios
    RESULTS_DIR = "results"
    EXPORTS_DIR = "exports"
    UPLOADS_DIR = "uploads"
    LOGS_DIR = "logs"
    
    # Configurações de logging
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configurações de performance
    BATCH_SIZE = 10
    MAX_TEXT_LENGTH = 10000
    
    # Configurações de cache
    CACHE_ENABLED = True
    CACHE_TTL = 3600  # 1 hora
    
    @classmethod
    def get_model_config(cls) -> Dict[str, Any]:
        """Retorna configurações do modelo"""
        return {
            'default_model': cls.DEFAULT_MODEL,
            'multilingual_model': cls.MULTILINGUAL_MODEL,
            'similarity_threshold': cls.DEFAULT_SIMILARITY_THRESHOLD
        }
    
    @classmethod
    def get_weights_config(cls) -> Dict[str, float]:
        """Retorna configurações de pesos"""
        return cls.DEFAULT_WEIGHTS.copy()
    
    @classmethod
    def get_processing_config(cls) -> Dict[str, Any]:
        """Retorna configurações de processamento"""
        return {
            'max_file_size_mb': cls.MAX_FILE_SIZE_MB,
            'supported_formats': cls.SUPPORTED_FORMATS,
            'batch_size': cls.BATCH_SIZE,
            'max_text_length': cls.MAX_TEXT_LENGTH
        }
    
    @classmethod
    def get_directories_config(cls) -> Dict[str, str]:
        """Retorna configurações de diretórios"""
        return {
            'results_dir': cls.RESULTS_DIR,
            'exports_dir': cls.EXPORTS_DIR,
            'uploads_dir': cls.UPLOADS_DIR,
            'logs_dir': cls.LOGS_DIR
        }
    
    @classmethod
    def create_directories(cls):
        """Cria diretórios necessários"""
        directories = [
            cls.RESULTS_DIR,
            cls.EXPORTS_DIR,
            cls.UPLOADS_DIR,
            cls.LOGS_DIR
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    @classmethod
    def validate_weights(cls, weights: Dict[str, float]) -> bool:
        """Valida se os pesos somam 1.0"""
        total = sum(weights.values())
        return abs(total - 1.0) < 0.01
    
    @classmethod
    def normalize_weights(cls, weights: Dict[str, float]) -> Dict[str, float]:
        """Normaliza pesos para somar 1.0"""
        total = sum(weights.values())
        if total == 0:
            return cls.DEFAULT_WEIGHTS
        
        normalized = {}
        for key, value in weights.items():
            normalized[key] = value / total
        
        return normalized

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    
    LOG_LEVEL = "DEBUG"
    CACHE_ENABLED = False
    
    # Configurações de desenvolvimento
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configurações para produção"""
    
    LOG_LEVEL = "WARNING"
    CACHE_ENABLED = True
    
    # Configurações de produção
    DEBUG = False
    TESTING = False
    
    # Configurações de segurança
    MAX_FILE_SIZE_MB = 5.0
    MAX_TEXT_LENGTH = 5000

class TestingConfig(Config):
    """Configurações para testes"""
    
    LOG_LEVEL = "ERROR"
    CACHE_ENABLED = False
    
    # Configurações de teste
    DEBUG = True
    TESTING = True
    
    # Usar modelo menor para testes
    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def get_config(environment: str = None) -> Config:
    """
    Retorna configuração baseada no ambiente
    
    Args:
        environment: Ambiente ('development', 'production', 'testing')
        
    Returns:
        Configuração apropriada
    """
    if environment is None:
        environment = os.getenv('ENVIRONMENT', 'development')
    
    config_map = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    
    return config_map.get(environment.lower(), DevelopmentConfig) 