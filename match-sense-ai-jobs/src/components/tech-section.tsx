import { Badge } from "@/components/ui/badge";

const technologies = [
  { name: "Python", category: "Backend" },
  { name: "Streamlit", category: "Framework" },
  { name: "SBERT", category: "AI/ML" },
  { name: "TF-IDF", category: "AI/ML" },
  { name: "Cosine Similarity", category: "AI/ML" },
  { name: "Plotly", category: "Visualização" },
  { name: "Matplotlib", category: "Visualização" },
  { name: "Seaborn", category: "Visualização" },
  { name: "PyMuPDF", category: "Processamento" },
  { name: "pdfminer", category: "Processamento" },
  { name: "Faker", category: "Dados" },
  { name: "NLP", category: "AI/ML" }
];

export const TechSection = () => {
  return (
    <section className="py-24 bg-card relative overflow-hidden">
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-primary-glow/5" />
      
      <div className="container mx-auto px-6 relative z-10">
        <div className="text-center mb-16">
          <h2 className="text-4xl lg:text-5xl font-bold text-card-foreground mb-6">
            Tecnologia <span className="text-primary">Avançada</span>
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            Construído com as melhores tecnologias para garantir performance, precisão e escalabilidade
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <div className="flex flex-wrap justify-center gap-4">
            {technologies.map((tech, index) => (
              <Badge 
                key={index}
                variant="secondary" 
                className="px-6 py-3 text-lg font-medium bg-gradient-primary text-primary-foreground hover:scale-105 transition-transform duration-300 shadow-card"
              >
                {tech.name}
              </Badge>
            ))}
          </div>
          
          <div className="mt-16 text-center">
            <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
              Nossa stack tecnológica combina o poder do processamento de linguagem natural 
              com visualizações interativas para entregar insights precisos e acionáveis.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};