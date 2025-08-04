import { Button } from "@/components/ui/button";
import { Brain, Zap } from "lucide-react";

export const HeroSection = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-hero">
      {/* Floating elements */}
      <div className="absolute top-20 left-10 w-20 h-20 bg-primary/10 rounded-full animate-float" />
      <div className="absolute top-40 right-20 w-32 h-32 bg-primary-glow/10 rounded-full animate-float" style={{ animationDelay: '2s' }} />
      <div className="absolute bottom-40 left-20 w-16 h-16 bg-primary/15 rounded-full animate-float" style={{ animationDelay: '4s' }} />
      
      <div className="container mx-auto px-6 text-center relative z-10">
        <div className="max-w-4xl mx-auto">
          {/* Icon */}
          <div className="mb-8 inline-flex items-center justify-center w-24 h-24 bg-white/10 rounded-full backdrop-blur-sm">
            <Brain size={48} className="text-white" />
          </div>
          
          {/* Main heading */}
          <h1 className="text-5xl lg:text-7xl font-bold text-white mb-6 leading-tight">
            JobMatcher <span className="bg-gradient-to-r from-white to-primary-glow bg-clip-text text-transparent">AI</span>
          </h1>
          
          {/* Subtitle */}
          <p className="text-xl lg:text-2xl text-white/90 mb-8 max-w-3xl mx-auto leading-relaxed">
            Solução inteligente para análise de compatibilidade entre vagas e currículos usando 
            <span className="font-semibold"> Processamento de Linguagem Natural</span>
          </p>
          
          {/* Key points */}
          <div className="flex flex-wrap justify-center gap-6 mb-12 text-white/80">
            <div className="flex items-center gap-2">
              <Zap size={20} className="text-primary-glow" />
              <span className="text-lg">Análise Semântica Avançada</span>
            </div>
            <div className="flex items-center gap-2">
              <Zap size={20} className="text-primary-glow" />
              <span className="text-lg">Visualizações Interativas</span>
            </div>
            <div className="flex items-center gap-2">
              <Zap size={20} className="text-primary-glow" />
              <span className="text-lg">Sistema de Recomendação</span>
            </div>
          </div>
          
          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button 
              size="lg" 
              className="bg-white text-primary hover:bg-white/90 font-semibold px-8 py-4 text-lg shadow-glow animate-pulse-glow"
              onClick={() => window.location.href = '/login'}
            >
              Entrar na Plataforma
            </Button>
            <Button 
              size="lg" 
              variant="outline" 
              className="border-white/30 text-white hover:bg-white/10 font-semibold px-8 py-4 text-lg backdrop-blur-sm"
            >
              Ver Demonstração
            </Button>
          </div>
        </div>
      </div>
      
      {/* Background pattern */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute inset-0" style={{
          backgroundImage: `radial-gradient(circle at 25% 25%, white 2px, transparent 2px)`,
          backgroundSize: '50px 50px'
        }} />
      </div>
    </section>
  );
};