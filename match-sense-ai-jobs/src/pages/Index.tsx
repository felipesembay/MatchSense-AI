import { HeroSection } from "@/components/hero-section";
import { FeaturesSection } from "@/components/features-section";
import { UseCasesSection } from "@/components/use-cases-section";
import { TechSection } from "@/components/tech-section";
import { FooterSection } from "@/components/footer-section";

const Index = () => {
  return (
    <div className="min-h-screen">
      <HeroSection />
      <FeaturesSection />
      <UseCasesSection />
      <TechSection />
      <FooterSection />
    </div>
  );
};

export default Index;
