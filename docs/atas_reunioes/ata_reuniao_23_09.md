# Ata de Reunião  Apresentação e Validação de Requisitos (CECP)

**Data:** Quarta-feira, 23 de setembro de 2026
**Modalidade:** Presencial
**Participantes pela equipe do projeto:** Marcos
**Participantes representando o cliente (CECP):** Ivan (presidente) e Sandra (Tesoureira)
**Pauta:** Apresentação, pela equipe, do levantamento de requisitos consolidado até aqui (funcionais e não funcionais), para validação ponto a ponto com o cliente

> Nota: esta ata cobre uma reunião única, registrada em dois áudios porque o celular usado para gravar descarregou no meio da conversa. O conteúdo é contínuo (a segunda gravação retoma exatamente de onde a primeira parou, na "gestão de conteúdo institucional").


## 1. Abertura e dinâmica da reunião

Marcos apresentou novamente o contexto do projeto a todos os presentes (inclusive à Sandra, que não participava da reunião anterior), para que todos ficassem "inteirados do assunto": trata-se de um projeto de uma disciplina da faculdade, feito para a ONG, com o objetivo de reduzir a dependência de papel.

Foi explicado que a reunião seria conduzida passando funcionalidade por funcionalidade já levantada, pedindo a aprovação (feedback) do Ivan e da Sandra em cada uma. Marcos reforçou, mais de uma vez ao longo da reunião, que **o projeto não é da equipe, é da ONG**  ou seja, qualquer parte não aprovada seria refeita quantas vezes fosse necessário até refletir o que o cliente precisa, e que o documento de requisitos é "vivo" (pode mudar).

## 2. Visão geral da arquitetura do sistema

Foi apresentada a estrutura geral do sistema, dividida em dois módulos:
- **Módulo público:** divulgação, informações institucionais, fotos e vídeos  acessível a qualquer visitante do site;
- **Módulo administrativo:** onde a ONG vai substituir os processos que hoje são feitos no papel, com acesso restrito por login.


## 3. Gestão e acompanhamento de turmas

Funcionalidade apresentada e **validada** pelo Ivan e pela Sandra:
- Cadastrar turma;
- Editar turma;
- Inativar turma;
- Associar aluno a uma turma;
- Listar/consultar turmas e quantos alunos há em cada uma (ex.: "quantos alunos tem no jiu-jitsu").

Foi destacado pelos os stakeholders que essa listagem facilita, por exemplo, responder perguntas de doadores sobre quantas pessoas o projeto atende, e que o mesmo cadastro vai comportar as modalidades já existentes (judô, jiu-jitsu, vôlei) e futuras (ex.: futebol, citado como modalidade a ser adicionada).

### Situação atual do vôlei (levantamento de contexto)
- Diferente do judô/jiu-jitsu, o vôlei tem hoje pouca documentação organizada;
- Ivan afirmou não conhecer bem a operação do vôlei  quem tem mais conhecimento é a Sandra;
- Os responsáveis pela modalidade são dois professores: **Genevaldo** (educação física) e **Ricardo** (não confirmado se é formado em educação física, mas é quem está à frente do vôlei hoje, com mais experiência na modalidade);
- Existe ficha de inscrição em papel apenas para os alunos mais antigos; alunos novos que entraram não têm ficha preenchida;
- Ficou combinado que esses dados serão lançados no sistema assim que possível, incluindo foto do aluno, para ter o registro correto.

## 4. Cadastro, edição, consulta e inativação de aluno

Requisitos apresentados e validados:
- Cadastrar aluno;
- Editar informações do aluno;
- Consultar a ficha do aluno (ex.: caso um pai peça um documento que comprove a participação da filha);
- **Inativar** aluno  Marcos destacou explicitamente que **não pode haver exclusão** de aluno do sistema, apenas inativação, para preservar o histórico. Ivan confirmou que hoje já funciona assim no papel (guarda as fichas antigas em uma caixa de arquivo) e que pretende manter esse histórico **para sempre**, sem prazo de descarte.
- O sistema deve permitir consultar quantos alunos estão ativos e quantos estão inativos.

