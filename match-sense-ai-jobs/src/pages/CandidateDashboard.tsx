import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Progress } from "@/components/ui/progress";
import { Search, Upload, Star, MapPin, Clock, Building2, LogOut } from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const CandidateDashboard = () => {
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState("");

  const jobs = [
    {
      id: 1,
      title: "Desenvolvedor Frontend React",
      company: "Tech Solutions",
      location: "São Paulo, SP",
      salary: "R$ 8.000 - R$ 12.000",
      score: 95,
      postedTime: "2 dias atrás",
      skills: ["React", "TypeScript", "Tailwind CSS"],
      description: "Buscamos desenvolvedor experiente em React para projetos inovadores..."
    },
    {
      id: 2,
      title: "Full Stack Developer",
      company: "StartupXYZ",
      location: "Remote",
      salary: "R$ 10.000 - R$ 15.000",
      score: 88,
      postedTime: "1 semana atrás",
      skills: ["Node.js", "React", "PostgreSQL"],
      description: "Oportunidade para trabalhar em startup em crescimento..."
    },
    {
      id: 3,
      title: "Desenvolvedor Python",
      company: "Data Corp",
      location: "Rio de Janeiro, RJ",
      salary: "R$ 9.000 - R$ 14.000",
      score: 75,
      postedTime: "3 dias atrás",
      skills: ["Python", "Django", "Machine Learning"],
      description: "Desenvolvedor Python para projetos de ciência de dados..."
    }
  ];

  const getScoreColor = (score: number) => {
    if (score >= 90) return "text-green-600";
    if (score >= 75) return "text-yellow-600";
    return "text-red-600";
  };

  const getScoreVariant = (score: number) => {
    if (score >= 90) return "default";
    if (score >= 75) return "secondary";
    return "destructive";
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b bg-card">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-primary">JobMatcher AI</h1>
          <div className="flex items-center gap-4">
            <Avatar>
              <AvatarFallback>JD</AvatarFallback>
            </Avatar>
            <div>
              <p className="font-medium">João Silva</p>
              <p className="text-sm text-muted-foreground">Desenvolvedor</p>
            </div>
            <Button variant="ghost" size="sm" onClick={() => navigate('/')}>
              <LogOut className="w-4 h-4 mr-2" />
              Sair
            </Button>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-6">
        {/* Upload CV Section */}
        <Card className="mb-6">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Upload className="w-5 h-5" />
              Seu Currículo
            </CardTitle>
            <CardDescription>
              Mantenha seu CV atualizado para melhores recomendações
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-4">
              <Button>
                <Upload className="w-4 h-4 mr-2" />
                Fazer Upload do CV
              </Button>
              <p className="text-sm text-muted-foreground">
                Último upload: curriculum_joao_silva.pdf (hoje)
              </p>
            </div>
          </CardContent>
        </Card>

        {/* Search */}
        <Card className="mb-6">
          <CardContent className="pt-6">
            <div className="flex gap-2">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground w-4 h-4" />
                <Input
                  placeholder="Buscar por cargo, empresa ou tecnologia..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="pl-10"
                />
              </div>
              <Button>Buscar</Button>
            </div>
          </CardContent>
        </Card>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <Card>
            <CardContent className="pt-6">
              <div className="text-2xl font-bold">127</div>
              <p className="text-sm text-muted-foreground">Vagas disponíveis</p>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="pt-6">
              <div className="text-2xl font-bold">23</div>
              <p className="text-sm text-muted-foreground">Candidaturas enviadas</p>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="pt-6">
              <div className="text-2xl font-bold">5</div>
              <p className="text-sm text-muted-foreground">Entrevistas agendadas</p>
            </CardContent>
          </Card>
        </div>

        {/* Job Listings */}
        <div className="space-y-4">
          <h2 className="text-xl font-semibold">Vagas Recomendadas para Você</h2>
          
          {jobs.map((job) => (
            <Card key={job.id} className="hover:shadow-md transition-shadow">
              <CardContent className="pt-6">
                <div className="flex justify-between items-start mb-4">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <h3 className="text-xl font-semibold">{job.title}</h3>
                      <Badge variant={getScoreVariant(job.score)} className="flex items-center gap-1">
                        <Star className="w-3 h-3" />
                        {job.score}% match
                      </Badge>
                    </div>
                    <div className="flex items-center gap-4 text-sm text-muted-foreground mb-3">
                      <div className="flex items-center gap-1">
                        <Building2 className="w-4 h-4" />
                        {job.company}
                      </div>
                      <div className="flex items-center gap-1">
                        <MapPin className="w-4 h-4" />
                        {job.location}
                      </div>
                      <div className="flex items-center gap-1">
                        <Clock className="w-4 h-4" />
                        {job.postedTime}
                      </div>
                    </div>
                    <p className="text-lg font-medium text-primary mb-3">{job.salary}</p>
                    <p className="text-muted-foreground mb-4">{job.description}</p>
                  </div>
                </div>

                <div className="flex justify-between items-center">
                  <div className="flex flex-wrap gap-2">
                    {job.skills.map((skill) => (
                      <Badge key={skill} variant="outline">
                        {skill}
                      </Badge>
                    ))}
                  </div>
                  <div className="flex gap-2">
                    <Button variant="outline">Ver Detalhes</Button>
                    <Button>Candidatar-se</Button>
                  </div>
                </div>

                <div className="mt-4">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm font-medium">Compatibilidade</span>
                    <span className={`text-sm font-medium ${getScoreColor(job.score)}`}>
                      {job.score}%
                    </span>
                  </div>
                  <Progress value={job.score} className="h-2" />
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CandidateDashboard;