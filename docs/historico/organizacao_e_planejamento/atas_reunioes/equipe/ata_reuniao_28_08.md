# Ata de Reunião — Tecnologias, Metodologia e Composição da Equipe

## 1. Identificação da reunião

**Data:** 28/08/2026
**Modalidade:** Remota (chamada de vídeo)
**Participantes:** Todos
**Pauta:** Continuação do preenchimento do documento de Visão do Produto e Projeto, definição das tecnologias a serem utilizadas, divisão de tarefas restantes do documento, definição da abordagem/ciclo de vida/processo de desenvolvimento, ferramentas e comunicação e composição/papéis da equipe


## 2. Arquitetura e tecnologias a serem utilizadas

### Arquitetura proposta
Foi discutida e definida a arquitetura geral do sistema, dividida em duas aplicações praticamente independentes, compartilhando o mesmo banco de dados:
- **Site público:** funciona basicamente como um formulário — as pessoas preenchem e enviam seus dados de cadastro, que vão direto para o servidor, sem que o site tenha qualquer acesso de leitura ao banco (**somente escrita**). Não haverá portal do aluno nem login de usuários comuns nessa parte, para reduzir a complexidade e o escopo do MVP;
- **Aplicação interna de gestão:** roda em **localhost**, no computador/servidor do próprio cliente. É por ela que o cliente vai visualizar e gerenciar os cadastros recebidos, as turmas etc. Não há integração direta entre o site público e essa aplicação, os dados enviados pelo site ficam "aguardando" no servidor até serem abertos por essa aplicação local.

A principal vantagem apontada dessa separação é reduzir a necessidade de camadas de segurança: como o cliente acessa tudo localmente, não há risco de acesso remoto indevido aos dados — quem quiser alterar algo precisa estar fisicamente no local. Foi cogitado tornar esse acesso mais amplo (ex.: acesso remoto, portal de aluno), mas descartado por falta de tempo para o escopo do projeto.

### Stack de tecnologia definida nesta reunião
- **Backend/Framework:** Python com **Django** escolhido não por preferência técnica (vários integrantes comentaram não gostar do Django), mas porque é o que a maioria da equipe já conhece, o que acelera o desenvolvimento;
- **ORM:** **SQLAlchemy** (referido na conversa como "Alckmin"/"Alchemy"), para evitar escrever SQL puro e facilitar a definição de tabelas via classes Python;
- **Front-end:** HTML, CSS e JavaScript e/ou TypeScript (ambos liberados cada um usa o que preferir; um dos integrantes comentou ser mais acostumado com TypeScript, outro com JavaScript puro; ficou como decisão deixar em aberto o uso de qualquer um dos dois, sem framework de front-end, já que o sistema interno não precisa ser esteticamente elaborado);
- **Banco de dados:** **MySQL** escolhido em vez de PostgreSQL ou SQLite porque é a tecnologia que a maioria da equipe já domina (um integrante mencionou inclusive precisar praticar MySQL por conta da disciplina de Banco de Dados 2).

### Direção visual das duas aplicações
Foi comentado que a aplicação interna de gestão deve priorizar funcionalidade sobre estética interfaces simples, baseadas em tabelas, fáceis de ler rapidamente e carregando rápido (poucas telas). Já o site público poderia ser um pouco mais elaborado visualmente, com um formato parecido a um site de notícias cards de novidades/eventos, mas ficou como ponto em aberto quem teria permissão para publicar essas notícias no site, já que isso implica algum tipo de acesso de escrita além do simples formulário de inscrição.

## 3. Divisão de tarefas restantes do documento

A equipe revisou a divisão de tarefas do documento, notando que algumas pessoas (citadas: Ana e Alexandre) ficaram com partes muito grandes ou pesadas (incluindo o cronograma). Ficou definido:
- Ajuda mútua nas partes mais pesadas, um dos integrantes se disponibilizou para ajudar Ana e Alexandre nessas tarefas;
- A tarefa da Ana (não especificada com clareza na gravação, mas descrita como "gigantesca") será dividida entre duas pessoas, para não sobrecarregar uma pessoa só;
- O **cronograma** também foi levantado como tarefa a ser feita em dupla, já que é um tipo de tarefa considerada trabalhosa/demorada por mais de um integrante.