### Documentos hoje exigidos na inscrição (contexto levantado)
- Identidade;
- CPF;
- Comprovante de residência;
- Foto 3x4;
- Atestado para prática de esporte;
- Se o aluno for menor de idade: cópia do RG e do CPF do responsável, e o responsável precisa comparecer presencialmente para assinar a inscrição.

Hoje existem **duas fichas**: uma de inscrição e outra que funciona como um questionário de liberação, usado quando o atestado médico ainda não foi trazido pelos pais no momento da inscrição.

Ficou em aberto se os documentos anexados ao sistema serão sempre escaneados ou também poderão ser inseridos manualmente  Marcos deixou claro que o sistema deve suportar o formato que a ONG já usa no dia a dia, e não impor um formato único.

## 5. Direito de imagem e uso de dados dos alunos

Ivan relatou um caso concreto (sem citar nomes) em que foi questionado sobre o direito de imagem de uma criança  um responsável alegou que a ONG não poderia divulgar a imagem do filho, mesmo ele tendo autorizado a participação no projeto e em competições.

A partir desse relato, foi levantado como requisito:
- O sistema deve armazenar/vincular à ficha do aluno o **termo/contrato assinado pelos pais** autorizando o uso da imagem;
- Esse termo deve deixar claro, de forma explícita para o responsável no momento da assinatura, que a imagem poderá ser usada durante a participação do aluno no projeto e por um período determinado após a saída dele (o prazo exato  "x dias" ou "tempo determinado"  **ainda não foi definido**, ficou como ponto em aberto);
- O sistema deve permitir **consultar rapidamente** esse termo assinado, para que a equipe consiga responder de forma objetiva caso um responsável questione o uso da imagem;
- Foi reforçado que essa autorização é importante também porque órgãos públicos que fazem doações (ex.: Ministério Público) frequentemente pedem fotos dos beneficiados como parte da prestação de contas, e a ONG precisa estar respaldada para poder tirar e usar essas fotos.
- A ficha de inscrição atual já contém uma cláusula de autorização de uso de imagem, mas Ivan e Sandra concordaram que ela deve ficar mais explícita/clara para o responsável no momento da assinatura, para evitar dúvidas futuras.

## 6. Pré-cadastro / matrícula online (ideia proposta durante a reunião)

Sandra sugeriu, durante a apresentação, que o sistema permitisse que o interessado iniciasse a inscrição remotamente pelo próprio site, preenchendo previamente os dados possíveis (ex.: CPF), de forma que, ao comparecer presencialmente, faltasse apenas completar informações pendentes e assinar o termo.

Marcos confirmou que a equipe já havia cogitado algo parecido ("matrícula online"), mas ainda não tinha sido apresentado  a equipe estava esperando essa reunião para decidir o melhor formato. Ficou definido como ideia validada em princípio (Ivan e Sandra gostaram), mas o **formato exato ainda precisa ser desenhado** pela equipe: um pré-cadastro online que, ao ser confirmado presencialmente (com assinatura do termo), vira cadastro definitivo.

## 7. Gestão de conteúdo institucional (módulo público)

Requisitos apresentados e validados:
- Publicar conteúdo no módulo público (informações da organização, fotos, imagens);
- Editar conteúdo publicado;
- Remover conteúdo;
- Publicar eventos (ex.: exame de faixa, outros eventos que a ONG já produz e divulga hoje);
- Consultar os conteúdos publicados.

Foi destacado explicitamente que o objetivo **não é substituir o Instagram** nem o WhatsApp como canal de divulgação, e sim complementar: cada canal atinge um público diferente, e o site amplia o alcance para outros públicos que os canais atuais não cobrem.

## 8. Comunicação com voluntários e famílias

Requisitos apresentados e validados:
- Publicar avisos (ex.: "vai ter um evento interno de judô tal dia");
- Consultar avisos publicados;
- Direcionar avisos a um público específico (ex.: um aviso só para os voluntários, outro só para os alunos de uma modalidade);
- Consultar o histórico de avisos, incluindo a data em que cada aviso foi publicado (hoje esse controle não existe  só se sabe a data do evento, não a data em que o aviso foi dado).

