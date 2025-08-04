import { Card } from "@/components/ui/card";
import { Users, Building2, Rocket } from "lucide-react";

const useCases = [
  {
    icon: <Users size={48} className="text-primary" />,
    title: "Equipes de RH",
    description: "Automatize a triagem de currículos e acelere o processo de seleção com análises precisas e relatórios detalhados."
  },
  {
    icon: <Building2 size={48} className="text-primary" />,
    title: "Plataformas de Recrutamento",
    description: "Integre nossa IA ao seu sistema para oferecer matchmaking inteligente e melhorar a experiência dos usuários."
  },
  {
    icon: <Rocket size={48} className="text-primary" />,
    title: "Startups",
    description: "Otimize a jornada de contratação desde o início, garantindo que você encontre os talentos certos rapidamente."
  }
];

export const UseCasesSection = () => {
  return (
    <section className="py-24 bg-background relative">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-6">
            Casos de <span className="text-primary">Uso</span>
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Veja como diferentes organizações podem se beneficiar do JobMatcher AI
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {useCases.map((useCase, index) => (
            <Card key={index} className="p-8 text-center bg-card border-border hover:shadow-ai transition-all duration-500 hover:scale-105 group">
              <div className="mb-6 flex justify-center group-hover:animate-float">
                {useCase.icon}
              </div>
              <h3 className="text-2xl font-bold text-card-foreground mb-4">
                {useCase.title}
              </h3>
              <p className="text-muted-foreground leading-relaxed">
                {useCase.description}
              </p>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};