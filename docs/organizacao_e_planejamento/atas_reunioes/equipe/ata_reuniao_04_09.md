# Ata de Reunião: Alinhamento de Stack Tecnológica e Documento do Projeto

## 1. Identificação da reunião

**Data:** 04/09/2026
**Modalidade:** Remota (chamada de vídeo)
**Participantes pela equipe:** Todos
**Participação externa:** Julia, monitora da disciplina
**Pauta:** Alinhamento de pendências do projeto, ajustes no GitHub Pages, decisão sobre mudança de stack tecnológica, e preenchimento da seção 11.1 do documento (lições aprendidas e dificuldades da Unidade 1)

## 2. Ajustes no GitHub Pages

A equipe estava organizando o card de apresentação do projeto na aba de início do GitHub Pages, incluindo todos os integrantes. Durante a reunião, houve uma tentativa de dar commit e rodar o deploy (`mkdocs gh-deploy`), mas o comando falhou com um erro de módulo não encontrado ("No module name mkdocs deploy"), mesmo tendo funcionado no dia anterior. Concluiu-se que o problema é uma incompatibilidade específica entre o Windows e o mkdocs no ambiente daquele integrante, não um problema do ambiente de desenvolvimento do projeto em si. A solução encontrada foi simplesmente não depender do Windows para rodar esse comando (outro integrante com ambiente funcional assume o deploy). Ficou como ideia para o futuro configurar uma esteira de CI no GitHub para automatizar esse processo.

## 3. Mudança de stack tecnológica

### Contexto e motivação
A stack definida anteriormente usava **Django** como framework principal, com o Django ORM para o banco de dados. Ao escrever a justificativa técnica do documento do projeto, um dos integrantes pesquisou mais a fundo sobre o Django e percebeu que ele é um framework grande demais para o que o projeto realmente precisa: em especial, todo o módulo de autenticação e gestão de login do Django seria desnecessário, porque **o controle de acesso do sistema será físico**: a parte de gerenciamento vai rodar apenas no servidor local do próprio cliente (a ONG), então só quem tem acesso físico a esse servidor consegue mexer no sistema; não haverá tela de login/autenticação dentro da aplicação. Essa definição já havia sido confirmada com o cliente (referido na conversa como "o moço" / possivelmente Pedro), que confirmou que é possível manter tudo local.

Diante disso, o objetivo passou a ser trocar o Django por uma tecnologia mais enxuta e específica para o que o projeto realmente precisa: basicamente, receber os dados de um formulário de inscrição preenchido digitalmente pelos alunos e disponibilizá-los para a equipe do cliente decidir manualmente (substituindo o processo de preencher e entregar o formulário em papel).

### Escolha do framework: Flask x FastAPI
Foram levantadas duas opções para substituir o Django:
- **Flask**: micro-framework tradicional, síncrono e minimalista, mais indicado para protótipos rápidos, aplicações simples ou baseadas em renderização de HTML;
- **FastAPI**: focado em alta performance, APIs assíncronas e validação rigorosa de dados, descrito como padrão mais moderno para microsserviços e aplicações de IA.

A equipe pesquisou as diferenças (inclusive consultando uma IA para ajudar a comparar as opções) e decidiu que o projeto, por ser mais voltado a uma comunicação simples de dados (parecido com um "blog com uma área de cadastro"), se encaixa melhor no perfil do **FastAPI**. A decisão foi tomada por consenso ao vivo (voto verbal, sem objeções).

### Manutenção do SQLAlchemy (ORM)
Foi discutido se valeria a pena também remover o **SQLAlchemy** (chamado na conversa de "SQL Alckmin"), usado como Object-Relational Mapper (ORM), ferramenta que permite definir tabelas do banco de dados usando classes Python, em vez de escrever SQL puro diretamente. Uma consulta a uma IA (com o contexto do projeto) sugeriu manter o SQLAlchemy, embora não fosse obrigatório usá-lo. A equipe decidiu por manter, porque facilita a escrita e a manutenção do código (relacionamentos e queries mais complexas ficam mais simples), mesmo reconhecendo que a ferramenta ficará "subutilizada" dado o pequeno porte do sistema, o que não é um problema, já que o sistema é interno e não tem exigência de desempenho crítica (a única régua citada foi não ultrapassar cerca de 2 segundos de resposta, o que não deve ser um problema).

### Stack final definida
Com a mudança, a stack tecnológica do projeto ficou definida como:
- Python
- FastAPI
- HTML
- CSS
- JavaScript (quando necessário)
- MySQL
- SQLAlchemy

## 4. Preenchimento da seção 11.1 do documento (lições aprendidas e dificuldades)