**Ideia extra sugerida durante a reunião:** um QR Code, fixado em um quadro de avisos físico na sede, que levaria diretamente à área de avisos do site  permitindo que quem está fisicamente na ONG também acompanhe os avisos publicados digitalmente. Ideia bem recebida, mas sem aprofundamento adicional.

## 9. Doações e prestação de contas

Requisitos apresentados e validados:
- Registrar uma doação recebida no sistema;
- Listar/consultar as doações registradas;
- Registrar o documento de prestação de contas referente a uma doação, associando: vídeos (ex.: entrega de kimonos), orçamentos e a nota fiscal da compra realizada;
- Consultar a prestação de contas e as doações já registradas.

Esse ponto se conecta diretamente à questão de direito de imagem (seção 5): as fotos usadas na prestação de contas dependem da autorização de imagem do aluno estar em ordem.

## 10. Gestão institucional e financeira da ONG (levantamento de contexto)

Marcos relatou que, na reunião anterior, havia perguntado ao Ivan como funciona a gestão da ONG (além da gestão dos alunos), mas o Ivan não tinha conseguido detalhar esse ponto sozinho  por isso essa parte foi aprofundada agora, com a Sandra, que cuida da parte financeira.

### Captação de recursos via editais e ofícios
- A ONG envia ofícios a órgãos públicos federais (de Brasília e de outros estados) sempre que sai um edital de doação (ex.: doação de imóveis ou equipamentos de informática);
- Para enviar esses ofícios, a documentação institucional precisa estar **sempre atualizada**. Os documentos citados como necessários foram:
  - Certidão de OSCIP;
  - CND (Certidão Negativa de Débitos), incluindo a trabalhista;
  - Certidão de FGTS;
  - CNPJ;
  - Certidão da Secretaria da Fazenda do DF (citada como "CEPAS").
- Foi dado um exemplo concreto de risco: se a ONG estiver com o IPVA de algum veículo em atraso, a certidão correspondente não sai atualizada, e isso pode inviabilizar a participação em um edital.
- Estrutura de diretoria da ONG, conforme relatado: Ivan é o presidente; Sandra é a vice-presidente e tesoureira; William (filho do Ivan) também foi mencionado, mas não como parte da diretoria formal.

### Controle de bens recebidos por doação
- A ONG recebe doações de bens (ex.: veículos, móveis, computadores), que depois são reformados e revendidos para gerar capital para o projeto (pagar contas, comprar materiais, custear viagens a competições, etc.);
- **Hoje não existe nenhum controle formal desse processo**  segundo a própria Sandra, esse controle "está tudo na cabeça"/"no chute": não há registro de quanto foi gasto (frete, conserto, transferência do veículo) nem de quanto foi obtido na venda, então não dá para saber com precisão o lucro de cada bem;
- Foi dado como exemplo detalhado o caso de doação de um veículo: custos envolvidos incluem frete (pode variar de ~R$1.500 a R$4.000, dependendo da distância  doações de fora de Brasília, como Pernambuco, Pará, Santa Catarina ou Porto Alegre, custam mais), conserto mecânico, transferência de propriedade (documentação, placa, IPVA);
- A ONG relatou que **não recusa doações**, mesmo sabendo que pode ter prejuízo em alguns casos (ex.: doação de móveis de um ministério que renderam prejuízo no frete), porque recusar uma doação pode fazer com que aquele órgão pare de oferecer futuras doações;
- Ficou explícito, como necessidade levantada, ter uma **planilha/controle de entrada e saída de bens**, permitindo registrar valor estimado, custos associados e status (reformado, vendido, disponível).

### Informações institucionais no site público
- O site atual está desatualizado ("tudo bagunçado"), inclusive com fotos antigas do próprio Ivan (usadas como exemplo de desatualização);
- Foi levantada a necessidade de reunir e publicar, no módulo público, os dados institucionais da ONG: CNPJ, diretoria (presidente, vice-presidente, tesoureiro), dados bancários (conta corrente) e possivelmente uma chave Pix (a ser confirmada  Sandra não tinha certeza se a ONG já usa Pix);
- Foi levantada a necessidade de uma área pública de **"Como ajudar"** (doações), similar a exemplos de outros sites mostrados durante a reunião.

