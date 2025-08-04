import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Progress } from "@/components/ui/progress";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { 
  Search, 
  Plus, 
  Star, 
  Archive, 
  Trash2, 
  Eye, 
  Filter,
  Building2,
  LogOut,
  Users,
  Briefcase,
  Clock
} from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const CompanyDashboard = () => {
  const navigate = useNavigate();
  const [selectedJob, setSelectedJob] = useState(1);

  const jobs = [
    {
      id: 1,
      title: "Desenvolvedor Frontend React",
      department: "Tecnologia",
      status: "Ativa",
      applicants: 45,
      posted: "5 dias atrás"
    },
    {
      id: 2,
      title: "UX/UI Designer",
      department: "Design",
      status: "Ativa", 
      applicants: 23,
      posted: "2 semanas atrás"
    }
  ];

  const candidates = [
    {
      id: 1,
      name: "João Silva",
      email: "joao.silva@email.com",
      score: 95,
      experience: "5 anos",
      location: "São Paulo, SP",
      skills: ["React", "TypeScript", "Node.js"],
      status: "Novo",
      appliedDate: "2 dias atrás"
    },
    {
      id: 2,
      name: "Maria Santos",
      email: "maria.santos@email.com", 
      score: 88,
      experience: "3 anos",
      location: "Rio de Janeiro, RJ",
      skills: ["React", "JavaScript", "CSS"],
      status: "Em análise",
      appliedDate: "1 semana atrás"
    },
    {
      id: 3,
      name: "Pedro Costa",
      email: "pedro.costa@email.com",
      score: 82,
      experience: "4 anos", 
      location: "Belo Horizonte, MG",
      skills: ["Vue.js", "React", "Python"],
      status: "Novo",
      appliedDate: "3 dias atrás"
    },
    {
      id: 4,
      name: "Ana Oliveira",
      email: "ana.oliveira@email.com",
      score: 75,
      experience: "2 anos",
      location: "Brasília, DF",
      skills: ["React", "HTML", "CSS"],
      status: "Arquivado",
      appliedDate: "1 semana atrás"
    }
  ];

  const getScoreColor = (score: number) => {
    if (score >= 90) return "text-green-600";
    if (score >= 75) return "text-yellow-600";
    return "text-red-600";
  };

  const getStatusVariant = (status: string) => {
    switch (status) {
      case "Novo": return "default";
      case "Em análise": return "secondary";
      case "Arquivado": return "outline";
      default: return "outline";
    }
  };

  const filteredCandidates = candidates.filter(c => 
    selectedJob === 1 // Filter by selected job
  );

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b bg-card">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-primary">JobMatcher AI - Empresa</h1>
          <div className="flex items-center gap-4">
            <Avatar>
              <AvatarFallback>TC</AvatarFallback>
            </Avatar>
            <div>
              <p className="font-medium">Tech Solutions</p>
              <p className="text-sm text-muted-foreground">RH Manager</p>
            </div>
            <Button variant="ghost" size="sm" onClick={() => navigate('/')}>
              <LogOut className="w-4 h-4 mr-2" />
              Sair
            </Button>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-6">
        {/* Stats Dashboard */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center gap-2">
                <Briefcase className="w-5 h-5 text-primary" />
                <div>
                  <div className="text-2xl font-bold">12</div>
                  <p className="text-sm text-muted-foreground">Vagas ativas</p>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center gap-2">
                <Users className="w-5 h-5 text-primary" />
                <div>
                  <div className="text-2xl font-bold">368</div>
                  <p className="text-sm text-muted-foreground">Candidatos totais</p>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center gap-2">
                <Clock className="w-5 h-5 text-primary" />
                <div>
                  <div className="text-2xl font-bold">47</div>
                  <p className="text-sm text-muted-foreground">Novos hoje</p>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center gap-2">
                <Star className="w-5 h-5 text-primary" />
                <div>
                  <div className="text-2xl font-bold">89%</div>
                  <p className="text-sm text-muted-foreground">Score médio</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <Tabs defaultValue="candidates" className="space-y-6">
          <TabsList>
            <TabsTrigger value="candidates">Candidatos</TabsTrigger>
            <TabsTrigger value="jobs">Minhas Vagas</TabsTrigger>
          </TabsList>

          <TabsContent value="candidates" className="space-y-4">
            {/* Job Selector */}
            <Card>
              <CardHeader>
                <CardTitle>Selecionar Vaga</CardTitle>
                <CardDescription>Escolha uma vaga para ver os candidatos</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {jobs.map((job) => (
                    <Button
                      key={job.id}
                      variant={selectedJob === job.id ? "default" : "outline"}
                      onClick={() => setSelectedJob(job.id)}
                    >
                      {job.title} ({job.applicants})
                    </Button>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Filters and Search */}
            <Card>
              <CardContent className="pt-6">
                <div className="flex gap-2 mb-4">
                  <div className="relative flex-1">
                    <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground w-4 h-4" />
                    <Input
                      placeholder="Buscar candidatos por nome, habilidades..."
                      className="pl-10"
                    />
                  </div>
                  <Button variant="outline">
                    <Filter className="w-4 h-4 mr-2" />
                    Filtros
                  </Button>
                </div>
              </CardContent>
            </Card>

            {/* Candidates List */}
            <div className="space-y-4">
              {filteredCandidates.map((candidate) => (
                <Card key={candidate.id} className="hover:shadow-md transition-shadow">
                  <CardContent className="pt-6">
                    <div className="flex justify-between items-start">
                      <div className="flex items-start gap-4 flex-1">
                        <Avatar className="w-12 h-12">
                          <AvatarFallback>
                            {candidate.name.split(' ').map(n => n[0]).join('')}
                          </AvatarFallback>
                        </Avatar>
                        
                        <div className="flex-1">
                          <div className="flex items-center gap-3 mb-2">
                            <h3 className="text-lg font-semibold">{candidate.name}</h3>
                            <Badge variant={getStatusVariant(candidate.status)}>
                              {candidate.status}
                            </Badge>
                            <Badge variant="outline" className="flex items-center gap-1">
                              <Star className="w-3 h-3" />
                              {candidate.score}%
                            </Badge>
                          </div>
                          
                          <p className="text-sm text-muted-foreground mb-2">
                            {candidate.email} • {candidate.experience} • {candidate.location}
                          </p>
                          
                          <div className="flex flex-wrap gap-2 mb-3">
                            {candidate.skills.map((skill) => (
                              <Badge key={skill} variant="secondary" className="text-xs">
                                {skill}
                              </Badge>
                            ))}
                          </div>

                          <div className="mb-3">
                            <div className="flex justify-between items-center mb-1">
                              <span className="text-sm font-medium">Score de Compatibilidade</span>
                              <span className={`text-sm font-medium ${getScoreColor(candidate.score)}`}>
                                {candidate.score}%
                              </span>
                            </div>
                            <Progress value={candidate.score} className="h-2" />
                          </div>

                          <p className="text-xs text-muted-foreground">
                            Candidatou-se {candidate.appliedDate}
                          </p>
                        </div>
                      </div>

                      <div className="flex flex-col gap-2 min-w-fit">
                        <Button size="sm" variant="outline">
                          <Eye className="w-4 h-4 mr-2" />
                          Ver Perfil
                        </Button>
                        <Button size="sm" variant="outline">
                          <Archive className="w-4 h-4 mr-2" />
                          Arquivar
                        </Button>
                        <Button size="sm" variant="outline">
                          <Trash2 className="w-4 h-4 mr-2" />
                          Excluir
                        </Button>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="jobs" className="space-y-4">
            <div className="flex justify-between items-center">
              <h2 className="text-xl font-semibold">Suas Vagas</h2>
              <Button>
                <Plus className="w-4 h-4 mr-2" />
                Nova Vaga
              </Button>
            </div>

            <div className="grid gap-4">
              {jobs.map((job) => (
                <Card key={job.id}>
                  <CardContent className="pt-6">
                    <div className="flex justify-between items-start">
                      <div>
                        <h3 className="text-lg font-semibold mb-2">{job.title}</h3>
                        <div className="flex items-center gap-4 text-sm text-muted-foreground mb-2">
                          <span>{job.department}</span>
                          <Badge variant="secondary">{job.status}</Badge>
                          <span>{job.posted}</span>
                        </div>
                        <p className="text-sm">
                          <strong>{job.applicants}</strong> candidatos se inscreveram
                        </p>
                      </div>
                      <div className="flex gap-2">
                        <Button variant="outline" size="sm">Ver Candidatos</Button>
                        <Button variant="outline" size="sm">Editar</Button>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
};

export default CompanyDashboard;