window.ESCOPO = {
  "rfs": {
    "RF00": {
      "nome": "Encerrar sessão",
      "estado": "Detalhado",
      "cp": "Acesso e controle de usuários",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível ao usuário autenticado encerrar sua sessão ativa no sistema, invalidando suas credenciais de acesso e redirecionando-o para a tela de login.",
      "entradas": "Ação \"Sair\"",
      "pre": "Usuário autenticado",
      "proc": "Invalida a sessão ativa e suas credenciais e redireciona para a tela de login",
      "saidas": "Sessão encerrada; tela de login exibida",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um usuário autenticado, quando clica em sair, então a sessão é invalidada e ele é redirecionado para a tela de login.",
        "2. Dada uma sessão encerrada, quando tenta acessar uma funcionalidade administrativa, então o sistema exige nova autenticação."
      ],
      "rns": [
        "RN17",
        "RN18"
      ],
      "rnfs": [
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC04"
      ],
      "pens": [
        "PEN04"
      ],
      "its": [
        "Iteração 7"
      ],
      "lacunas": [
        "PEN04: Completar a data e a fonte das decisões DEC04 e DEC05"
      ]
    },
    "RF01": {
      "nome": "Autenticar usuário",
      "estado": "Detalhado",
      "cp": "Acesso e controle de usuários",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível ao coordenador acessar a área de coordenação informando usuário e senha.",
      "entradas": "Usuário (formato CSCP + sequência numérica); senha",
      "pre": "Usuário previamente cadastrado ou usuário administrador padrão",
      "proc": "Valida usuário e senha; se corretos, inicia a sessão e libera a área de coordenação",
      "saidas": "Acesso à área de coordenação; mensagem de erro quando as credenciais forem inválidas",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dados usuário e senha válidos, quando o coordenador se autentica, então o sistema libera a área de coordenação.",
        "2. Dadas credenciais inválidas, quando tenta autenticar, então o sistema nega o acesso e informa o erro.",
        "3. Dada a tela de login, então ela não apresenta opção de cadastro."
      ],
      "rns": [
        "RN19",
        "RN20",
        "RN21"
      ],
      "rnfs": [
        "RNF11",
        "RNF12",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [
        "Iteração 7"
      ],
      "lacunas": []
    },
    "RF02": {
      "nome": "Controlar acesso",
      "estado": "Detalhado",
      "cp": "Acesso e controle de usuários",
      "ator": "Sistema (aplica o perfil de coordenador)",
      "declaracao": "O sistema deve disponibilizar as funcionalidades administrativas exclusivamente para usuários autenticados com perfil de coordenador.",
      "entradas": "Requisição a uma funcionalidade administrativa, com ou sem sessão autenticada",
      "pre": "Funcionalidade administrativa existente",
      "proc": "Verifica se há sessão autenticada com perfil de coordenador; se houver, libera a funcionalidade; caso contrário, nega a requisição",
      "saidas": "Funcionalidade liberada ou acesso negado",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "Dado um usuário autenticado com perfil de coordenador, quando acessa uma funcionalidade administrativa, então o sistema a libera.",
        "Dada uma requisição sem autenticação ou sem o perfil de coordenador, quando tenta acessar uma funcionalidade administrativa, então o sistema nega o acesso."
      ],
      "rns": [
        "RN20"
      ],
      "rnfs": [
        "RNF11",
        "RNF13",
        "RNF08"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [
        "Iteração 7"
      ],
      "lacunas": []
    },
    "RF03": {
      "nome": "Cadastrar turma",
      "estado": "Detalhado",
      "cp": "CP1: Gestão e acompanhamento de turmas",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação cadastrar turmas.",
      "entradas": "Modalidade; dias e horários. [PENDENTE] demais campos (nome da turma, instrutor, limite de vagas)",
      "pre": "Coordenador autenticado",
      "proc": "Valida os campos obrigatórios e grava a turma",
      "saidas": "Turma disponível para associação de alunos; mensagem de erro em caso de campo ausente",
      "pdf": false,
      "pendente": 1,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dada uma turma com modalidade e horários, quando salva, então ela fica disponível para seleção no cadastro do aluno.",
        "2. Dados campos obrigatórios ausentes, quando tenta salvar, então o sistema bloqueia e informa."
      ],
      "rns": [
        "RN22"
      ],
      "rnfs": [
        "RNF01",
        "RNF03",
        "RNF06",
        "RNF11"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [
        "PEN09"
      ],
      "its": [
        "Iteração 8"
      ],
      "lacunas": [
        "1 campo(s) marcado(s) como pendente na ficha",
        "PEN09: Regra citada em 30/10 para turmas com limite de 30 alunos e inscrição prévia da pessoa ficou pouco clara"
      ]
    },
    "RF04": {
      "nome": "Editar turma",
      "estado": "Rascunho",
      "cp": "CP1: Gestão e acompanhamento de turmas",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação editar os dados de uma turma já cadastrada.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Os dados alterados da turma são salvos e exibidos atualizados na consulta. Os alunos já associados à turma são mantidos."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF06",
        "RNF10",
        "RNF11"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF05": {
      "nome": "Inativar turma",
      "estado": "Rascunho",
      "cp": "CP1: Gestão e acompanhamento de turmas",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação inativar uma turma, preservando o histórico de alunos e frequências vinculados a ela, sem excluir os registros do sistema.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Após a confirmação, a turma passa a constar como inativa. Os alunos e as frequências vinculados a ela continuam consultáveis, sem exclusão de registros."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF04",
        "RNF05",
        "RNF10",
        "RNF11"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC02"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF06": {
      "nome": "Associar aluno à turma",
      "estado": "Detalhado",
      "cp": "CP1: Gestão e acompanhamento de turmas",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível associar um aluno a uma turma (modalidade, dias e horários).",
      "entradas": "Aluno; turma",
      "pre": "Aluno e turma cadastrados",
      "proc": "Vincula o aluno à turma escolhida.",
      "saidas": "Aluno vinculado à turma",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dados um aluno e uma turma existentes, quando a coordenação os associa, então o aluno aparece vinculado à turma.",
        "2. Dado o cadastro de um aluno, então é possível escolher a turma na própria ficha."
      ],
      "rns": [
        "RN23"
      ],
      "rnfs": [
        "RNF03",
        "RNF04",
        "RNF06",
        "RNF11"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [
        "PEN09"
      ],
      "its": [
        "Iteração 8"
      ],
      "lacunas": [
        "PEN09: Regra citada em 30/10 para turmas com limite de 30 alunos e inscrição prévia da pessoa ficou pouco clara"
      ]
    },
    "RF07": {
      "nome": "Consultar alunos de uma turma",
      "estado": "Detalhado",
      "cp": "CP1: Gestão e acompanhamento de turmas",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação consultar os alunos que fazem parte de uma turma específica.",
      "entradas": "Seleção da turma",
      "pre": "Turma cadastrada; coordenador autenticado",
      "proc": "Busca os alunos associados à turma e exibe a listagem; ao selecionar um aluno, abre a ficha (RF23)",
      "saidas": "Lista de alunos da turma (foto e nome completo)",
      "pdf": false,
      "pendente": 1,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dada uma turma com alunos associados, quando a coordenação a seleciona, então o sistema lista os alunos da turma.",
        "2. Dada uma turma sem alunos, quando consultada, então o sistema informa que não há alunos associados."
      ],
      "rns": [
        "RN24"
      ],
      "rnfs": [
        "RNF01",
        "RNF06",
        "RNF11"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [
        "PEN02"
      ],
      "its": [
        "Iteração 8"
      ],
      "lacunas": [
        "1 campo(s) marcado(s) como pendente na ficha",
        "PEN02: Definir se alunos inativos aparecem na lista da turma"
      ]
    },
    "RF08": {
      "nome": "Registrar doação recebida",
      "estado": "Rascunho",
      "cp": "CP2: Registro de doações e prestação de contas",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação registrar uma doação ou recurso recebido, identificando o doador ou parceiro, o tipo de recurso e as informações correspondentes.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "1, Não precisa ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: A doação é salva com o doador ou parceiro, o tipo de recurso e as demais informações obrigatórias, e passa a constar no histórico de doações. Campo obrigatório vazio impede o registro."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF09": {
      "nome": "Editar doação recebida",
      "estado": "Rascunho",
      "cp": "CP2: Registro de doações e prestação de contas",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação editar uma doação ou recurso recebido, conseguindo mudar as dados informados.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "1, Não precisa ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Os dados alterados da doação são salvos e exibidos atualizados no histórico. A edição é registrada em log com data e usuário responsável."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF06",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF10": {
      "nome": "Registrar documentos de prestação de contas",
      "estado": "Rascunho",
      "cp": "CP2: Registro de doações e prestação de contas",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação registrar documentos utilizados na prestação de contas, como orçamentos, notas fiscais e registros fotográficos ou audiovisuais, vinculando-os à respectiva doação ou recurso recebido.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "1, Não precisa ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Cada documento (orçamento, nota fiscal, registro fotográfico ou audiovisual) só é salvo vinculado a uma doação ou recurso recebido. Após salvo, o documento pode ser aberto na consulta da doação."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF11": {
      "nome": "Editar documentos de prestação de contas",
      "estado": "Rascunho",
      "cp": "CP2: Registro de doações e prestação de contas",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação conseguir editar os documentos já informado ou anexado utilizados na prestação de contas.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "1, Não precisa ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O documento já registrado pode ser substituído ou ter seus dados alterados, mantendo o vínculo com a doação ou recurso. A versão atualizada é exibida na consulta."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF06",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF12": {
      "nome": "Consultar doações e prestações de contas",
      "estado": "Rascunho",
      "cp": "CP2: Registro de doações e prestação de contas",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação consultar o histórico consolidado de doações e prestações de contas registradas em um determinado período.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "1, Não precisa ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Ao informar um período, o sistema lista as doações registradas nele com os documentos de prestação de contas vinculados. Período sem registros exibe mensagem informativa."
      ],
      "rns": [],
      "rnfs": [
        "RNF06",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF13": {
      "nome": "Publicar conteúdo institucional",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação publicar conteúdos institucionais, como informações da organização, fotos e vídeos, no módulo público.",
      "entradas": "Título (obrigatório); texto, imagens e vídeos (opcionais)",
      "pre": "Coordenador autenticado no sistema",
      "proc": "Valida a presença do título, armazena os anexos informados e grava a publicação como visível no módulo público",
      "saidas": "Conteúdo exibido no módulo público; mensagem de erro quando o título não for informado",
      "pdf": true,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um conteúdo com título, quando a coordenação publica, então ele passa a ser exibido no módulo público para qualquer visitante, sem login.",
        "2. Dado um conteúdo sem título, quando a coordenação tenta publicar, então o sistema bloqueia a publicação e informa que o título é obrigatório.",
        "3. Dado um conteúdo apenas com título e imagem, quando publicado, então o sistema o aceita sem exigir texto ou vídeo."
      ],
      "rns": [
        "RN25",
        "RN26",
        "RN27"
      ],
      "rnfs": [
        "RNF01",
        "RNF02",
        "RNF07",
        "RNF09"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Feito"
        ],
        [
          "Construção: implementação",
          "Em Andamento"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC06",
        "DEC07",
        "DEC11",
        "DEC12",
        "DEC13"
      ],
      "pens": [
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF14": {
      "nome": "Editar conteúdo institucional",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação editar conteúdos institucionais já publicados, como informações da organização, fotos e vídeos, no módulo público.",
      "entradas": "Título, texto, imagens e vídeos (alterados, adicionados ou removidos)",
      "pre": "Coordenador autenticado; conteúdo institucional já publicado",
      "proc": "Carrega o conteúdo existente, permite alterar texto e substituir ou remover fotos e vídeos, valida o título e grava as alterações",
      "saidas": "Conteúdo atualizado exibido no módulo público",
      "pdf": true,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um conteúdo publicado, quando a coordenação altera o texto e salva, então a nova versão é exibida no módulo público.",
        "2. Dado um conteúdo com vídeo ou foto, quando a coordenação os remove ou substitui, então o módulo público exibe apenas a mídia atual.",
        "3. Dado que a coordenação apagou o título, quando tenta salvar, então o sistema bloqueia a gravação."
      ],
      "rns": [
        "RN25",
        "RN26",
        "RN28"
      ],
      "rnfs": [
        "RNF01",
        "RNF02",
        "RNF07",
        "RNF09",
        "RNF10"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC06",
        "DEC07",
        "DEC08",
        "DEC11",
        "DEC12",
        "DEC13"
      ],
      "pens": [
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF15": {
      "nome": "Consultar conteúdo institucional",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Visitante (qualquer pessoa)",
      "declaracao": "Deve ser possível a qualquer visitante consultar as informações institucionais publicadas, sem necessidade de autenticação.",
      "entradas": "Acesso ao módulo público",
      "pre": "Existir ao menos um conteúdo institucional publicado",
      "proc": "Recupera os conteúdos publicados e os exibe com título, texto, fotos e vídeos",
      "saidas": "Lista e visualização dos conteúdos institucionais; mensagem informativa quando não houver conteúdo publicado",
      "pdf": true,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um visitante não autenticado, quando acessa o módulo público, então visualiza os conteúdos institucionais publicados.",
        "2. Dado um conteúdo removido pela coordenação, quando o visitante consulta, então ele não aparece."
      ],
      "rns": [
        "RN29"
      ],
      "rnfs": [
        "RNF02",
        "RNF07",
        "RNF09"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC07",
        "DEC11",
        "DEC12",
        "DEC13"
      ],
      "pens": [
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF16": {
      "nome": "Remover conteúdo institucional",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação remover um conteúdo institucional publicado.",
      "entradas": "Identificação do conteúdo a ser removido; confirmação da remoção",
      "pre": "Coordenador autenticado; conteúdo institucional existente",
      "proc": "Solicita confirmação, exclui o conteúdo e seus anexos do sistema",
      "saidas": "Confirmação da remoção; conteúdo deixa de ser exibido a qualquer usuário",
      "pdf": true,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um conteúdo publicado, quando a coordenação confirma a remoção, então ele deixa de ser exibido no módulo público e na área da coordenação.",
        "2. Dado um usuário sem perfil de coordenação, quando tenta remover, então o sistema nega a operação."
      ],
      "rns": [
        "RN26",
        "RN30"
      ],
      "rnfs": [
        "RNF02",
        "RNF05",
        "RNF07",
        "RNF09",
        "RNF10"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC02",
        "DEC03",
        "DEC07",
        "DEC08",
        "DEC11",
        "DEC12",
        "DEC13"
      ],
      "pens": [
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF17": {
      "nome": "Publicar evento",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação publicar um evento ou campeonato, informando: nome do evento ou competição, data, local, horário e descrição.",
      "entradas": "Obrigatórias: título, subtítulo, nome do evento/competição, data, horário (início e término), local, descrição, informação sobre alimentação (haverá ou não), informação sobre pesagem (haverá ou não, quando aplicável), informações de pagamento (se é cobrado, valor, data limite e meio de pagamento, como PIX). Opcionais: vídeo e imagens",
      "pre": "Coordenador autenticado",
      "proc": "Valida todos os campos obrigatórios, grava o evento, define seu estado conforme a data e o torna visível no módulo público",
      "saidas": "Evento exibido no módulo público; mensagem indicando os campos pendentes quando a validação falhar",
      "pdf": true,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um evento com todos os campos obrigatórios, quando a coordenação publica, então ele aparece no módulo público.",
        "2. Dado um evento com qualquer campo obrigatório vazio, quando a coordenação tenta publicar, então o sistema bloqueia a publicação e indica o que falta.",
        "3. Dado um evento sem vídeo, quando publicado, então o sistema o aceita normalmente."
      ],
      "rns": [
        "RN26",
        "RN31",
        "RN32",
        "RN33"
      ],
      "rnfs": [
        "RNF01",
        "RNF02",
        "RNF07",
        "RNF09"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC07",
        "DEC09",
        "DEC10",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC14"
      ],
      "pens": [
        "PEN01",
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN01: O subtítulo do evento é opcional (\"se houver\") nas reuniões de 21/10 e 30/10, mas a ficha do RF17 o lista entre as entradas obrigatórias",
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF18": {
      "nome": "Editar evento",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação editar os dados de um evento ou campeonato já publicado.",
      "entradas": "Qualquer dado do evento (data, horário, local, descrição, informações de pagamento, mídias etc.)",
      "pre": "Coordenador autenticado; evento já publicado",
      "proc": "Carrega os dados atuais, aplica as alterações, revalida os campos obrigatórios e grava",
      "saidas": "Evento atualizado exibido no módulo público",
      "pdf": true,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um evento com data incorreta, quando a coordenação corrige e salva, então a nova data é exibida no módulo público.",
        "2. Dado que a coordenação esvaziou um campo obrigatório, quando tenta salvar, então o sistema bloqueia a gravação."
      ],
      "rns": [
        "RN26",
        "RN31",
        "RN34"
      ],
      "rnfs": [
        "RNF01",
        "RNF02",
        "RNF07",
        "RNF09",
        "RNF10"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC07",
        "DEC08",
        "DEC09",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC14"
      ],
      "pens": [
        "PEN01",
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN01: O subtítulo do evento é opcional (\"se houver\") nas reuniões de 21/10 e 30/10, mas a ficha do RF17 o lista entre as entradas obrigatórias",
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF19": {
      "nome": "Remover evento",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação remover um evento ou campeonato.",
      "entradas": "Identificação do evento; confirmação da remoção",
      "pre": "Coordenador autenticado; evento existente",
      "proc": "Solicita confirmação e exclui o evento e seus anexos",
      "saidas": "Confirmação da remoção; evento deixa de ser exibido",
      "pdf": true,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um evento publicado, quando a coordenação confirma a remoção, então ele deixa de aparecer em qualquer listagem.",
        "2. Dado um usuário sem perfil de coordenação, quando tenta remover, então o sistema nega a operação."
      ],
      "rns": [
        "RN26",
        "RN30"
      ],
      "rnfs": [
        "RNF02",
        "RNF05",
        "RNF07",
        "RNF09",
        "RNF10"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC02",
        "DEC03",
        "DEC07",
        "DEC08",
        "DEC11",
        "DEC12",
        "DEC13"
      ],
      "pens": [
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF20": {
      "nome": "Consultar eventos",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível consultar os eventos ou campeonatos já publicados, em uma listagem que indique o estado de cada um.",
      "entradas": "Acesso à listagem de eventos",
      "pre": "Existir ao menos um evento publicado. Não exige autenticação para visitantes",
      "proc": "Recupera os eventos, calcula o estado de cada um e os exibe em lista; a coordenação acessa também as opções de editar e remover",
      "saidas": "Lista com título, data, local e estado (Em breve, Em andamento, Encerrado); detalhes completos ao selecionar um evento",
      "pdf": true,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um visitante, quando acessa a listagem, então vê eventos futuros, em andamento e encerrados, cada um com seu estado.",
        "2. Dado um evento cuja data já passou, quando listado, então aparece como Encerrado.",
        "3. Dado um coordenador autenticado, quando consulta um evento, então tem acesso às ações de editar e remover."
      ],
      "rns": [
        "RN33"
      ],
      "rnfs": [
        "RNF02",
        "RNF07",
        "RNF09"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Feito"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC07",
        "DEC10",
        "DEC11",
        "DEC12",
        "DEC13"
      ],
      "pens": [
        "PEN08"
      ],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": [
        "PEN08: O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno"
      ]
    },
    "RF21": {
      "nome": "Cadastrar aluno",
      "estado": "Detalhado",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação cadastrar um novo aluno, registrando seus dados cadastrais e a documentação exigida pelo CECP, por uma ficha de inscrição digital que substitui a ficha de papel.",
      "entradas": "Obrigatórios: nome completo; data de início; documento de identificação; nome da mãe; telefone da mãe; celular; tipo de escola; informação se há problema de saúde (sim/não); questionário de liberação respondido por completo; aceite do termo único (responsabilidade, uso de imagem e política de dados); graduação; modalidade, dias e horário.\nOpcionais: telefone do pai; telefone de emergência; nome da escola; foto do aluno; foto 3x4; atestado para prática de esporte; comprovante de residência; certificado de graduação; laudo.",
      "pre": "Coordenador autenticado",
      "proc": "Valida os campos obrigatórios, grava o aluno e seus anexos e o associa à turma",
      "saidas": "Aluno cadastrado; mensagem de erro indicando os campos obrigatórios ausentes",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado o preenchimento de todos os obrigatórios, quando a coordenação salva, então o aluno é cadastrado.",
        "2. Dado um campo obrigatório vazio, quando tenta salvar, então o sistema bloqueia e indica o campo.",
        "3. Dado o questionário incompleto, então o sistema não libera o cadastro.",
        "4. Dado problema de saúde = sim, então o sistema exibe descrição e anexo de laudos, sem exigir o laudo na hora.",
        "5. Dado um aluno sem laudo, certificado, foto 3x4 ou atestado, quando salva, então o cadastro é aceito."
      ],
      "rns": [
        "RN35",
        "RN36",
        "RN37",
        "RN38",
        "RN39",
        "RN40"
      ],
      "rnfs": [
        "RNF01",
        "RNF03",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC05"
      ],
      "pens": [
        "PEN03",
        "PEN04"
      ],
      "its": [
        "Iteração 10"
      ],
      "lacunas": [
        "PEN03: Conciliar o termo único do cadastro presencial (RN40, RF21) com a regra de que dados e imagem são aceites independentes na matrícula online (RN16, RF38 e RF39)",
        "PEN04: Completar a data e a fonte das decisões DEC04 e DEC05"
      ]
    },
    "RF22": {
      "nome": "Editar aluno",
      "estado": "Detalhado",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação editar os dados do aluno e acrescentar documentos posteriormente.",
      "entradas": "Qualquer campo da ficha; anexos (imagens digitalizadas, textos)",
      "pre": "Aluno cadastrado; coordenador autenticado",
      "proc": "Valida e atualiza os dados e armazena os novos anexos",
      "saidas": "Ficha atualizada; mensagem de erro se um campo obrigatório for esvaziado",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um aluno sem laudo, quando a coordenação anexa o laudo, então ele passa a constar na ficha.",
        "2. Dada a edição de um campo obrigatório para vazio, quando tenta salvar, então o sistema bloqueia."
      ],
      "rns": [
        "RN41",
        "RN42",
        "RN43"
      ],
      "rnfs": [
        "RNF03",
        "RNF06",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [
        "Iteração 10"
      ],
      "lacunas": []
    },
    "RF23": {
      "nome": "Consultar ficha do aluno",
      "estado": "Detalhado",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação consultar a ficha de um aluno, incluindo seus dados cadastrais e histórico de participação em turmas.",
      "entradas": "Seleção do aluno na listagem",
      "pre": "Coordenador autenticado",
      "proc": "Exibe a listagem (foto e nome completo) e, ao selecionar o aluno, o perfil com dados cadastrais, anexos e histórico de turmas",
      "saidas": "Ficha exibida; documentos baixáveis; pendências visíveis; contagem de alunos ativos e inativos",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um aluno, quando selecionado, então a ficha exibe dados cadastrais, anexos e histórico de participação em turmas.",
        "2. Dado um documento anexado, então a coordenação consegue baixá-lo.",
        "3. Dado um documento ausente, então a ficha deixa visível a pendência.",
        "4. Dada uma ficha aberta, então ela pode ser impressa."
      ],
      "rns": [
        "RN44",
        "RN45",
        "RN46"
      ],
      "rnfs": [
        "RNF01",
        "RNF06",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [
        "Iteração 10"
      ],
      "lacunas": []
    },
    "RF24": {
      "nome": "Inativar aluno",
      "estado": "Detalhado",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação marcar um aluno como inativo, preservando seu histórico no sistema.",
      "entradas": "Aluno; confirmação",
      "pre": "Aluno ativo; coordenador autenticado",
      "proc": "Exibe confirmação (\"Deseja inativar [nome]?\") e, ao confirmar, altera o status para inativo mantendo todos os dados",
      "saidas": "Aluno exibido como inativo; contagem de ativos/inativos atualizada",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um aluno ativo, quando a coordenação confirma a inativação, então ele passa a inativo com histórico preservado.",
        "2. Dada a ação cancelada na confirmação, então o status não muda."
      ],
      "rns": [
        "RN47",
        "RN01",
        "RN48"
      ],
      "rnfs": [
        "RNF03",
        "RNF04",
        "RNF05",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Feito"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC02",
        "DEC03"
      ],
      "pens": [],
      "its": [
        "Iteração 10"
      ],
      "lacunas": []
    },
    "RF25": {
      "nome": "Remover dados do aluno",
      "estado": "Rascunho",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação remover do sistema os dados de um aluno, mediante pedido do responsável legal ou do próprio aluno, caso ele tenha 18 anos ou mais.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "1, Não precisa ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: A remoção só é executada após confirmação e mediante pedido do responsável legal ou do próprio aluno, se ele tiver 18 anos ou mais. São removidos a identidade, o CPF e o comprovante de residência, e os demais registros são mantidos. A remoção é registrada em log."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF05",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC02"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF26": {
      "nome": "Registrar frequência",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento pedagógico e disciplinar do aluno",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação registrar a frequência dos alunos em cada aula de uma turma.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Para cada aula de uma turma, a presença ou falta de cada aluno associado é registrada com a data da aula e passa a constar no histórico de frequência do aluno."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF03",
        "RNF06",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF27": {
      "nome": "Consultar frequência",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento pedagógico e disciplinar do aluno",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação consultar o histórico de frequência de um aluno.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O histórico de frequência de um aluno lista as aulas com a data e a situação (presença ou falta) de cada uma."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF06",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF28": {
      "nome": "Emitir alerta de faltas críticas",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento pedagógico e disciplinar do aluno",
      "ator": "(a detalhar)",
      "declaracao": "O sistema deve gerar uma notificação para a coordenação quando um aluno atingir o número crítico de faltas definido pelo parâmetro configurado.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Quando o número de faltas de um aluno atinge o limite configurado (inicialmente 8 faltas), o sistema gera uma notificação para a coordenação. Abaixo do limite, nenhuma notificação é gerada."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF06",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF29": {
      "nome": "Registrar medida disciplinar",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento pedagógico e disciplinar do aluno",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação registrar uma medida disciplinar aplicada a um aluno, como advertência, suspensão ou desligamento, vinculada ao seu histórico.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: A medida (advertência, suspensão ou desligamento) só é salva após confirmação e passa a constar no histórico do aluno."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF05",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC02",
        "DEC03"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF30": {
      "nome": "Publicar aviso",
      "estado": "Rascunho",
      "cp": "CP6: Comunicação com voluntários e famílias",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação publicar avisos no módulo público.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O aviso publicado, com destinatário voluntários, familiares ou ambos, passa a ser exibido no módulo público."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF03",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF31": {
      "nome": "Consultar avisos",
      "estado": "Rascunho",
      "cp": "CP6: Comunicação com voluntários e famílias",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível aos voluntários e familiares consultar os avisos no módulo público.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Voluntários e familiares visualizam no módulo público os avisos publicados. Aviso removido não é exibido."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF06",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF32": {
      "nome": "Editar aviso",
      "estado": "Rascunho",
      "cp": "CP6: Comunicação com voluntários e famílias",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação editar um aviso para voluntários, familiares ou ambos já publicado no módulo público.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: As alterações salvas no aviso são exibidas atualizadas no módulo público."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF33": {
      "nome": "Remover aviso",
      "estado": "Rascunho",
      "cp": "CP6: Comunicação com voluntários e famílias",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação remover um aviso para voluntários, familiares ou ambos já publicado no módulo público.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Após a confirmação, o aviso deixa de ser exibido no módulo público."
      ],
      "rns": [],
      "rnfs": [],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF34": {
      "nome": "Consultar histórico de avisos",
      "estado": "Rascunho",
      "cp": "CP6: Comunicação com voluntários e famílias",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação consultar os avisos publicados anteriormente, incluindo seus destinatários e data de publicação.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "1, Não precisa ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O sistema lista os avisos publicados anteriormente com seus destinatários e a data de publicação."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF06",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF35": {
      "nome": "Acessar formulário de matrícula online",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível a qualquer interessado acessar o formulário de matrícula por link público, sem necessidade de login.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O formulário de matrícula abre pelo link público, sem necessidade de login."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF02",
        "RNF09"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF36": {
      "nome": "Preencher dados do aluno",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível o interesado inserir, no formulário, os dados do aluno (nome, data de nascimento, contato e modalidade ou turma de interesse).",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O formulário aceita nome, data de nascimento, contato e modalidade ou turma de interesse do aluno. O envio é bloqueado enquanto algum desses campos estiver vazio."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF03",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF37": {
      "nome": "Informar dados do responsável legal",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível inserir os dados do responsável legal (nome, contato e vínculo) quando o aluno tiver menos de 18 anos.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Quando a data de nascimento indica aluno menor de 18 anos, o formulário exige nome, contato e vínculo do responsável legal. Para aluno com 18 anos ou mais, esses dados não são exigidos."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF03",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF38": {
      "nome": "Registrar consentimento de dados pessoais",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível ao aluno, ou ao responsável legal no caso de menores, aceitar o termo de tratamento de dados pessoais, sendo o aceite condição para o envio e registrado com data, hora, versão do termo e identificação de quem aceitou.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O envio do formulário só é permitido após o aceite do termo de tratamento de dados pessoais. O aceite é registrado com data, hora, versão do termo e identificação de quem aceitou (aluno ou responsável legal)."
      ],
      "rns": [
        "RN16"
      ],
      "rnfs": [
        "RNF03",
        "RNF10",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [
        "PEN03"
      ],
      "its": [],
      "lacunas": [
        "PEN03: Conciliar o termo único do cadastro presencial (RN40, RF21) com a regra de que dados e imagem são aceites independentes na matrícula online (RN16, RF38 e RF39)"
      ]
    },
    "RF39": {
      "nome": "Registrar termo de uso de imagem",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível ao aluno ou ao responsável legal aceitar, separadamente do consentimento de dados, o termo de uso de imagem.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: O termo de uso de imagem é apresentado em item separado do consentimento de dados pessoais, e a resposta do aluno ou do responsável legal é registrada."
      ],
      "rns": [
        "RN16"
      ],
      "rnfs": [
        "RNF03",
        "RNF10",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [
        "PEN03"
      ],
      "its": [],
      "lacunas": [
        "PEN03: Conciliar o termo único do cadastro presencial (RN40, RF21) com a regra de que dados e imagem são aceites independentes na matrícula online (RN16, RF38 e RF39)"
      ]
    },
    "RF40": {
      "nome": "Informar pessoas autorizadas a retirar o aluno",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível inserir ao menos uma pessoa autorizada a retirar o aluno quando ele for menor de idade, com nome e contato, ou se o menor pode ir embora só.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "2, Poderia ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Para aluno menor de idade, o formulário exige ao menos uma pessoa autorizada, com nome e contato, ou a indicação de que o menor pode ir embora sozinho. Para aluno maior de idade, essa informação não é exigida."
      ],
      "rns": [],
      "rnfs": [
        "RNF01",
        "RNF03",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF41": {
      "nome": "Emitir comprovante de solicitação",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível ao solicitante receber, após o envio, um número de protocolo.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: Após o envio bem-sucedido do formulário, o sistema exibe ao solicitante um número de protocolo. Cada solicitação recebe um número de protocolo distinto."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF06"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC03"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF42": {
      "nome": "Analisar solicitações de matrícula",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Deve ser possível à coordenação consultar as solicitações recebidas e defini-las como aprovada, recusada ou em lista de espera.",
      "entradas": "(a detalhar)",
      "pre": "(a detalhar)",
      "proc": "(a detalhar)",
      "saidas": "(a detalhar)",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "Do backlog (10.1), a reescrever em Dado/Quando/Então: A coordenação consulta as solicitações recebidas e define cada uma como aprovada, recusada ou em lista de espera. O status definido é exibido atualizado na consulta."
      ],
      "rns": [],
      "rnfs": [
        "RNF03",
        "RNF05",
        "RNF10",
        "RNF11",
        "RNF13"
      ],
      "andamento": [
        [
          "Detalhamento",
          "Pendente"
        ],
        [
          "Design do usuário (protótipo)",
          "Pendente"
        ],
        [
          "Construção: início",
          "Pendente"
        ],
        [
          "Construção: implementação",
          "Pendente"
        ],
        [
          "Teste de aceite",
          "Pendente"
        ]
      ],
      "decs": [
        "DEC02",
        "DEC03"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    }
  },
  "rn": {
    "RN01": "Preservação de Histórico de Alunos: O aluno nunca pode ser excluído do sistema. A única ação permitida é a inativação, preservando todo o histórico de participação e frequência.",
    "RN02": "Assinatura Presencial Obrigatória: Toda inscrição, mesmo que iniciada remotamente via pré-cadastro / formulário online, exige a presença física do responsável legal para a assinatura presencial dos termos.",
    "RN03": "Autorização e Validade do Uso de Imagem: O uso da imagem do aluno depende de autorização assinada pelo responsável legal, com validade vinculada à sua permanência no projeto e por um período adicional após a saída.",
    "RN04": "Manutenção de Documentação Institucional: A documentação institucional da ONG (certidões OSCIP, FGTS, CND, CNPJ, Fazenda) precisa estar sempre atualizada para viabilizar a participação em editais de doação e recursos (pendências fiscais ou veiculares impedem a emissão de certidões).",
    "RN05": "Política de Aceite de Doações: A ONG evita recusar doações (mesmo quando o custo de frete ou conserto supera o benefício imediato) para preservar o relacionamento com os órgãos e parceiros doadores.",
    "RN06": "Comprovação Fotográfica em Prestação de Contas: Órgãos públicos doadores (ex.: Ministério Público) exigem registros fotográficos ou audiovisuais dos beneficiados como parte obrigatória da prestação de contas.",
    "RN07": "Documentação de Maior de Idade: Para alunos maiores de 18 anos, não é necessária a documentação nem a autorização de um responsável legal, visto que o próprio aluno responde legalmente por si.",
    "RN08": "Tolerância para Atestado Médico: Existe uma tolerância de aproximadamente 30 a 35 dias para a entrega do atestado médico para prática de esportes, em razão do tempo necessário para consulta médica.",
    "RN09": "Autorização para Retirada de Menores: A retirada de alunos menores de idade deve seguir estritamente as autorizações e registros formais cadastrados na instituição.",
    "RN10": "Indicação Obrigatória de Pessoas Autorizadas a Retirar Menores: No cadastro de alunos menores de idade, é obrigatório informar o nome e contato de pelo menos uma pessoa autorizada a retirar o menor.",
    "RN11": "Atualização de Autorização de Retirada: Alterações nas pessoas autorizadas a retirar um menor de idade precisam ser formalmente comunicadas e atualizadas no registro da instituição.",
    "RN12": "Manutenção de Domínio: O domínio do site institucional da ONG permanece ativo.",
    "RN13": "Diversidade de Recursos: O recebimento de recursos ocorre por múltiplos canais (doações diretas, bens físicos e parcerias/ofícios).",
    "RN14": "Fluxo de Prestação de Contas: A prestação de contas de recursos envolve orçamentos prévios, aprovação, nota fiscal e registros fotográficos/audiovisuais.",
    "RN15": "Vínculo Socioeducacional e Permanência: A regra de negócio central do CECP condiciona a permanência e a evolução do aluno no projeto social esportivo ao acompanhamento direto de sua frequência nas aulas do CECP e de seu desempenho/assiduidade na escola formal de origem.",
    "RN16": "Separação de Consentimento de Dados e Termo de Imagem: O aceite do termo de tratamento de dados pessoais (LGPD) e do termo de uso de imagem são tratados de forma independente. A recusa do termo de imagem impede a realização da matrícula.",
    "RN17": "O encerramento é total; para voltar à área de coordenação é preciso informar usuário e senha novamente.",
    "RN18": "Na reunião o cliente admitiu redirecionar também para um modo público; a tela de login é o comportamento adotado.",
    "RN19": "Não há autocadastro; a tela de login não oferece opção de cadastro.",
    "RN20": "Existe um único nível de acesso (coordenador).",
    "RN21": "O acesso inicial é feito por um usuário administrador padrão, entregue ao responsável do projeto, que repassa aos demais.",
    "RN22": "O sistema inicia vazio, então cadastrar turma é a primeira ação necessária.",
    "RN23": "Modalidade, dias e horários fazem parte da ficha do aluno.",
    "RN24": "A listagem de alunos segue o padrão mostrado na reunião (foto e nome completo).",
    "RN25": "Todo conteúdo institucional deve ter título.",
    "RN26": "Apenas a coordenação pode publicar, editar e remover conteúdos institucionais e eventos; professores solicitam à coordenação.",
    "RN27": "Não há conjunto fixo de campos além do título (exemplo a publicação pode ser só uma imagem que já contém todas as informações).",
    "RN28": "O sistema não precisa sinalizar ao visitante que o conteúdo foi editado; a coordenação é responsável por comunicar mudanças relevantes (por exemplo, publicando um novo aviso institucional).",
    "RN29": "A consulta é pública e não exige login nem cadastro.",
    "RN30": "A remoção é total e definitiva; o conteúdo deixa de ser visível para todos.",
    "RN31": "O evento só pode ser publicado com todos os campos obrigatórios preenchidos; não se publica evento vago.",
    "RN32": "O vídeo é opcional.",
    "RN33": "O estado do evento é Em breve, Em andamento ou Encerrado.",
    "RN34": "A coordenação é responsável por avisar os interessados sobre alterações (por exemplo, publicando um aviso institucional); o sistema não precisa sinalizar a edição ao visitante.",
    "RN35": "Sem o questionário respondido, o cadastro não é liberado.",
    "RN36": "A graduação é obrigatória, mas o certificado não é exigido no ato; o aluno é cadastrado com a graduação declarada e o certificado é anexado depois. A coordenação cobra o certificado de qualquer faixa acima da branca; sem ele, o aluno não é graduado.",
    "RN37": "O aluno com problema de saúde ou necessidade especial deve ter isso declarado no cadastro. O laudo pode ser entregue depois, em prazo definido pela coordenação (ex.: duas semanas), sob pena de suspensão da matrícula. O prazo é controle manual da coordenação.",
    "RN38": "Ao marcar \"sim\" para problema de saúde, o sistema exibe campos para descrição e anexo de laudos; ao marcar \"não\", segue o fluxo normal.",
    "RN39": "O cadastro pode ser concluído com documentos faltantes, desde que os campos obrigatórios estejam preenchidos.",
    "RN40": "O uso de imagem deve aparecer com destaque, conforme a LGPD, e o cliente quer o termo de responsabilidade, de imagem e de dados juntos em um único termo. O cliente enviará o modelo ou pedirá a remodelagem ao time.",
    "RN41": "A edição serve principalmente para completar documentos pendentes (laudo, certificado, atestado, foto 3x4, comprovante).",
    "RN42": "Os documentos podem ser anexados como imagem digitalizada ou pdf.",
    "RN43": "A edição preserva as regras de obrigatoriedade do cadastro (RF21).",
    "RN44": "A consulta serve, por exemplo, para checar a documentação na época da graduação.",
    "RN45": "A ficha pode ser impressa; o sistema não bloqueia a impressão.",
    "RN46": "O sistema exibe a contagem de ativos e inativos.",
    "RN47": "A inativação é manual, feita pela coordenação (ex.: aluno muito faltoso); o sistema não inativa sozinho.",
    "RN48": "A confirmação é exibida antes da inativação (cliente aprovou a tela de confirmação, pedida para evitar ações acidentais)."
  },
  "rnf": {
    "RNF01": {
      "nome": "Facilidade de aprendizado",
      "desc": "Interface que permite ao usuário realizar tarefas sem precisar de muito tempo de aprendizado ou treinamento para voluntários sem experiência técnica (CP1, CP3, CP4, CP5).",
      "crit": "Usuários novatos no sistema deverão conseguir realizar as tarefas após de se familiarizarem com o sistema por no máximo 8 minutos. 80% dos usuários devem cumprir as tarefas para ser aceito."
    },
    "RNF02": {
      "nome": "Interface responsiva do módulo público",
      "desc": "O módulo público deve adaptar sua interface ao tamanho da tela, mantendo a legibilidade e a organização dos conteúdos em diferentes resoluções.",
      "crit": "Conteúdos de divulgação institucional devem ser exibidos sem sobreposição ou corte em resoluções ≥ 360px."
    },
    "RNF03": {
      "nome": "Feedback em ações críticas",
      "desc": "Feedback ao usuário em ações críticas, como registrar frequência, aplicar medida disciplinar e inativar aluno ou turma.",
      "crit": "Mensagem de sucesso/erro exibida em até 2s após a ação (ex.: registrar frequência, aplicar medida disciplinar)."
    },
    "RNF04": {
      "nome": "Preservação de histórico",
      "desc": "Preservação de histórico ao inativar turma ou aluno.",
      "crit": "Registros preservados no banco após a inativação, permanecendo consultáveis na ficha/histórico."
    },
    "RNF05": {
      "nome": "Confirmação antes de ações críticas",
      "desc": "O sistema deve solicitar confirmação antes da execução de ações críticas que possam alterar ou inativar registros relevantes.",
      "crit": "Caixa de confirmação exibida antes de inativar turma, inativar aluno ou registrar medida disciplinar."
    },
    "RNF06": {
      "nome": "Tempo de resposta das consultas internas",
      "desc": "Resposta das consultas internas em até 3s (ficha do aluno, frequência, turmas).",
      "crit": "P95 das requisições autenticadas ≤ 3s sob carga normal."
    },
    "RNF07": {
      "nome": "Carregamento da página pública",
      "desc": "Carregamento da página pública em até 5s (CP2, CP3).",
      "crit": "LCP ≤ 5s em conexão 3G, medido pelo Lighthouse."
    },
    "RNF08": {
      "nome": "Acesso simultâneo de usuários autenticados",
      "desc": "O sistema deve suportar o acesso simultâneo de usuários autenticados sem ultrapassar os limites de desempenho definidos para as operações internas.",
      "crit": "Com 10 sessões autenticadas simultâneas, o P95 das requisições deve permanecer ≤ 3s sob carga normal."
    },
    "RNF09": {
      "nome": "Logs de operações críticas",
      "desc": "Logs de operações críticas.",
      "crit": "Toda criação, edição e inativação (turma, aluno, doação, medida disciplinar) registrada com timestamp e usuário responsável."
    },
    "RNF10": {
      "nome": "Compatibilidade com navegadores modernos",
      "desc": "O sistema deve utilizar padrões e tecnologias web atuais e amplamente adotados, garantindo compatibilidade com navegadores modernos.",
      "crit": "Compatível com Chrome, Firefox e Safari nas últimas 2 versões."
    },
    "RNF11": {
      "nome": "Controle de acesso por perfil",
      "desc": "Controle de acesso por perfil (coordenação, professor/voluntário, família).",
      "crit": "Rotas administrativas retornam 401/403 para requisições sem perfil autorizado."
    },
    "RNF12": {
      "nome": "Proteção de senhas e dados sensíveis",
      "desc": "Senhas com hash e dados sensíveis criptografados.",
      "crit": "Nenhuma senha armazenada em texto claro; auditoria por inspeção de banco."
    },
    "RNF13": {
      "nome": "Conformidade com a LGPD",
      "desc": "O sistema deve tratar os dados pessoais de acordo com os princípios, direitos dos titulares e requisitos de segurança e tratamento estabelecidos pela Lei nº 13.709/2018 (LGPD).",
      "crit": "O sistema deve permitir o atendimento às solicitações aplicáveis dos titulares ou responsáveis legais relacionadas aos seus dados pessoais, incluindo solicitação de eliminação quando cabível, além de classificar e proteger dados pessoais sensíveis conforme a LGPD."
    }
  },
  "dec": [
    {
      "id": "DEC01",
      "data": "08/10/2026 (data registrada na própria ata; o arquivo está nomeado como 09/10)",
      "texto": "O MVP foi refeito: após explicar o conceito de MVP ao cliente, o MoSCoW foi reclassificado, porque a primeira priorização (24/09) deixou cerca de 36 dos 42 requisitos no MVP. Os valores de negócio seguem vigentes; o conjunto do MVP foi substituído pela DEC03",
      "rfs": [],
      "fonte": "Priorização, ata 09/10"
    },
    {
      "id": "DEC02",
      "data": "22/09/2026, reforçada em 24/09/2026 e prototipada em 30/10/2026",
      "texto": "Ações críticas (inativar aluno ou turma, aplicar medida disciplinar, remover) exigem confirmação antes de serem executadas (RNF05). Para conteúdo institucional e eventos, a tela de confirmação de remoção foi apresentada no protótipo",
      "rfs": [
        "RF05",
        "RF16",
        "RF19",
        "RF24",
        "RF25",
        "RF29",
        "RF42"
      ],
      "fonte": "Ata 22/09, ata 24/09, ata 30/10"
    },
    {
      "id": "DEC03",
      "data": "30/10/2026",
      "texto": "O MVP foi redefinido pela matriz 4 × 4 final: entram os RFs com valor de negócio 3 ou 4 e esforço técnico 1 ou 2 (18 de 43). Saem do MVP e viram pós-MVP os RFs com valor alto e esforço alto. O cliente validou esse escopo na reunião de 30/10",
      "rfs": [
        "RF00",
        "RF01",
        "RF02",
        "RF03",
        "RF06",
        "RF07",
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20",
        "RF21",
        "RF22",
        "RF23",
        "RF24",
        "RF29",
        "RF35",
        "RF36",
        "RF37",
        "RF38",
        "RF39",
        "RF41",
        "RF42"
      ],
      "fonte": "Backlog 10.2.2, priorização, ata 30/10"
    },
    {
      "id": "DEC04",
      "data": "A confirmar",
      "texto": "Após encerrar a sessão, o sistema redireciona para a tela de login (o cliente admitiu também o modo público)",
      "rfs": [
        "RF00"
      ],
      "fonte": "A confirmar (falta a data da reunião)"
    },
    {
      "id": "DEC05",
      "data": "A confirmar",
      "texto": "Termo único (responsabilidade, imagem e dados) no cadastro de aluno",
      "rfs": [
        "RF21"
      ],
      "fonte": "A confirmar (falta a data da reunião e o modelo de termo do cliente)"
    },
    {
      "id": "DEC06",
      "data": "21/10/2026",
      "texto": "Conteúdo institucional: o único campo obrigatório é o título. Texto, imagem e vídeo são opcionais; áudio não é necessário. A ONG não tem modelo nem regra de formato para as publicações",
      "rfs": [
        "RF13",
        "RF14"
      ],
      "fonte": "Ata 21/10, RN25, RN27"
    },
    {
      "id": "DEC07",
      "data": "21/10/2026",
      "texto": "Somente a coordenação publica, edita e remove conteúdo institucional e eventos; professores solicitam à coordenação. A consulta é pública, sem login nem cadastro",
      "rfs": [
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ],
      "fonte": "Ata 21/10, RN26, RN29"
    },
    {
      "id": "DEC08",
      "data": "21/10/2026",
      "texto": "A remoção é total e definitiva. O sistema não sinaliza ao visitante que um conteúdo ou evento foi editado; a coordenação é responsável por avisar os interessados, por exemplo com um aviso institucional",
      "rfs": [
        "RF14",
        "RF16",
        "RF18",
        "RF19"
      ],
      "fonte": "Ata 21/10, RN28, RN30, RN34"
    },
    {
      "id": "DEC09",
      "data": "21/10/2026",
      "texto": "Um evento só é publicado com todos os campos obrigatórios preenchidos, para não divulgar eventos vagos. O vídeo é opcional. Quando o evento é cobrado, valor, data limite e meio de pagamento (como Pix) são obrigatórios",
      "rfs": [
        "RF17",
        "RF18"
      ],
      "fonte": "Ata 21/10, RN31, RN32"
    },
    {
      "id": "DEC10",
      "data": "21/10/2026",
      "texto": "Os estados de um evento são em breve, em andamento e encerrado, sem outros. A coordenação tem uma lista com todos os eventos, para consultar e editar",
      "rfs": [
        "RF17",
        "RF20"
      ],
      "fonte": "Ata 21/10, RN33"
    },
    {
      "id": "DEC11",
      "data": "21/10/2026",
      "texto": "Identidade visual do módulo público: cores predominantes preto, branco e vermelho, com amarelo para destaque. O cliente enviará a logo atualizada",
      "rfs": [
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ],
      "fonte": "Ata 21/10, ata 09/10"
    },
    {
      "id": "DEC12",
      "data": "30/10/2026",
      "texto": "O protótipo das telas de conteúdo institucional e eventos (18 telas) foi aprovado pelo cliente, e a construção pode começar a partir de 02/11/2026, com previsão de 3 a 4 semanas para o MVP",
      "rfs": [
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ],
      "fonte": "Ata 30/10, evidência do design do usuário"
    },
    {
      "id": "DEC13",
      "data": "30/10/2026",
      "texto": "As telas da coordenação (publicar, editar, listar e remover) serão feitas somente para computador. Para celular, há quatro telas públicas: página institucional, publicação, lista de eventos e evento",
      "rfs": [
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ],
      "fonte": "Ata 30/10"
    },
    {
      "id": "DEC14",
      "data": "30/10/2026",
      "texto": "No formulário de evento, o botão de publicar fica desabilitado enquanto faltar campo obrigatório. Evento gratuito não exibe as informações de pagamento",
      "rfs": [
        "RF17",
        "RF18"
      ],
      "fonte": "Ata 30/10"
    }
  ],
  "pen": [
    {
      "id": "PEN01",
      "texto": "O subtítulo do evento é opcional (\"se houver\") nas reuniões de 21/10 e 30/10, mas a ficha do RF17 o lista entre as entradas obrigatórias",
      "rfs": [
        "RF17",
        "RF18"
      ],
      "acao": "Ajustar a ficha e o protótipo, ou confirmar com o cliente"
    },
    {
      "id": "PEN02",
      "texto": "Definir se alunos inativos aparecem na lista da turma",
      "rfs": [
        "RF07"
      ],
      "acao": "Marcada como [PENDENTE] na ficha"
    },
    {
      "id": "PEN03",
      "texto": "Conciliar o termo único do cadastro presencial (RN40, RF21) com a regra de que dados e imagem são aceites independentes na matrícula online (RN16, RF38 e RF39)",
      "rfs": [
        "RF21",
        "RF38",
        "RF39"
      ],
      "acao": "Confirmar com o cliente se são fluxos distintos"
    },
    {
      "id": "PEN04",
      "texto": "Completar a data e a fonte das decisões DEC04 e DEC05",
      "rfs": [
        "RF00",
        "RF21"
      ],
      "acao": "Localizar a ata ou o áudio da reunião e o modelo de termo do cliente"
    },
    {
      "id": "PEN06",
      "texto": "Reconciliar as notas de esforço da seção 5 da priorização com a posição de esforço da matriz final (30 RFs divergem do arredondamento do ET)",
      "rfs": [],
      "acao": "Atualizar os votos ou documentar o critério usado na matriz"
    },
    {
      "id": "PEN07",
      "texto": "Confirmar as datas das reuniões de 21/10 (detalhamento) e 30/10 (design do usuário), deduzidas dos nomes de arquivo e da data de publicação do vídeo",
      "rfs": [],
      "acao": "Conferir com o vídeo e o calendário e corrigir as atas, se preciso"
    },
    {
      "id": "PEN08",
      "texto": "O cliente deve enviar a logo atualizada e mostrar o protótipo à Sandra, trazendo o retorno",
      "rfs": [
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ],
      "acao": "Aguardar o cliente; cobrar na conversa de segunda-feira (02/11/2026)"
    },
    {
      "id": "PEN09",
      "texto": "Regra citada em 30/10 para turmas com limite de 30 alunos e inscrição prévia da pessoa ficou pouco clara",
      "rfs": [
        "RF03",
        "RF06"
      ],
      "acao": "Validar no detalhamento de turmas"
    }
  ],
  "pen_enc": [
    {
      "id": "PEN05",
      "texto": "Data da reunião de priorização (08/10 no texto, 09/10 nos arquivos)",
      "rfs": [],
      "acao": "Encerrada em 03/11/2026: a própria ata registra 08/10/2026; 09/10 é só o nome do arquivo. A DEC01 foi atualizada."
    }
  ],
  "its": [
    {
      "nome": "Iteração 0",
      "periodo": "",
      "foco": "Entrega unidade 1 (08/09)",
      "entregas": "Documento de visão versão 1.1 e git pages",
      "rfs": []
    },
    {
      "nome": "Iteração 1",
      "periodo": "20/09/2026 - 27/09/2026",
      "foco": "Planejamento de Requisitos: Elicitação e ajuste da lista de RFs e RNFs, preparação para validação",
      "entregas": "Atualização da documentação do git pages com a prévia dos principais requisitos",
      "rfs": []
    },
    {
      "nome": "Iteração 2",
      "periodo": "28/09/2026 - 04/10/2026",
      "foco": "Planejamento de Requisitos: Validação final da lista de RFs e RNFs (29/09); avaliação de valor de negócio com o cliente e de esforço técnico pela equipe; construção da matriz 4×4; definição do MVP",
      "entregas": "Lista validada de RFs/RNFs; matriz 4×4 de priorização; lista de RFs selecionados para o MVP",
      "rfs": []
    },
    {
      "nome": "Iteração 3",
      "periodo": "05/10/2026 - 11/10/2026",
      "foco": "Planejamento de Requisitos: definição do backlog, DoR e DoD com base no MVP validado; preparação da documentação para a entrega da Unidade 2",
      "entregas": "Backlog, DoR e DoD definidos",
      "rfs": []
    },
    {
      "nome": "Iteração 4",
      "periodo": "12/10/2026 - 18/10/2026",
      "foco": "Entrega da Unidade 2 (13/10)",
      "entregas": "Documento de visão versão 1.2; requisitos detalhados de turmas e conteúdo institucional/eventos",
      "rfs": []
    },
    {
      "nome": "Iteração 5",
      "periodo": "19/10/2026 - 25/10/2026",
      "foco": "Planejamento: detalhamento dos requisitos do módulo público (publicações e eventos)\n\nDesign do Usuário: Protótipo da tela de publicação, edição e consulta de conteúdo institucional e eventos; protótipo inicial do dashboard de gestão de turmas\n\nConstrução: início da implementação do módulo de conteúdo institucional/eventos",
      "entregas": "Protótipos de conteúdo institucional/eventos e de dashboard de turmas; requisitos detalhados de alunos e acompanhamento disciplinar",
      "rfs": [
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ]
    },
    {
      "nome": "Iteração 6",
      "periodo": "26/10/2026 - 01/11/2026",
      "foco": "Planejamento: detalhamento de todos os requisitos restantes do MVP\n\nConstrução: continuação da implementação do módulo de conteúdo institucional/eventos\n\nTransição: teste de aceite dos requisitos implementados nesta construção",
      "entregas": "Módulo de conteúdo institucional/eventos e dashboard de turmas funcionais; protótipo da ficha do aluno",
      "rfs": [
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ]
    },
    {
      "nome": "Iteração 7",
      "periodo": "02/11/2026 - 08/11/2026",
      "foco": "Design do Usuário: Prototipação das telas de autenticação.\n\nConstrução: implementação dos RF00, RF01 e RF02\n\nTransição: teste de aceite dos requisitos implementados nesta construção",
      "entregas": "RF00, RF01 e RF02 implementados e testados",
      "rfs": [
        "RF00",
        "RF01",
        "RF02"
      ]
    },
    {
      "nome": "Iteração 8",
      "periodo": "09/11/2026 - 15/11/2026",
      "foco": "Design do Usuário: Prototipação das telas de gestão de turmas.\n\nConstrução: implementação dos RF03, RF06 e RF07\n\nTransição: teste de aceite dos requisitos implementados nesta construção; treinamento inicial e capacitação da ONG",
      "entregas": "RF03, RF06 e RF07 implementados e testados",
      "rfs": [
        "RF03",
        "RF06",
        "RF07"
      ]
    },
    {
      "nome": "Iteração 9",
      "periodo": "16/11/2026 - 22/11/2026",
      "foco": "Entrega da unidade 3 (17/11)\n\nConstrução: sem requisitos novos do MVP; o formulário de matrícula online (RF35 a RF39) é incremento pós-MVP e só entra se houver capacidade e validação do cliente (DEC03)",
      "entregas": "Nova versão do documento de visão 1.3; issues anteriores fechadas",
      "rfs": []
    },
    {
      "nome": "Iteração 10",
      "periodo": "23/11/2026 - 29/11/2026",
      "foco": "Construção: cadastro, edição, inativação e remoção de dados do aluno (ficha do aluno)\n\nTransição: testes de segurança; validação com a coordenação; testes de aceite do MVP completo; treinamento final",
      "entregas": "MVP concluído e validado; ficha de aluno funcional, com cadastro, histórico e tratamento de dados críticos",
      "rfs": [
        "RF21",
        "RF22",
        "RF23",
        "RF24"
      ]
    },
    {
      "nome": "Iteração 11",
      "periodo": "30/11/2026 - 01/12/2026",
      "foco": "Entrega da unidade 4 (01/12)\n\nTransição: correções finais a partir da validação, último deploy, finalização do projeto",
      "entregas": "Última versão do documento de visão 1.4; projeto entregue",
      "rfs": []
    }
  ],
  "cron_nota": "Critério de transição entre fases: as macrofases de Design, Construção e Transição do RAD só entram em foco a partir da Iteração 5, após a validação formal dos requisitos, priorização via matriz 4×4, definição do MVP e formalização do backlog/DoR/DoD na Entrega da Unidade 2 (13/10). Até lá, o esforço da equipe está inteiramente concentrado em Planejamento de Requisitos. O cronograma é uma previsão e que pode sofrer mudanças no decorrer do desenvolvimento para melhor adequação do projeto.",
  "alertas": [
    {
      "tipo": "Decisão sem fonte ou data",
      "texto": "DEC04 ainda precisa de data ou fonte"
    },
    {
      "tipo": "Decisão sem fonte ou data",
      "texto": "DEC05 ainda precisa de data ou fonte"
    }
  ]
};