## 11. Objetivo geral e objetivos específicos do projeto (reapresentados)

Marcos reapresentou o objetivo do projeto para os presentes, reforçando que a equipe não vai conseguir resolver tudo da gestão da ONG, e sim focar no que for possível dentro do escopo:

**Objetivo geral:** dar mais autonomia à coordenação da ONG e mais alcance à comunidade, reduzindo a dependência do papel e dando mais controle sobre os próprios processos.

**Objetivos específicos apresentados:**
- Centralizar os dados dos alunos;
- Garantir o acompanhamento das condições e da pontualidade (frequência) dos alunos;
- Apoiar a aplicação e o histórico de medidas disciplinares aplicadas a um aluno;
- Facilitar a comunicação entre a ONG, os voluntários e as famílias;
- Garantir transparência na prestação de contas, inclusive para apoiar as exigências dos órgãos federais.

## 12. Acompanhamento pedagógico e disciplinar

Foi retomado o ponto (já levantado na reunião anterior) de que o desempenho escolar do aluno pode gerar medidas dentro do projeto  por exemplo, um aluno que vai mal na escola pode receber uma restrição temporária no judô/jiu-jitsu. Hoje isso é difícil de acompanhar porque não há um controle estruturado de frequência.

Requisitos apresentados e validados:
- Registrar a frequência (presença) do aluno;
- Consultar a frequência de um aluno;
- Emitir um **alerta de falta crítica** quando o número de faltas ultrapassar um limite definido pela ONG.

Sobre esse limite, houve uma pequena negociação ao vivo: o judô já usa informalmente o número de 10 faltas como referência, mas ficou definido que o sistema vai emitir o alerta antes disso  quando o aluno atingir 8 faltas  para dar tempo de a coordenação agir (conversar com a família, registrar as medidas tomadas) antes de chegar ao limite máximo.

## 13. Requisitos não funcionais e critérios de aceite

Esta parte da reunião foi conduzida de forma diferente das demais: cada requisito não funcional foi apresentado já com um **critério de aceite** proposto pela equipe, e Ivan/Sandra validaram (ou ajustaram) cada número ao vivo.

| Categoria | Requisito | Critério de aceite validado |
|---|---|---|
| Usabilidade | Interface deve permitir realizar tarefas sem necessidade de treinamento ou experiência técnica prévia | Um usuário novo deve conseguir concluir uma tarefa em até **8 minutos**, para pelo menos **80% dos usuários** (número negociado ao vivo  chegou a se cogitar 5 min e citou-se que sistemas mais "chatos" levam até 15 min; 8 minutos foi o valor aceito) |
| Responsividade | Interface deve se adaptar a qualquer tamanho de tela (computador, tablet, celular) | Conteúdo não pode se sobrepor (ex.: ícone em cima de texto) nem ser cortado, em nenhum tamanho de tela |
| Qualidade de imagem | Deve haver uma qualidade mínima de exibição de imagem | Mínimo de **360p** |
| Feedback ao usuário | Toda ação crítica deve informar sucesso ou erro | Mensagem de sucesso/erro exibida em até **2 segundos** após a ação |
| Confirmação de ações críticas | Ações que alteram dados relevantes (ex.: inativar aluno, inativar turma, aplicar medida disciplinar) devem pedir confirmação antes de serem executadas | Caixa de confirmação exibida antes de inativar turma, inativar aluno ou aplicar medida disciplinar |
| Confiabilidade | Histórico de aluno inativado deve ser preservado | Registros do aluno permanecem acessíveis no banco de dados mesmo após a inativação, sem prazo de expiração |
| Desempenho (consultas internas) | Sistema deve responder rápido às ações do usuário já autenticado | Resposta de consultas internas em até **3 segundos** |
| Desempenho (carregamento inicial) | Página deve carregar mesmo em conexão ruim | Conteúdo principal visível em até **5 segundos**, mesmo em conexão 2G |
| Capacidade / concorrência | Sistema deve suportar múltiplos usuários ao mesmo tempo sem perder desempenho | Suportar ao menos **10 usuários autenticados simultâneos**, mantendo os tempos de resposta acima (3s/5s) |
| Log de auditoria | Toda ação crítica deve ficar registrada | Registro de usuário responsável e timestamp (data/hora) para toda criação, edição ou inativação de turma/aluno |
| Compatibilidade | Sistema deve funcionar em diferentes sistemas operacionais e navegadores | Deve funcionar corretamente em Windows, no mínimo nos navegadores Chrome, Firefox e Safari |
| Controle de acesso / segurança | Sistema deve restringir funcionalidades por perfil de usuário | Aluno (perfil comum) não pode acessar funcionalidades administrativas; tentativa de acesso indevido deve retornar erro específico de "não autorizado" |
| Segurança de dados | Senhas e dados sensíveis devem ser protegidos | Senhas armazenadas com hash (nunca em texto puro); dados sensíveis criptografados |
| Conformidade legal | Tratamento de dados pessoais deve seguir a legislação brasileira | Sistema deve estar em conformidade com a **LGPD** (Lei Geral de Proteção de Dados) |

