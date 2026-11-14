window.ESCOPO = {
  "rfs": {
    "RF00": {
      "nome": "Encerrar sessão",
      "estado": "Validado",
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
          "Feito"
        ],
        [
          "Construção: início",
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC04",
        "DEC19",
        "DEC20"
      ],
      "pens": [],
      "its": [
        "Iteração 7"
      ],
      "lacunas": []
    },
    "RF01": {
      "nome": "Autenticar usuário",
      "estado": "Validado",
      "cp": "Acesso e controle de usuários",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível ao coordenador acessar a área de coordenação informando usuário e senha.",
      "entradas": "Usuário (formato CECP + sequência numérica, por exemplo CECP0001); senha",
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
          "Feito"
        ],
        [
          "Construção: início",
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC19",
        "DEC20",
        "DEC28"
      ],
      "pens": [],
      "its": [
        "Iteração 7"
      ],
      "lacunas": []
    },
    "RF02": {
      "nome": "Controlar acesso",
      "estado": "Validado",
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
          "Feito"
        ],
        [
          "Construção: início",
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC19",
        "DEC20",
        "DEC28",
        "DEC29"
      ],
      "pens": [],
      "its": [
        "Iteração 7"
      ],
      "lacunas": []
    },
    "RF03": {
      "nome": "Cadastrar turma",
      "estado": "Validado",
      "cp": "CP1: Gestão e acompanhamento de turmas",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação cadastrar turmas.",
      "entradas": "Modalidade; dias da semana; horário de início; horário de término. Todos obrigatórios, como no protótipo apresentado em 10/11/2026. Nome da turma e instrutor não fazem parte do protótipo; não há limite de alunos por turma (DEC24)",
      "pre": "Coordenador autenticado",
      "proc": "Valida os campos obrigatórios e grava a turma",
      "saidas": "Turma disponível para associação de alunos e exibida na lista de turmas (modalidade, dias, horário e quantidade de alunos); mensagem indicando o campo obrigatório ausente",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dada uma turma com modalidade e horários, quando salva, então ela fica disponível para seleção no cadastro do aluno.",
        "2. Dados campos obrigatórios ausentes, quando tenta salvar, então o sistema bloqueia e informa qual campo falta.",
        "3. Dada a lista de turmas, então cada turma mostra modalidade, dias, horário e quantidade de alunos."
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
        "DEC20",
        "DEC24",
        "DEC26"
      ],
      "pens": [],
      "its": [
        "Iteração 8"
      ],
      "lacunas": []
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
        "DEC02",
        "DEC17"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF06": {
      "nome": "Associar aluno à turma",
      "estado": "Validado",
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
        "2. Dado o cadastro de um aluno, então é possível escolher a turma na própria ficha.",
        "3. Dada uma turma sem alunos, quando a coordenação seleciona um aluno já cadastrado, então ele passa a constar na turma."
      ],
      "rns": [
        "RN23",
        "RN22"
      ],
      "rnfs": [
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
        "DEC17",
        "DEC20",
        "DEC24",
        "DEC26"
      ],
      "pens": [],
      "its": [
        "Iteração 8"
      ],
      "lacunas": []
    },
    "RF07": {
      "nome": "Consultar alunos de uma turma",
      "estado": "Validado",
      "cp": "CP1: Gestão e acompanhamento de turmas",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação consultar os alunos que fazem parte de uma turma específica.",
      "entradas": "Seleção da turma",
      "pre": "Turma cadastrada; coordenador autenticado",
      "proc": "Busca os alunos associados à turma e exibe a listagem; ao selecionar um aluno, abre a ficha (RF23)",
      "saidas": "Lista de alunos da turma (foto e nome completo)",
      "pdf": false,
      "pendente": 0,
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
        "DEC20",
        "DEC23",
        "DEC26",
        "DEC29"
      ],
      "pens": [],
      "its": [
        "Iteração 8"
      ],
      "lacunas": []
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
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC06",
        "DEC07",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC19",
        "DEC22"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
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
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC06",
        "DEC07",
        "DEC08",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC19",
        "DEC22"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
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
        "2. Dado um conteúdo removido pela coordenação, quando o visitante consulta, então ele não aparece.",
        "3. Dada uma imagem exibida, quando o visitante clica nela, então ela é mostrada ampliada (pedido do cliente em 10/11, ainda a construir)."
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
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC07",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC19",
        "DEC21",
        "DEC22"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
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
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC02",
        "DEC03",
        "DEC07",
        "DEC08",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC17",
        "DEC19",
        "DEC22"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
    },
    "RF17": {
      "nome": "Publicar evento",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação publicar um evento ou campeonato, informando: nome do evento ou competição, data, local, horário e descrição.",
      "entradas": "Obrigatórias: título, nome do evento/competição, data, horário (início e término), local, descrição, informação sobre alimentação (haverá ou não), informação sobre pesagem (haverá ou não, quando aplicável), informações de pagamento (se é cobrado, valor, data limite e meio de pagamento, como PIX). Opcionais: subtítulo, vídeo e imagens",
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
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
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
        "DEC14",
        "DEC19",
        "DEC22",
        "DEC27"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
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
        "2. Dado que a coordenação esvaziou um campo obrigatório, quando tenta salvar, então o sistema bloqueia a gravação.",
        "3. Dado um evento sem subtítulo, quando a coordenação salva, então a gravação é aceita, porque o subtítulo é opcional (DEC27)."
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
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
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
        "DEC14",
        "DEC19",
        "DEC22",
        "DEC27"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
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
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC02",
        "DEC03",
        "DEC07",
        "DEC08",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC17",
        "DEC19",
        "DEC22"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
    },
    "RF20": {
      "nome": "Consultar eventos",
      "estado": "Validado",
      "cp": "CP3: Gestão de conteúdo institucional",
      "ator": "Visitante (consulta pública, sem login) e coordenação (acesso às ações de editar e remover)",
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
        "3. Dado um coordenador autenticado, quando consulta um evento, então tem acesso às ações de editar e remover.",
        "4. Dada uma imagem exibida, quando o visitante clica nela, então ela é mostrada ampliada (pedido do cliente em 10/11, ainda a construir)."
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
          "Feito"
        ],
        [
          "Construção: implementação",
          "Feito"
        ],
        [
          "Teste de aceite",
          "Feito"
        ]
      ],
      "decs": [
        "DEC03",
        "DEC07",
        "DEC10",
        "DEC11",
        "DEC12",
        "DEC13",
        "DEC19",
        "DEC21",
        "DEC22"
      ],
      "pens": [],
      "its": [
        "Iteração 5",
        "Iteração 6"
      ],
      "lacunas": []
    },
    "RF21": {
      "nome": "Cadastrar aluno",
      "estado": "Validado",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação cadastrar um novo aluno, registrando seus dados cadastrais e a documentação exigida pelo CECP, por uma ficha de inscrição digital que substitui a ficha de papel.",
      "entradas": "Obrigatórios: nome completo; data de início; documento de identificação; nome da mãe; telefone da mãe; celular; tipo de escola; informação se há problema de saúde (sim/não); questionário de liberação respondido por completo; aceite do termo único (responsabilidade, uso de imagem e política de dados); graduação; modalidade, dias e horário.\nOpcionais: telefone do pai; telefone de emergência; nome da escola; foto do aluno; foto 3x4; atestado para prática de esporte; comprovante de residência; certificado de graduação; laudo.",
      "pre": "Coordenador autenticado; turma cadastrada (RN22)",
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
        "RN08",
        "RN40"
      ],
      "rnfs": [
        "RNF01",
        "RNF03",
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
        "DEC05",
        "DEC18",
        "DEC20",
        "DEC25",
        "DEC26",
        "DEC32"
      ],
      "pens": [],
      "its": [
        "Iteração 10"
      ],
      "lacunas": []
    },
    "RF22": {
      "nome": "Editar aluno",
      "estado": "Validado",
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
        "DEC20",
        "DEC26"
      ],
      "pens": [],
      "its": [
        "Iteração 10"
      ],
      "lacunas": []
    },
    "RF23": {
      "nome": "Consultar ficha do aluno",
      "estado": "Validado",
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
        "DEC20",
        "DEC26",
        "DEC29"
      ],
      "pens": [],
      "its": [
        "Iteração 10"
      ],
      "lacunas": []
    },
    "RF24": {
      "nome": "Inativar aluno",
      "estado": "Validado",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação marcar um aluno como inativo, preservando seu histórico no sistema.",
      "entradas": "Aluno; confirmação",
      "pre": "Aluno ativo; coordenador autenticado",
      "proc": "Exibe confirmação (\"Deseja inativar [nome]?\") e, ao confirmar, altera o status para inativo mantendo todos os dados",
      "saidas": "Aluno exibido como inativo, com a data da inativação; aviso de que a inativação foi feita; contagem de ativos/inativos atualizada",
      "pdf": false,
      "pendente": 0,
      "moscow": "3, Deveria ter",
      "entrega": "MVP",
      "criterios": [
        "1. Dado um aluno ativo, quando a coordenação confirma a inativação, então ele passa a inativo com histórico preservado.",
        "2. Dada a ação cancelada na confirmação, então o status não muda.",
        "3. Dado um aluno inativado, então a ficha mostra a data em que ele foi inativado."
      ],
      "rns": [
        "RN47",
        "RN01",
        "RN48"
      ],
      "rnfs": [
        "RNF03",
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
        "DEC17",
        "DEC20",
        "DEC26"
      ],
      "pens": [
        "PEN23"
      ],
      "its": [
        "Iteração 10"
      ],
      "lacunas": [
        "PEN23: Não há regra nem RF para reativar um aluno inativo (por exemplo, um aluno que volta ao projeto). A lacuna apareceu ao representar o ciclo de vida do aluno (seção 5.3)"
      ]
    },
    "RF25": {
      "nome": "Remover dados do aluno",
      "estado": "Rascunho",
      "cp": "CP4: Cadastro e histórico de alunos",
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação remover do sistema os documentos de identificação de um aluno (identidade, CPF e comprovante de residência), mediante pedido do responsável legal ou do próprio aluno, caso ele tenha 18 anos ou mais. Os demais registros (histórico de participação e frequência) são mantidos, porque o aluno não é excluído (RN01).",
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
        "DEC17"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF26": {
      "nome": "Registrar frequência",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento de frequência e disciplinar do aluno",
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
      "decs": [
        "DEC15"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF27": {
      "nome": "Consultar frequência",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento de frequência e disciplinar do aluno",
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
      "decs": [
        "DEC15"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF28": {
      "nome": "Emitir alerta de faltas críticas",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento de frequência e disciplinar do aluno",
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
      "decs": [
        "DEC15"
      ],
      "pens": [
        "PEN15"
      ],
      "its": [],
      "lacunas": [
        "PEN15: Definir a regra de contagem de faltas do alerta: período (mês, semestre), reinício da contagem e tratamento de faltas justificadas"
      ]
    },
    "RF29": {
      "nome": "Registrar medida disciplinar",
      "estado": "Rascunho",
      "cp": "CP5: Acompanhamento de frequência e disciplinar do aluno",
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
        "DEC03",
        "DEC15",
        "DEC17"
      ],
      "pens": [
        "PEN13"
      ],
      "its": [],
      "lacunas": [
        "PEN13: Definir quem registra uma medida disciplinar, se a data é a da ocorrência ou a do registro, e o efeito de suspensão e desligamento sobre a matrícula e a turma"
      ]
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
      "decs": [
        "DEC17"
      ],
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
      "nome": "Solicitar matrícula online",
      "estado": "Rascunho",
      "cp": "CP7: Matrícula online",
      "ator": "Interessado (aluno maior de idade ou responsável legal)",
      "declaracao": "Deve ser possível a qualquer interessado enviar, por um formulário público e sem login, a solicitação de matrícula de um aluno, com os dados do aluno, do responsável legal (se menor de idade) e das pessoas autorizadas a retirá-lo. A solicitação fica registrada para análise da coordenação (RF42); a matrícula só é efetivada presencialmente (RN02).",
      "entradas": "Aluno: nome, data de nascimento, contato e modalidade ou turma de interesse (antigo RF36).\nResponsável legal, se o aluno tiver menos de 18 anos: nome, contato e vínculo (antigo RF37).\nPessoas autorizadas a retirar o aluno, se menor de idade: ao menos uma, com nome e contato, ou a indicação de que pode ir embora sozinho (antigo RF40).\nTermos: aceite de dados (RF38) e resposta ao termo de imagem (RF39).",
      "pre": "Nenhuma: o formulário é público",
      "proc": "(a detalhar)",
      "saidas": "Solicitação registrada e número de protocolo (RF41); ou indicação dos campos que faltam",
      "pdf": false,
      "pendente": 0,
      "moscow": "4, Tem que ter",
      "entrega": "Pós-MVP",
      "criterios": [
        "1. Dado um visitante sem login, quando abre o link público, então vê o formulário.",
        "2. Dado um campo do aluno vazio, quando tenta enviar, então o envio é bloqueado e o campo é indicado.",
        "3. Dada uma data de nascimento de menor de 18 anos, então o formulário exige nome, contato e vínculo do responsável legal e ao menos uma pessoa autorizada (ou a indicação de que o menor pode ir embora sozinho).",
        "4. Dado um aluno com 18 anos ou mais, então os dados do responsável e das pessoas autorizadas não são exigidos.",
        "5. Dado o formulário completo e o termo de dados aceito, quando envia, então a solicitação é registrada e o protocolo é exibido."
      ],
      "rns": [
        "RN02",
        "RN07",
        "RN10"
      ],
      "rnfs": [
        "RNF01",
        "RNF02",
        "RNF03",
        "RNF09",
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
        "DEC03",
        "DEC16",
        "DEC18"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF36": {
      "nome": "Preencher dados do aluno (incorporado ao RF35)",
      "estado": "Retirado",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Incorporado ao RF35 em 14/11/2026: era uma etapa do formulário de matrícula, e não uma operação completa. O código não é reutilizado. Texto original: Deve ser possível o interesado inserir, no formulário, os dados do aluno (nome, data de nascimento, contato e modalidade ou turma de interesse).",
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
      "decs": [
        "DEC03",
        "DEC16"
      ],
      "pens": [],
      "its": [],
      "lacunas": []
    },
    "RF37": {
      "nome": "Informar dados do responsável legal (incorporado ao RF35)",
      "estado": "Retirado",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Incorporado ao RF35 em 14/11/2026: era uma etapa do formulário de matrícula, e não uma operação completa. O código não é reutilizado. Texto original: Deve ser possível inserir os dados do responsável legal (nome, contato e vínculo) quando o aluno tiver menos de 18 anos.",
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
      "decs": [
        "DEC03",
        "DEC16"
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
        "DEC03",
        "DEC25"
      ],
      "pens": [
        "PEN14"
      ],
      "its": [],
      "lacunas": [
        "PEN14: Definir como as versões dos termos (dados e imagem) são criadas e guardadas, para que o aceite registre a versão vigente"
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
        "DEC03",
        "DEC25"
      ],
      "pens": [
        "PEN14"
      ],
      "its": [],
      "lacunas": [
        "PEN14: Definir como as versões dos termos (dados e imagem) são criadas e guardadas, para que o aceite registre a versão vigente"
      ]
    },
    "RF40": {
      "nome": "Informar pessoas autorizadas a retirar o aluno (incorporado ao RF35)",
      "estado": "Retirado",
      "cp": "CP7: Matrícula online",
      "ator": "(a detalhar)",
      "declaracao": "Incorporado ao RF35 em 14/11/2026: era uma etapa do formulário de matrícula, e não uma operação completa. O código não é reutilizado. Texto original: Deve ser possível inserir ao menos uma pessoa autorizada a retirar o aluno quando ele for menor de idade, com nome e contato, ou se o menor pode ir embora só.",
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
      "decs": [
        "DEC16"
      ],
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
      "ator": "Coordenação",
      "declaracao": "Deve ser possível à coordenação consultar as solicitações recebidas (RF35) e defini-las como aprovada, recusada ou em lista de espera. A aprovação não cria o cadastro definitivo: o aluno aprovado é convocado para a confirmação presencial, com assinatura dos termos (RN02), e só então é cadastrado (RF21), aproveitando os dados da solicitação.",
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
      "rns": [
        "RN02"
      ],
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
      "decs": [
        "DEC02",
        "DEC03",
        "DEC17",
        "DEC18"
      ],
      "pens": [
        "PEN12"
      ],
      "its": [],
      "lacunas": [
        "PEN12: Definir o que a aprovação de uma solicitação de matrícula gera: reserva de vaga na turma, prazo para a confirmação presencial e documentos que ficam pendentes. Afeta só a matrícula online (pós-MVP); o cadastro definitivo continua sendo feito pelo RF21"
      ]
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
    "RN16": "Separação de Consentimento de Dados e Termo de Imagem: O aceite do termo de tratamento de dados pessoais (LGPD) e do termo de uso de imagem são tratados de forma independente. A recusa do termo de imagem impede a realização da matrícula. Vale para a matrícula online; no cadastro presencial, o termo é único (DEC25).",
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
      "desc": "Um voluntário sem experiência técnica deve conseguir concluir as tarefas do sistema sem treinamento prévio (CP1, CP3, CP4, CP5).",
      "crit": "Em teste com usuários que nunca usaram o sistema e não receberam treinamento, pelo menos 80% concluem a tarefa proposta em até 8 minutos, contados do início da tarefa."
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
      "nome": "Preservação de histórico (retirado)",
      "desc": "Retirado: descrevia um comportamento funcional já especificado em RN01 (o aluno nunca é excluído, só inativado) e nos critérios de RF05 e RF24. Não é um atributo de qualidade.",
      "crit": "— (verificado pelos critérios de aceitação dos RFs)"
    },
    "RNF05": {
      "nome": "Confirmação antes de ações críticas (retirado)",
      "desc": "Retirado: descrevia um comportamento funcional de interação, já registrado na DEC02 e nos critérios dos RFs afetados (por exemplo, RN48 no RF24). Não é um atributo de qualidade.",
      "crit": "— (verificado pelos critérios de aceitação dos RFs)"
    },
    "RNF06": {
      "nome": "Tempo de resposta das consultas internas",
      "desc": "Resposta das consultas internas em até 3s (ficha do aluno, frequência, turmas).",
      "crit": "P95 das requisições autenticadas ≤ 3s sob carga normal."
    },
    "RNF07": {
      "nome": "Carregamento da página pública",
      "desc": "Carregamento da página pública em até 5s (CP3, CP7).",
      "crit": "LCP ≤ 5s em conexão 2G simulada (limitação de rede do Chrome DevTools/Lighthouse), medido pelo Lighthouse."
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
      "desc": "As funcionalidades administrativas são restritas ao perfil de coordenação, o único perfil com login (RN20). Professores, voluntários e famílias não têm login: acessam apenas o módulo público.",
      "crit": "Rotas administrativas retornam 401 para requisições sem autenticação e 403 para requisições autenticadas sem o perfil de coordenação. Rotas do módulo público respondem sem autenticação."
    },
    "RNF12": {
      "nome": "Proteção de senhas e dados sensíveis",
      "desc": "Senhas com hash e dados sensíveis criptografados.",
      "crit": "Verificado por inspeção do banco e do armazenamento de anexos: (1) nenhuma senha está em texto claro, apenas o hash gerado por algoritmo próprio para senhas (por exemplo, bcrypt ou Argon2); (2) os dados de saúde do aluno (descrição do problema de saúde e laudos) e os documentos anexados (identidade, comprovante de residência) estão criptografados, e lê-los diretamente no banco ou no armazenamento não revela o conteúdo."
    },
    "RNF13": {
      "nome": "Conformidade com a LGPD",
      "desc": "O sistema deve tratar os dados pessoais de acordo com os princípios, direitos dos titulares e requisitos de segurança e tratamento estabelecidos pela Lei nº 13.709/2018 (LGPD).",
      "crit": "Aceito quando todos os itens abaixo são verificados:\n1. O cadastro só é concluído com o aceite do termo de dados registrado, com data (RN40; RF38 na matrícula online).\n2. A ficha do aluno não pede dado que não esteja na ficha de papel do CECP ou em uma regra de negócio (necessidade, art. 6º, III).\n3. Os dados de saúde ficam visíveis só na ficha do aluno, para a coordenação autenticada (RNF11).\n4. Os dados de saúde e os documentos estão protegidos conforme RNF12.\n5. A coordenação consegue atender a um pedido de eliminação (RF25) e a operação fica registrada em log (RNF09).\n6. O módulo público informa quais dados são coletados e para quê (art. 14, §2º)."
    }
  },
  "dec": [
    {
      "id": "DEC01",
      "data": "08/10/2026 (data registrada na própria ata; o arquivo está nomeado como 09/10)",
      "texto": "O MVP foi refeito: após explicar o conceito de MVP ao cliente, o MoSCoW foi reclassificado, porque a primeira priorização (24/09) deixou cerca de 36 dos 42 requisitos no MVP. Os valores de negócio seguem vigentes; o conjunto do MVP foi substituído pela DEC03. Nota: a ata de 09/10 encerrou com o encaminhamento de que a matriz seria refeita e validada com o cliente; esse passo foi concluído em 30/10/2026 e registrado na DEC03",
      "rfs": [],
      "fonte": "Priorização, ata 09/10"
    },
    {
      "id": "DEC02",
      "data": "22/09/2026, reforçada em 24/09/2026 e prototipada em 30/10/2026",
      "texto": "Ações críticas (inativar aluno ou turma, aplicar medida disciplinar, remover) exigem confirmação antes de serem executadas. Era o RNF05, retirado em 14/11/2026 por ser comportamento funcional; a regra vale por esta decisão e pelos critérios de cada RF. Para conteúdo institucional e eventos, a tela de confirmação de remoção foi apresentada no protótipo",
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
      "data": "10/11/2026 (a reunião em que o comportamento foi discutido pela primeira vez continua sem data)",
      "texto": "Após encerrar a sessão, o sistema redireciona para a tela de login (o cliente admitiu também o modo público). O protótipo aprovado em 10/11 mostra esse comportamento",
      "rfs": [
        "RF00"
      ],
      "fonte": "Ata 10/11 (protótipo aprovado, DEC20)"
    },
    {
      "id": "DEC05",
      "data": "Sem data registrada",
      "texto": "Termo único (responsabilidade, imagem e dados) no cadastro de aluno. A base é o termo de responsabilidade da ficha de inscrição em papel do CECP, que não tem cláusulas de uso de imagem nem de dados; a equipe já acrescentou essas cláusulas ao termo do sistema, remodelando-o como a RN40 previa",
      "rfs": [
        "RF21"
      ],
      "fonte": "ficha de inscrição do CECP; confirmado pela equipe em 14/11/2026"
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
    },
    {
      "id": "DEC15",
      "data": "14/11/2026",
      "texto": "OE2 e CP5 tratam apenas de frequência nas aulas do CECP e de medidas disciplinares. O desempenho na escola de origem (RN15) continua sendo conferido pela coordenação fora do sistema; o produto não registra notas nem situação escolar. Encerra a PEN10",
      "rfs": [
        "RF26",
        "RF27",
        "RF28",
        "RF29"
      ],
      "fonte": "Decisão da equipe sobre as issues #24 e #27; solução proposta"
    },
    {
      "id": "DEC16",
      "data": "14/11/2026",
      "texto": "RF36, RF37 e RF40 foram incorporados ao RF35, que passa a ser \"Solicitar matrícula online\": eram etapas do formulário, e não operações completas. Os códigos retirados não são reutilizados",
      "rfs": [
        "RF35",
        "RF36",
        "RF37",
        "RF40"
      ],
      "fonte": "Decisão da equipe sobre a issue #28"
    },
    {
      "id": "DEC17",
      "data": "14/11/2026",
      "texto": "RNF04 (preservar histórico) e RNF05 (pedir confirmação) foram retirados: descreviam comportamento funcional já coberto por RN01, DEC02 e pelos critérios dos RFs. Os códigos não são reutilizados",
      "rfs": [
        "RF05",
        "RF06",
        "RF16",
        "RF19",
        "RF24",
        "RF25",
        "RF29",
        "RF33",
        "RF42"
      ],
      "fonte": "Decisão da equipe sobre a issue #29"
    },
    {
      "id": "DEC18",
      "data": "14/11/2026",
      "texto": "A matrícula online é uma pré-matrícula: o interessado envia a solicitação, a coordenação a analisa e a aprovada é efetivada presencialmente, com assinatura dos termos (RN02); só então o aluno é cadastrado pelo RF21",
      "rfs": [
        "RF35",
        "RF42",
        "RF21"
      ],
      "fonte": "Ata 08/10 (pré-matrícula com aprovação presencial); consolidação pedida na issue #24"
    },
    {
      "id": "DEC19",
      "data": "10/11/2026",
      "texto": "O cliente testou o sistema construído e aceitou o acesso (RF00 a RF02) e o conteúdo institucional e eventos (RF13 a RF20). O teste do encerramento de sessão (RF00) foi confirmado pela equipe em 14/11, pois não aparece na transcrição. O sistema rodava no computador da equipe, sem ambiente publicado",
      "rfs": [
        "RF00",
        "RF01",
        "RF02",
        "RF13",
        "RF14",
        "RF15",
        "RF16",
        "RF17",
        "RF18",
        "RF19",
        "RF20"
      ],
      "fonte": "Ata 10/11"
    },
    {
      "id": "DEC20",
      "data": "10/11/2026",
      "texto": "O representante do cliente aprovou o protótipo das telas de acesso, turmas, alunos e coordenadores. O retorno das demais pessoas do CECP, recebido depois da reunião, também foi positivo, sem ajustes pedidos (confirmado pela equipe em 14/11/2026)",
      "rfs": [
        "RF00",
        "RF01",
        "RF02",
        "RF03",
        "RF06",
        "RF07",
        "RF21",
        "RF22",
        "RF23",
        "RF24"
      ],
      "fonte": "Ata 10/11"
    },
    {
      "id": "DEC21",
      "data": "10/11/2026",
      "texto": "Ao clicar em uma imagem de uma publicação, ela se expande. Pedido do cliente durante o teste",
      "rfs": [
        "RF15",
        "RF20"
      ],
      "fonte": "Ata 10/11"
    },
    {
      "id": "DEC22",
      "data": "10/11/2026",
      "texto": "O tamanho da letra do sistema é mantido, apesar do pedido do José Ivan por letras maiores, porque os demais que viram as telas o acharam adequado. Uma letra maior pode ser avaliada para a página institucional \"Quem somos\", depois do MVP",
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
      "fonte": "Ata 10/11"
    },
    {
      "id": "DEC23",
      "data": "14/11/2026",
      "texto": "Alunos inativos aparecem na lista de alunos da turma. Encerra a PEN02",
      "rfs": [
        "RF07"
      ],
      "fonte": "Confirmado pela equipe em 14/11/2026"
    },
    {
      "id": "DEC24",
      "data": "14/11/2026",
      "texto": "Não existe limite de alunos por turma nem regra de inscrição prévia. Encerra a PEN09",
      "rfs": [
        "RF03",
        "RF06"
      ],
      "fonte": "Confirmado pela equipe em 14/11/2026"
    },
    {
      "id": "DEC25",
      "data": "14/11/2026",
      "texto": "Cadastro presencial e matrícula online são fluxos distintos. No cadastro presencial, a coordenação registra um termo único (responsabilidade, uso de imagem e dados, DEC05). Na matrícula online, os aceites de dados e de imagem continuam separados (RN16). Encerra a PEN03",
      "rfs": [
        "RF21",
        "RF38",
        "RF39"
      ],
      "fonte": "Confirmado pela equipe em 14/11/2026"
    },
    {
      "id": "DEC26",
      "data": "14/11/2026",
      "texto": "Turmas (RF03, RF06 e RF07) e alunos (RF21 a RF24) serão construídos juntos e entregues funcionando no mesmo incremento, o que resolve a dependência entre associar aluno à turma e cadastrar aluno. A iteração seguinte fica para iterar sobre esse incremento, com os ajustes do retorno do cliente. Encerra a PEN11",
      "rfs": [
        "RF03",
        "RF06",
        "RF07",
        "RF21",
        "RF22",
        "RF23",
        "RF24"
      ],
      "fonte": "Decisão da equipe em 14/11/2026"
    },
    {
      "id": "DEC27",
      "data": "21/10/2026, reforçada em 30/10/2026",
      "texto": "O subtítulo do evento é opcional (\"se houver\"). O cliente concordou nas duas reuniões; a ficha do RF17, que o listava como obrigatório, foi corrigida. Encerra a PEN01",
      "rfs": [
        "RF17",
        "RF18"
      ],
      "fonte": "Ata 21/10, ata 30/10"
    },
    {
      "id": "DEC28",
      "data": "14/11/2026",
      "texto": "Os usuários da coordenação continuam sendo criados pelo terminal (RN21). A tela de gestão de coordenadores, aprovada no protótipo de 10/11, fica fora do MVP e não vira RF agora. Encerra a PEN20",
      "rfs": [
        "RF01",
        "RF02"
      ],
      "fonte": "Decisão da equipe em 14/11/2026"
    },
    {
      "id": "DEC29",
      "data": "14/11/2026",
      "texto": "A \"carga normal\" dos RNF06 e RNF08 é de até 10 sessões de coordenação autenticadas e simultâneas, o mesmo número já usado no critério do RNF08. O volume de alunos, turmas e anexos usado no teste é registrado como premissa junto com o resultado. Encerra a PEN16",
      "rfs": [
        "RF02",
        "RF07",
        "RF23"
      ],
      "fonte": "Decisão da equipe em 14/11/2026"
    },
    {
      "id": "DEC30",
      "data": "30/10/2026",
      "texto": "Na matriz final, a equipe reavaliou a posição de esforço dos RFs, e a coluna \"Esforço na matriz\" da priorização é a vigente, mesmo quando difere do arredondamento da média dos votos. No empate da moda, vale o maior valor (estimativa mais conservadora). Encerra a PEN06",
      "rfs": [],
      "fonte": "Priorização; confirmado pela equipe em 14/11/2026"
    },
    {
      "id": "DEC31",
      "data": "14/11/2026",
      "texto": "Não serão criados agora RNFs de backup e recuperação de dados nem de comunicação segura (HTTPS). Encerra a PEN17",
      "rfs": [],
      "fonte": "Decisão da equipe em 14/11/2026"
    },
    {
      "id": "DEC32",
      "data": "14/11/2026",
      "texto": "Não haverá migração em lote dos dados existentes. Depois da entrega, a coordenação cadastra aos poucos os alunos ativos pelo próprio sistema (RF21), usando as fichas em papel, com apoio da equipe na primeira semana. Encerra a PEN19",
      "rfs": [
        "RF21"
      ],
      "fonte": "Decisão da equipe em 14/11/2026"
    }
  ],
  "pen": [
    {
      "id": "PEN12",
      "texto": "Definir o que a aprovação de uma solicitação de matrícula gera: reserva de vaga na turma, prazo para a confirmação presencial e documentos que ficam pendentes. Afeta só a matrícula online (pós-MVP); o cadastro definitivo continua sendo feito pelo RF21",
      "rfs": [
        "RF42"
      ],
      "acao": "Confirmar com o cliente no detalhamento da matrícula online"
    },
    {
      "id": "PEN13",
      "texto": "Definir quem registra uma medida disciplinar, se a data é a da ocorrência ou a do registro, e o efeito de suspensão e desligamento sobre a matrícula e a turma",
      "rfs": [
        "RF29"
      ],
      "acao": "Confirmar com o cliente no detalhamento de CP5"
    },
    {
      "id": "PEN14",
      "texto": "Definir como as versões dos termos (dados e imagem) são criadas e guardadas, para que o aceite registre a versão vigente",
      "rfs": [
        "RF38",
        "RF39"
      ],
      "acao": "Definir com o cliente junto do modelo de termo (DEC05)"
    },
    {
      "id": "PEN15",
      "texto": "Definir a regra de contagem de faltas do alerta: período (mês, semestre), reinício da contagem e tratamento de faltas justificadas",
      "rfs": [
        "RF28"
      ],
      "acao": "Confirmar com o cliente no detalhamento de CP5"
    },
    {
      "id": "PEN23",
      "texto": "Não há regra nem RF para reativar um aluno inativo (por exemplo, um aluno que volta ao projeto). A lacuna apareceu ao representar o ciclo de vida do aluno (seção 5.3)",
      "rfs": [
        "RF24"
      ],
      "acao": "Perguntar ao cliente se o aluno que volta é reativado ou cadastrado de novo"
    }
  ],
  "pen_enc": [
    {
      "id": "PEN05",
      "texto": "Data da reunião de priorização (08/10 no texto, 09/10 nos arquivos)",
      "rfs": [],
      "acao": "Encerrada em 03/11/2026: a própria ata registra 08/10/2026; 09/10 é só o nome do arquivo. A DEC01 foi atualizada."
    },
    {
      "id": "PEN10",
      "texto": "OE2 menciona \"condicionalidades pedagógicas\" e CP5 promete \"acompanhamento pedagógico do aluno\", mas não existe RF para registrar ou consultar informações escolares (notas, situação escolar de origem). Confirmar se essa é uma limitação de escopo deliberada e, se for, registrar na descrição de OE2 e CP5 que o acompanhamento pedagógico se restringe a frequência e medidas disciplinares",
      "rfs": [
        "RF26",
        "RF27",
        "RF28",
        "RF29"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC15: OE2 e CP5 foram restritos a frequência e disciplina na solução proposta"
    },
    {
      "id": "PEN21",
      "texto": "RF00 (encerrar sessão) foi construído, mas o teste com o cliente não aparece na transcrição da reunião de 10/11",
      "rfs": [
        "RF00"
      ],
      "acao": "Encerrada em 14/11/2026: a equipe confirmou que o cliente saiu do sistema e voltou à tela de login na reunião de 10/11 (DEC19)"
    },
    {
      "id": "PEN02",
      "texto": "Definir se alunos inativos aparecem na lista da turma",
      "rfs": [
        "RF07"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC23: alunos inativos aparecem na lista da turma"
    },
    {
      "id": "PEN03",
      "texto": "Conciliar o termo único do cadastro presencial (RN40, RF21) com a regra de que dados e imagem são aceites independentes na matrícula online (RN16, RF38 e RF39)",
      "rfs": [
        "RF21",
        "RF38",
        "RF39"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC25: são fluxos distintos; termo único no presencial e aceites separados na matrícula online"
    },
    {
      "id": "PEN04",
      "texto": "Completar a data e a fonte da decisão DEC05. A DEC04 passou a ter fonte: o protótipo aprovado em 10/11",
      "rfs": [
        "RF21"
      ],
      "acao": "Encerrada em 14/11/2026: a DEC04 tem fonte no protótipo de 10/11 e a DEC05 tem como fonte a ficha de inscrição do CECP (o modelo do termo)"
    },
    {
      "id": "PEN09",
      "texto": "Regra citada em 30/10 para turmas com limite de 30 alunos e inscrição prévia da pessoa ficou pouco clara",
      "rfs": [
        "RF03",
        "RF06"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC24: a regra não existe"
    },
    {
      "id": "PEN11",
      "texto": "O cronograma prevê RF06 e RF07 (Iteração 8) antes do cadastro de aluno RF21 (Iteração 10), mas associar aluno à turma depende de aluno cadastrado. O conflito entre CP3 e a autenticação já não bloqueia: as duas partes foram aceitas juntas em 10/11 (DEC19)",
      "rfs": [
        "RF01",
        "RF02",
        "RF06",
        "RF07",
        "RF13",
        "RF21"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC26: turmas e alunos serão construídos juntos"
    },
    {
      "id": "PEN01",
      "texto": "O subtítulo do evento é opcional (\"se houver\") nas reuniões de 21/10 e 30/10, mas a ficha do RF17 o lista entre as entradas obrigatórias",
      "rfs": [
        "RF17",
        "RF18"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC27: subtítulo opcional no RF17 e no RF18"
    },
    {
      "id": "PEN08",
      "texto": "O cliente deve enviar a logo atualizada. O retorno da Sandra sobre as telas de CP3 foi positivo, conforme relatado em 10/11 (ata); falta o retorno das demais pessoas sobre as telas de acesso, turmas, alunos e coordenadores (DEC20)",
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
      "acao": "Encerrada em 14/11/2026: o cliente enviou a logo atualizada e o retorno das demais pessoas sobre as telas, sem ajustes pedidos (confirmado pela equipe)"
    },
    {
      "id": "PEN16",
      "texto": "Definir a \"carga normal\" dos RNF06 e RNF08: número de usuários simultâneos, volume de alunos e anexos e operações mais frequentes",
      "rfs": [
        "RF02",
        "RF07",
        "RF23"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC29: até 10 sessões de coordenação simultâneas"
    },
    {
      "id": "PEN20",
      "texto": "A tela de gestão de coordenadores (criar coordenador com nome, usuário, perfil, situação e senha inicial) foi prototipada e aprovada, mas não tem RF. Hoje o usuário é criado pelo terminal, e a RN21 fala só de um usuário administrador padrão",
      "rfs": [
        "RF01",
        "RF02"
      ],
      "acao": "Encerrada em 14/11/2026 pela DEC28: a criação de coordenadores continua pelo terminal"
    },
    {
      "id": "PEN22",
      "texto": "Não há ata nem gravação publicada da reunião em que acesso, turmas e alunos (RF00 a RF07 e RF21 a RF24) foram detalhados, embora as fichas e as regras RN17 a RN24 e RN35 a RN48 citem \"a reunião\"",
      "rfs": [
        "RF00",
        "RF01",
        "RF02",
        "RF03",
        "RF06",
        "RF07",
        "RF21",
        "RF22",
        "RF23",
        "RF24"
      ],
      "acao": "Encerrada em 14/11/2026: não houve gravação nem ata do detalhamento; o resultado foi validado pelo cliente no protótipo aprovado em 10/11 (DEC20) (confirmado pela equipe)"
    },
    {
      "id": "PEN18",
      "texto": "Atas anteriores à renumeração citam códigos de RF que hoje têm outro significado. Falta uma tabela de correspondência entre a numeração antiga e a atual",
      "rfs": [],
      "acao": "Encerrada em 14/11/2026: a tabela de correspondência está em Documentos arquivados, e as atas que usam a numeração antiga (cliente 24/09 e equipe 26/09) têm um aviso apontando para ela"
    },
    {
      "id": "PEN06",
      "texto": "Reconciliar as notas de esforço da seção 5 da priorização com a posição de esforço da matriz final (30 RFs divergem do arredondamento do ET) e documentar a regra de desempate quando a moda dos votos empata",
      "rfs": [],
      "acao": "Encerrada em 14/11/2026 pela DEC30: a posição da matriz é a vigente; desempate pelo maior valor"
    },
    {
      "id": "PEN07",
      "texto": "Confirmar as datas das reuniões de 21/10 (detalhamento) e 30/10 (design do usuário), deduzidas dos nomes de arquivo e da data de publicação do vídeo",
      "rfs": [],
      "acao": "Encerrada em 14/11/2026: a equipe confirmou as datas de 21/10 e 30/10; as atas e as evidências foram corrigidas"
    },
    {
      "id": "PEN17",
      "texto": "Backup, recuperação de dados e comunicação segura (HTTPS) foram recusados na página de ajustes por \"já haver proteção de dados\", mas proteção de senha não garante recuperar dados perdidos",
      "rfs": [],
      "acao": "Encerrada em 14/11/2026 pela DEC31: a equipe decidiu não incluir esses RNFs agora"
    },
    {
      "id": "PEN19",
      "texto": "Planejar a carga inicial dos dados existentes: volume de fichas a migrar, quem da coordenação faz a digitação, quem da equipe apoia e como os dados são conferidos",
      "rfs": [],
      "acao": "Encerrada em 14/11/2026 pela DEC32: a coordenação cadastra os alunos ativos aos poucos, pelo sistema"
    }
  ],
  "its": [
    {
      "nome": "Iteração 0",
      "periodo": "",
      "foco": "Entrega unidade 1 (08/09)",
      "entregas": "Documento de visão versão 1.1 e git pages",
      "rfs": [],
      "situacao": "Concluída. Unidade 1 entregue. Reunião realizada em 17/09 (ata)"
    },
    {
      "nome": "Iteração 1",
      "periodo": "20/09/2026 - 27/09/2026",
      "foco": "Planejamento de Requisitos: Elicitação e ajuste da lista de RFs e RNFs, preparação para validação",
      "entregas": "Atualização da documentação do git pages com a prévia dos principais requisitos",
      "rfs": [],
      "situacao": "Concluída. Reuniões realizadas em 22/09, 24/09 (primeira priorização MoSCoW) e 26/09 (atas)"
    },
    {
      "nome": "Iteração 2",
      "periodo": "28/09/2026 - 04/10/2026",
      "foco": "Planejamento de Requisitos: Validação final da lista de RFs e RNFs (29/09); avaliação de valor de negócio com o cliente e de esforço técnico pela equipe; construção da matriz 4×4; definição do MVP",
      "entregas": "Lista validada de RFs/RNFs; matriz 4×4 de priorização; lista de RFs selecionados para o MVP",
      "rfs": [],
      "situacao": "Concluída. A votação de esforço da equipe ocorreu em 26/09; a matriz e o MVP foram refeitos depois (DEC01, DEC03)"
    },
    {
      "nome": "Iteração 3",
      "periodo": "05/10/2026 - 11/10/2026",
      "foco": "Planejamento de Requisitos: definição do backlog, DoR e DoD com base no MVP validado; preparação da documentação para a entrega da Unidade 2",
      "entregas": "Backlog, DoR e DoD definidos",
      "rfs": [],
      "situacao": "Concluída. Nova priorização com o cliente em 08/10 (ata, DEC01); DoR e DoD escritos em 10/10"
    },
    {
      "nome": "Iteração 4",
      "periodo": "12/10/2026 - 18/10/2026",
      "foco": "Entrega da Unidade 2 (13/10)",
      "entregas": "Documento de visão versão 1.2; requisitos detalhados de turmas e conteúdo institucional/eventos",
      "rfs": [],
      "situacao": "Concluída. Unidade 2 entregue. Nenhuma reunião com o cliente registrada"
    },
    {
      "nome": "Iteração 5",
      "periodo": "19/10/2026 - 25/10/2026",
      "foco": "Planejamento: detalhamento dos requisitos do módulo público (publicações e eventos)\n\nDesign do Usuário: Protótipo da tela de publicação, edição e consulta de conteúdo institucional e eventos; protótipo inicial das telas de turmas (cadastro de turma, RF03, e lista de alunos da turma, RF07)\n\nConstrução: início da implementação do módulo de conteúdo institucional/eventos",
      "entregas": "Detalhamento de RF13 a RF20 com o cliente; protótipo de RF13 a RF20 pronto para avaliação",
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
      "situacao": "Concluída. Detalhamento de RF13 a RF20 com o cliente em 21/10 (ata)"
    },
    {
      "nome": "Iteração 6",
      "periodo": "26/10/2026 - 01/11/2026",
      "foco": "Planejamento: detalhamento de todos os requisitos restantes do MVP\n\nDesign do Usuário: avaliação do protótipo de RF13 a RF20 com o cliente e ajustes\n\nConstrução: implementação de RF13 a RF20 após a aprovação do protótipo",
      "entregas": "Protótipo de RF13 a RF20 aprovado pelo cliente; RF13 a RF20 em construção",
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
      "situacao": "Concluída. Protótipo de CP3 aprovado e MVP validado em 30/10 (ata, DEC03, DEC12)"
    },
    {
      "nome": "Iteração 7",
      "periodo": "02/11/2026 - 08/11/2026",
      "foco": "Design do Usuário: prototipação das telas de autenticação, avaliação com o cliente na reunião da iteração e ajustes\n\nConstrução: implementação dos RF00, RF01 e RF02, pré-requisito das ações da coordenação em RF13 a RF24\n\nTransição: teste de aceite dos requisitos implementados nesta construção",
      "entregas": "RF00, RF01 e RF02 implementados e testados",
      "rfs": [
        "RF00",
        "RF01",
        "RF02"
      ],
      "situacao": "Concluída. RF00 a RF02 e RF13 a RF20 construídos; o cliente testou e aceitou RF00 a RF02 e RF13 a RF20 em 10/11 (ata, DEC19)"
    },
    {
      "nome": "Iteração 8",
      "periodo": "09/11/2026 - 15/11/2026",
      "foco": "Design do Usuário: prototipação das telas de gestão de turmas, avaliação com o cliente e ajustes\n\nConstrução: implementação dos RF03, RF06 e RF07\n\nTransição: teste de aceite dos requisitos implementados nesta construção; treinamento inicial e capacitação da ONG",
      "entregas": "RF03, RF06 e RF07 implementados e testados",
      "rfs": [
        "RF03",
        "RF06",
        "RF07"
      ],
      "situacao": "Em andamento. Design do Usuário concluído: o protótipo de turmas (RF03, RF06 e RF07) e de alunos (RF21 a RF24) foi aprovado pelo cliente em 10/11 (ata, DEC20). Construção ainda não iniciada. Turmas e alunos (RF21 a RF24) serão construídos juntos e entregues funcionando; a iteração seguinte fica para iterar sobre o incremento (DEC26)"
    },
    {
      "nome": "Iteração 9",
      "periodo": "16/11/2026 - 22/11/2026",
      "foco": "Entrega da unidade 3 (17/11)\n\nConstrução: sem requisitos novos do MVP; a matrícula online (RF35, RF38 e RF39) é incremento pós-MVP e só entra se houver capacidade e validação do cliente (DEC03)",
      "entregas": "Nova versão do documento de visão 1.3; issues anteriores fechadas",
      "rfs": [],
      "situacao": "Planejada"
    },
    {
      "nome": "Iteração 10",
      "periodo": "23/11/2026 - 29/11/2026",
      "foco": "Design do Usuário: protótipo da ficha do aluno, avaliação com o cliente e ajustes\n\nConstrução: cadastro, edição, consulta e inativação do aluno (ficha do aluno). A remoção de dados (RF25) é pós-MVP\n\nTransição: início do cadastro dos alunos ativos pela própria coordenação, pelo sistema, com apoio da equipe (DEC32); testes de segurança; testes de aceite do MVP completo; validação com a coordenação em 26/11 ou 27/11; treinamento final",
      "entregas": "MVP concluído e validado; ficha de aluno funcional, com cadastro e histórico; coordenação pronta para cadastrar os alunos ativos pelo sistema",
      "rfs": [
        "RF21",
        "RF22",
        "RF23",
        "RF24"
      ],
      "situacao": "Planejada"
    },
    {
      "nome": "Iteração 11",
      "periodo": "30/11/2026 - 01/12/2026",
      "foco": "Entrega da unidade 4 (01/12)\n\nTransição: correções a partir da validação de 26/11 ou 27/11, nova execução dos testes afetados e confirmação dos ajustes com o cliente por WhatsApp ou reunião curta; último deploy; finalização do projeto. A janela é curta (28/11 a 01/12): só entram correções, sem funcionalidade nova",
      "entregas": "Última versão do documento de visão 1.4; projeto entregue",
      "rfs": [],
      "situacao": "Planejada"
    }
  ],
  "cron_nota": "Critério de transição entre fases: as macrofases de Design, Construção e Transição do RAD só entram em foco a partir da Iteração 5, após a validação formal dos requisitos, priorização via matriz 4×4, definição do MVP e formalização do backlog/DoR/DoD na Entrega da Unidade 2 (13/10). Até lá, o esforço da equipe está inteiramente concentrado em Planejamento de Requisitos. O cronograma é uma previsão e que pode sofrer mudanças no decorrer do desenvolvimento para melhor adequação do projeto.",
  "alertas": []
};