A equipe teve dificuldade em identificar problemas reais para essa seção do documento, já que, segundo os próprios integrantes, não enfrentaram nenhuma das dificuldades típicas citadas em exemplos de semestres anteriores (ex.: outro grupo relatou dificuldade em identificar claramente o problema do cliente, ou limitação de acesso contínuo ao cliente para validação, o que não é o caso desta equipe, já que o cliente mora perto de um dos integrantes e responde prontamente). Depois de conversarem bastante para tentar generalizar algo genuíno (sem inventar um problema que não existiu), chegaram a dois pontos:

1. **Organização das reuniões:** a equipe reconheceu que as reuniões são marcadas de forma pouco antecipada (no próprio dia em que vão ocorrer), em vez de já estarem pré-agendadas com antecedência. Como ação de melhoria, foi sugerido documentar os horários fixos de indisponibilidade de cada integrante (ex.: em uma tabela), e padronizar mais o ambiente de trabalho da equipe (templates de commit, de branch e de modelo de reunião/ata).
2. **Falta de compreensão de termos e conceitos da disciplina:** a equipe generalizou, para toda a equipe, uma dificuldade pontual que um integrante (Renato) teve para entender como produzir corretamente os "objetivos específicos" do projeto, problema também citado pela monitora como recorrente entre outros grupos (fácil de confundir com "características do produto").

Ficou definido que alguém (não especificado com clareza na gravação) ficaria responsável por escrever essa seção no documento.

## 5. Participação da monitora Julia

A monitora da disciplina, Julia, entrou na chamada no meio da reunião para acompanhar o andamento do grupo. Pontos levantados por ela:
- Já deu uma olhada rápida no documento da equipe e achou bom, mas avisou que vai revisar de novo quando estiver completo;
- Alertou que o professor (citado como "Jorge") costuma cobrar bastante a escrita dos objetivos específicos e das características do produto (que o pessoal costuma confundir), além do cronograma;
- Reforçou que o professor quer clareza sobre a proposta de solução e o problema que a equipe busca resolver junto ao cliente;
- Observou que, por ser um projeto de cunho social (uma ONG que sobrevive de doações), isso tende a ser bem recebido pelo professor, que costuma valorizar esse tipo de iniciativa;
- Sobre a apresentação: tem limite de **15 minutos** (o professor corta se passar do tempo, inclusive com cronômetro visível durante a apresentação); há também uma versão em **vídeo**, com o mesmo limite de tempo e o mesmo conteúdo da apresentação presencial; a apresentação presencial é feita por sorteio (nem todos os integrantes necessariamente apresentam); slides são opcionais; o professor acompanha a apresentação junto com o GitHub Pages do grupo, em tempo real; o conteúdo apresentado deve cobrir os pontos 1 a 7 e o 11.1 do documento.

## 6. Pendências administrativas

- Falta coletar a **matrícula** e o **usuário do GitHub** do Alexandre (seu nome completo já foi obtido através do Meet).

## 7. Outras tarefas em andamento

- Ajustes no **diagrama de Ishikawa** do projeto;
- Ajustes no **quadro comparativo**;
- Ambos serão commitados no GitHub Pages em seguida;
- O **cronograma** do projeto ainda está em produção (não finalizado até o momento da reunião).

## 8. Agendamento da próxima reunião (ensaio de apresentação)

A equipe tentou combinar um horário para um ensaio da apresentação, a ser feito depois que o documento e o GitHub Pages estiverem completos. Restrições levantadas ao vivo:
- Um integrante tem aniversário no domingo à noite (mas está livre à tarde);
- Outro integrante tem um concurso público no domingo à tarde (prova de 4 horas, das 15h às 19h, com fechamento de portão às 14h45); domingo inteiro fica inviável para essa pessoa;
- Segunda-feira é feriado, o que deixa a maioria mais disponível, embora alguns só consigam à noite.

## 9. Prazos e encaminhamentos

- **Todo o grupo:** finalizar o documento do projeto (cobrindo ao menos os pontos 1 a 7 e o 11.1) até **amanhã à noite, no mais tardar**, para depois ser passado para o Markdown/GitHub Pages;
- Quem tiver dificuldade ou não conseguir cumprir o prazo deve avisar no grupo do WhatsApp para receber ajuda de outro integrante;
- **Todo o grupo:** decidir, pelo grupo do WhatsApp, o horário do ensaio de apresentação (opções em jogo: sexta ou domingo à tarde/noite, ou segunda-feira, feriado);
- **Responsável não especificado:** escrever a seção 11.1 do documento com os pontos definidos na seção 4 desta ata;
- **Responsável não especificado:** coletar matrícula e usuário do GitHub do Alexandre.

*Ata elaborada a partir da transcrição de reunião remota da equipe do projeto, com participação parcial da monitora da disciplina, para conhecimento e alinhamento de todos os integrantes.*