Ao final dessa parte, Ivan e Sandra confirmaram não ter dúvidas sobre os critérios apresentados.

## 14. Metodologia e cronograma do projeto

Marcos explicou que o projeto está dividido em quatro unidades/etapas:
1. **Levantamento inicial** (já concluído  reuniões anteriores com o Ivan);
2. **Análise e consenso**  etapa atual, em que todos (equipe, Ivan, Sandra) precisam estar alinhados sobre o que será construído;
3. **Construção**  início previsto para o mês seguinte (codificação e design do sistema);
4. **Entrega final**  integração e finalização do projeto, com previsão para **dezembro de 2026**.

Foi reforçado, mais uma vez, que ao longo de toda a construção (design, funcionalidades) a equipe vai continuar validando cada entrega com a ONG antes de seguir adiante  inclusive o design visual do sistema, que também será submetido à aprovação de Ivan e Sandra.

## 15. Implantação do sistema

Ivan confirmou que a ONG já possui servidor(es) próprios, e que o sistema será implantado localmente, na própria sede. A implementação/instalação ficará a cargo da equipe de Marcos  ele mencionou que os colegas de equipe estão à disposição para ir até a sede se for necessário, mas que, caso não seja preciso, ele mesmo fará a implantação junto com o Ivan.

## 16. Regras de negócio identificadas

- **RN01**  Aluno nunca pode ser excluído do sistema; a única ação permitida é inativação, preservando o histórico.
- **RN02**  Toda inscrição, mesmo iniciada remotamente por pré-cadastro, exige a presença física do responsável para assinatura do termo.
- **RN03**  O uso da imagem de um aluno depende de autorização assinada pelo responsável, com validade vinculada à participação do aluno no projeto e por um período adicional após a saída (prazo exato ainda não definido).
- **RN04**  A documentação institucional da ONG (certidões de OSCIP, FGTS, CND, CNPJ, Secretaria da Fazenda) precisa estar sempre atualizada para viabilizar a participação em editais de doação; pendências como IPVA em atraso podem impedir a emissão de uma certidão.
- **RN05**  A ONG evita recusar doações, mesmo quando o custo (frete, conserto) supera o benefício imediato, para preservar o relacionamento com os órgãos doadores e manter futuras doações.
- **RN06**  Órgãos públicos que fazem doações (ex.: Ministério Público) costumam exigir fotos dos beneficiados como parte da prestação de contas.

## 17. Pendências e próximos passos

- **Equipe:** detalhar o formato exato do pré-cadastro/matrícula online (seção 6);
- **Ivan/Sandra:** levantar e organizar a documentação dos alunos de vôlei que ainda não têm ficha preenchida (seção 3);

## 18. Pontos em aberto / dúvidas

Ao final da reunião, Ivan e Sandra confirmaram não ter dúvidas adicionais sobre o que foi apresentado.


*Ata elaborada a partir da transcrição de reunião presencial entre Marcos, Ivan e Sandra (representantes do CECP), realizada em 23/09/2026 e registrada em dois áudios devido à descarga da bateria do celular durante a gravação, para conhecimento e alinhamento do restante da equipe do projeto.*