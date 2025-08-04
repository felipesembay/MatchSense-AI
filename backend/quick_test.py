#!/usr/bin/env python3
"""
Teste rápido para verificar se a funcionalidade está funcionando
"""

def quick_test():
    """Teste rápido da funcionalidade"""
    print("🎯 Teste Rápido - MatchSense AI")
    print("=" * 40)
    
    try:
        # Importar componentes
        from semantic_engine import SemanticEngine
        from document_processor import DocumentProcessor
        
        print("✅ Componentes importados")
        
        # Teste simples
        engine = SemanticEngine()
        processor = DocumentProcessor()
        
        print("✅ Componentes inicializados")
        
        # Teste com dados simples
        job_desc = "Desenvolvedor Python com experiência em Django e React"
        resume = "Desenvolvedor Full Stack com 5 anos de experiência em Python, Django, React e JavaScript"
        
        result = engine.analyze_compatibility(resume, job_desc, "Senior")
        
        print(f"✅ Análise concluída: {result['overall_score']:.1f}%")
        print("✅ Funcionalidade funcionando corretamente!")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

if __name__ == "__main__":
    quick_test() 