## 4. Abordagem, ciclo de vida e processo de desenvolvimento

Essa parte do documento foi resolvida ao vivo, em grupo, durante a própria reunião (ao invés de dividida individualmente), por ser considerada uma tarefa mais complexa e sujeita a gerar desigualdade de trabalho se dividida (a seção "5.2", cogitada por um integrante, foi descartada por esse motivo).

### Abordagem de desenvolvimento
A equipe decidiu adotar uma abordagem **híbrida** (nem puramente ágil, nem puramente dirigida por planos), já que:
- A equipe não teria estrutura para seguir uma abordagem 100% dirigida por planos ou ágil.

A estratégia combinada foi: basear-se em um modelo/ciclo de vida reconhecido, mas deixando claro que houve adaptações próprias sempre que necessário ("é baseado naquilo, mas com alterações nossas"), abordagem que, segundo relatos em aula, o professor aceita.

### Ciclo de vida
Foram avaliadas as opções de ciclo de vida (com base em material da disciplina, cruzando frequência de entrega e grau de mudança):
- **Preditivo (cascata):** descartado, não permite dividir o trabalho entre a equipe nem voltar a fases anteriores, e a entrega teria que ser de tudo de uma vez;
- **Ágil:** descartado, a equipe entende que não vai conseguir seguir todas as práticas ágeis de fato, e arriscaria ser questionada pelo professor por "não ser ágil de verdade";
- **Adaptativo:** descartado, considerado desproporcional ao tamanho e à maturidade do projeto (o escopo já está bem definido, não hoje há tanta exploração/incerteza que justifique esse ciclo);
- **Iterativo Incremental:** **escolhido**, permite quebrar o projeto em pedaços/incrementos menores, entregando o produto de forma gradual, com possibilidade de voltar e ajustar antes da entrega final. Considerado o mais viável dado o tempo disponível e a divisão de trabalho entre a equipe.

### Processo de desenvolvimento
Foram discutidos processos possíveis dentro da abordagem híbrida — Cascata, Spiral, RAD, DSDM, derivações do UP, Scrum e XP. A maior parte foi descartada:
- **Espiral:** descartado, considerado complexo/inviável dado o tempo da equipe;
- **Scrum/XP:** descartado, avaliado como arriscado, pois o professor tende a cobrar muitos detalhes específicos dessas metodologias que a equipe não teria como cumprir de fato;
- **Derivações do UP:** descartadas, dariam trabalho considerado desnecessário para o escopo do projeto;
- **RAD (Rapid Application Development):** **escolhido**. A equipe considerou esse processo o mais adequado, por ser baseado em prototipagem rápida e iterativa, com forte participação do cliente durante todo o processo (o que é viável, já que o cliente está bastante acessível) e por permitir retomar fases anteriores, ao contrário da cascata. As quatro fases do RAD foram identificadas: planejamento de requisitos, design do usuário (onde entram os protótipos de papel, baixa fidelidade ou alta fidelidade em Figma), construção (implementação) e cutover.

**Alerta levantado pela própria equipe:** na apresentação, o professor pode perguntar a qualquer integrante, de forma aleatória, o que é o RAD e a equipe reforçou a necessidade de todos estudarem bem esse processo (e não só o conteúdo da disciplina em si).

## 5. Ferramentas e reuniões

### Backlog e gerenciamento de tarefas
Foi discutido qual ferramenta usar para gerenciar o backlog do projeto (opções cogitadas: GitHub Projects, Trello, e uma ferramenta usada por um dos integrantes em outro contexto, citada como "PyPy"/ClickUp). A equipe decidiu usar o **GitHub Projects**, por já estar integrado ao repositório do projeto e ser mais simples de manter, mesmo reconhecendo que não é a opção mais "profissional" e por entenderem que o professor provavelmente vai cobrar o uso de alguma ferramenta desse tipo.

### Frequência de reuniões
- **Reuniões internas da equipe:** aproximadamente **uma vez por semana** (não há necessidade de reuniões diárias, já que a equipe não está seguindo Scrum/XP à risca);
- **Reuniões com o cliente:** frequência não totalmente fixa — cogitou-se algo em torno de **a cada 15 dias**, ou ao final de cada iteração/bloco de entrega, servindo para atualizar o cliente sobre o andamento e esclarecer dúvidas pendentes.

