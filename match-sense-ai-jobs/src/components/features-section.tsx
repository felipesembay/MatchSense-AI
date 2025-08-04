import { FeatureCard } from "@/components/ui/feature-card";
import { Brain, Upload, BarChart3, Target, Database, Cog } from "lucide-react";

const features = [
  {
    icon: <Brain size={40} />,
    title: "Análise Semântica Avançada",
    description: "Motor de análise que vai além da correspondência de palavras-chave, utilizando modelos de linguagem para interpretar significado e intenção com extração automática de skills."
  },
  {
    icon: <Upload size={40} />,
    title: "Múltiplos Modos de Entrada",
    description: "Flexibilidade total com upload de arquivos, entrada manual e modo híbrido. Suporta importação em lote de currículos e descrições de vagas com processamento automático de PDFs."
  },
  {
    icon: <BarChart3 size={40} />,
    title: "Visualizações Interativas",
    description: "Transforme dados em insights com gráficos de gauge, radar charts, heatmaps de similaridade e distribuições estatísticas para análise completa dos resultados."
  },
  {
    icon: <Target size={40} />,
    title: "Sistema de Recomendação",
    description: "Turbine seu processo seletivo com ranqueamento inteligente, scores de compatibilidade claros e ordenação automática dos melhores perfis por vaga."
  },
  {
    icon: <Database size={40} />,
    title: "Geração de Dados Sintéticos",
    description: "Facilite testes e simulações com dados realistas usando integração com Faker, mais de 60 skills técnicas e cenários autênticos para desenvolvimento."
  },
  {
    icon: <Cog size={40} />,
    title: "Tecnologia Avançada",
    description: "Construído com Python, Streamlit e modelos SBERT/TF-IDF para similaridade semântica, com visualizações em Plotly e extração eficiente de texto de PDFs."
  }
];

export const FeaturesSection = () => {
  return (
    <section className="py-24 bg-gradient-secondary relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute top-0 left-0 w-96 h-96 bg-primary/5 rounded-full blur-3xl -translate-x-48 -translate-y-48" />
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-primary-glow/5 rounded-full blur-3xl translate-x-48 translate-y-48" />
      
      <div className="container mx-auto px-6 relative z-10">
        <div className="text-center mb-16">
          <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-6">
            Funcionalidades <span className="text-primary">Principais</span>
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            Descubra como o JobMatcher AI revoluciona o processo de seleção com tecnologia de ponta 
            e inteligência artificial aplicada ao recrutamento
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <FeatureCard
              key={index}
              icon={feature.icon}
              title={feature.title}
              description={feature.description}
              className="transform transition-all duration-500"
            />
          ))}
        </div>
      </div>
    </section>
  );
};