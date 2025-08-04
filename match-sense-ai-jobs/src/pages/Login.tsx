import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Github, Chrome, Users, Building2 } from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [userType, setUserType] = useState<'candidate' | 'company' | null>(null);
  const navigate = useNavigate();

  const handleLogin = (provider: string) => {
    // Simulate login - in real app would integrate with auth provider
    if (userType === 'candidate') {
      navigate('/candidate-dashboard');
    } else if (userType === 'company') {
      navigate('/company-dashboard');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary/10 via-background to-secondary/10 flex items-center justify-center p-4">
      <div className="w-full max-w-4xl">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-primary to-primary-glow bg-clip-text text-transparent mb-2">
            JobMatcher AI
          </h1>
          <p className="text-muted-foreground text-lg">
            Conecte talentos com oportunidades usando inteligência artificial
          </p>
        </div>

        {!userType ? (
          <div className="grid md:grid-cols-2 gap-6">
            <Card className="cursor-pointer transition-all hover:shadow-elegant border-primary/20 hover:border-primary/40" 
                  onClick={() => setUserType('candidate')}>
              <CardHeader className="text-center">
                <div className="mx-auto w-16 h-16 bg-gradient-primary rounded-full flex items-center justify-center mb-4">
                  <Users className="w-8 h-8 text-white" />
                </div>
                <CardTitle className="text-2xl">Sou Candidato</CardTitle>
                <CardDescription className="text-base">
                  Encontre vagas que combinam com seu perfil
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-muted-foreground">
                  <li>• Busca inteligente de vagas</li>
                  <li>• Score de compatibilidade</li>
                  <li>• Upload de CV automático</li>
                  <li>• Recomendações personalizadas</li>
                </ul>
              </CardContent>
            </Card>

            <Card className="cursor-pointer transition-all hover:shadow-elegant border-primary/20 hover:border-primary/40" 
                  onClick={() => setUserType('company')}>
              <CardHeader className="text-center">
                <div className="mx-auto w-16 h-16 bg-gradient-primary rounded-full flex items-center justify-center mb-4">
                  <Building2 className="w-8 h-8 text-white" />
                </div>
                <CardTitle className="text-2xl">Sou Empresa</CardTitle>
                <CardDescription className="text-base">
                  Encontre os melhores candidatos para suas vagas
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-muted-foreground">
                  <li>• Ranking automático de candidatos</li>
                  <li>• Análise semântica avançada</li>
                  <li>• Gestão de candidaturas</li>
                  <li>• Dashboard completo</li>
                </ul>
              </CardContent>
            </Card>
          </div>
        ) : (
          <Card className="max-w-md mx-auto">
            <CardHeader className="text-center">
              <CardTitle className="text-2xl">
                {userType === 'candidate' ? 'Login - Candidato' : 'Login - Empresa'}
              </CardTitle>
              <CardDescription>
                Escolha uma opção para continuar
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <Button 
                onClick={() => handleLogin('google')} 
                variant="outline" 
                className="w-full h-12"
              >
                <Chrome className="w-5 h-5 mr-2" />
                Continuar com Google
              </Button>
              
              <Button 
                onClick={() => handleLogin('github')} 
                variant="outline" 
                className="w-full h-12"
              >
                <Github className="w-5 h-5 mr-2" />
                Continuar com GitHub
              </Button>

              <Button 
                onClick={() => setUserType(null)} 
                variant="ghost" 
                className="w-full"
              >
                Voltar
              </Button>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
};

export default Login;