## 6. Composição da equipe e papéis

A equipe decidiu **não separar os papéis por front-end e back-end**. Em vez disso, o trabalho será dividido por **requisito/funcionalidade**: a pessoa responsável por um requisito (ex.: tela de login) implementa tanto a parte de front quanto a de back daquele requisito.

Papéis definidos para o documento:
- **Gerente de Projeto:** Marcos (também atua como desenvolvedor, como todos os demais);
- **Desenvolvedores:** todos os integrantes da equipe, listados individualmente por nome;
- A equipe considerou, mas **descartou** a criação de papéis formais separados de **Analista de Requisitos** (já que a disciplina em si é sobre requisitos, entendem que essa função já está implícita para todos) e de um **QA dedicado** de forma isolada;
- Ainda assim, ficou reconhecido que um dos integrantes já vinha informalmente cuidando de qualidade/testes (testes automatizados e pipeline de CI, com cobertura de testes citada em torno de 70%), o que pode ser refletido no documento como uma responsabilidade adicional dessa pessoa, sem necessariamente virar um papel formal isolado;
- Para a parte de **requisitos**, ficou definida uma pessoa como responsável/linha de frente: **Ana**, escolhida por votação entre os candidatos cogitados (Maria, Ana, Renato, Alexandre).

## 7. Convenção de documentação (boa prática levantada na reunião)

Foi levantada uma recomendação importante para o preenchimento do documento: **nunca escrever "todos" como responsável por uma atividade** — sempre listar os nomes específicos de cada integrante envolvido (ex.: "Marcos, Enzo, Maria"). A justificativa é que, se alguém trancar a disciplina ou sair do grupo depois, ou se alguém entrar mais tarde, escrever "todos" gera atribuição incorreta de responsabilidade (para mais ou para menos) sobre quem de fato participou daquela atividade.

## 8. Decisões

- **Arquitetura:** duas aplicações separadas, site público (somente escrita, sem portal do aluno) e aplicação de gestão interna, sem integração direta entre as duas;
- **Stack tecnológica (nesta reunião):** Python, Django, SQLAlchemy, HTML, CSS, JavaScript/TypeScript, MySQL — **posteriormente revista** (ver nota na seção 1);
- **Abordagem de desenvolvimento:** híbrida;
- **Ciclo de vida:** iterativo incremental;
- **Processo de desenvolvimento:** RAD (Rapid Application Development);
- **Ferramentas:** GitHub Projects para backlog; WhatsApp (equipe e cliente), Meet e Discord para comunicação;
- **Cadência de reuniões:** semanal internamente; aproximadamente quinzenal (ou por iteração) com o cliente;
- **Composição da equipe:** Gerente de Projeto (Marcos) + Desenvolvedores (todos, por requisito, sem divisão front/back); sem papéis formais de Analista de Requisitos ou QA dedicado; Ana como responsável pela parte de requisitos.

## 9. Pendências e próximos passos

- **Ana + colega a definir:** dividir e concluir a tarefa "gigantesca" atribuída a ela;
- **Dupla a definir:** finalizar o cronograma do projeto;
- **Todo o grupo:** estudar bem o processo RAD e a justificativa da abordagem híbrida/ciclo iterativo incremental escolhidos, para responder perguntas do professor na apresentação;
- **Marcos:** criar o grupo de WhatsApp com o cliente e adicionar os integrantes;
- **Todo o grupo:** ao preencher o documento, revisar se algum campo ficou com "todos" escrito de forma genérica e substituir pelos nomes específicos.

## 10. Pontos em aberto / dúvidas

- Ficou em aberto quem teria permissão para publicar notícias/conteúdo no site público (já que isso exigiria algum nível de acesso além do simples formulário de inscrição), não foi decidido nesta reunião;
- Não ficou claro, na gravação, qual foi exatamente a tarefa "gigantesca" atribuída à Ana que precisou ser dividida;
- A frequência exata das reuniões com o cliente não foi fixada com precisão (ficou como faixa aproximada de 15 dias/por iteração).
