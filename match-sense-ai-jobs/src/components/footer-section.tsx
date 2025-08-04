import { Button } from "@/components/ui/button";
import { Brain, Mail, Github, Linkedin } from "lucide-react";

export const FooterSection = () => {
  return (
    <footer className="bg-gradient-hero text-white relative overflow-hidden">
      {/* Background pattern */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute inset-0" style={{
          backgroundImage: `radial-gradient(circle at 75% 75%, white 1px, transparent 1px)`,
          backgroundSize: '30px 30px'
        }} />
      </div>
      
      <div className="container mx-auto px-6 py-16 relative z-10">
        <div className="text-center mb-12">
          <div className="inline-flex items-center gap-3 mb-6">
            <div className="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center backdrop-blur-sm">
              <Brain size={24} className="text-white" />
            </div>
            <span className="text-2xl font-bold">JobMatcher AI</span>
          </div>
          
          <p className="text-xl text-white/90 max-w-2xl mx-auto mb-8">
            Revolucione seu processo de recrutamento com inteligência artificial de ponta
          </p>
          
          <Button 
            size="lg" 
            className="bg-white text-primary hover:bg-white/90 font-semibold px-8 py-4 text-lg shadow-glow"
          >
            <Mail size={20} className="mr-2" />
            Entre em Contato
          </Button>
        </div>
        
        <div className="border-t border-white/20 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center gap-6">
            <div className="text-white/80">
              <p>&copy; 2024 JobMatcher AI. Todos os direitos reservados.</p>
            </div>
            
            <div className="flex gap-4">
              <Button variant="outline" size="icon" className="border-white/30 text-white hover:bg-white/10">
                <Github size={20} />
              </Button>
              <Button variant="outline" size="icon" className="border-white/30 text-white hover:bg-white/10">
                <Linkedin size={20} />
              </Button>
              <Button variant="outline" size="icon" className="border-white/30 text-white hover:bg-white/10">
                <Mail size={20} />
              </Button>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};