# 2 SOLUÇÃO PROPOSTA


## 2.1 Objetivo Geral do Produto

O objetivo do produto é fortalecer a gestão do Centro Esportivo Cultural de Planaltina DF (CECP) por meio de um sistema de gestão de alunos e da instituição, substituindo o controle manual e descentralizado hoje utilizado pela instituição. A solução visa dar autonomia à coordenação, ampliar o alcance da instituição junto à comunidade. Do ponto de vista técnico, a solução será composta por uma única plataforma integrada, organizada em dois módulos que compartilham a mesma base de dados:

__Módulo público__: divulgação institucional e de eventos no MVP. A manifestação de interesse por pré-matrícula online (CP7) pertence ao pós-MVP e antecede a confirmação presencial da matrícula.

__Módulo administrativo__: no MVP, acesso da coordenação, cadastro e histórico de alunos e as operações de turmas selecionadas na [priorização](../../historico/10_backlog_produto.md). Frequência, medidas disciplinares, comunicação dirigida a voluntários e famílias e registro de doações e prestação de contas dependem dos requisitos pós-MVP. O acompanhamento de desempenho escolar ainda precisa de definição funcional com o cliente, conforme a seção 2.3.2.

## 2.2 Objetivos Específicos (OE) do Produto

- **OE1:** Centralizar os dados dos alunos em uma base tecnológica única, eliminando o uso de documentos físicos e registros manuais dispersos e viabilizando a gestão digital do CECP.
- **OE2:** Apoiar o acompanhamento da assiduidade dos alunos nas atividades do CECP. O acompanhamento das condicionalidades escolares permanece uma necessidade do negócio, cuja cobertura funcional ainda depende da definição registrada na seção 2.3.2.
- **OE3:** Apoiar a aplicação e o histórico de medidas disciplinares (advertências, suspensões e desligamentos), garantindo rastreabilidade das decisões tomadas pela coordenação.
- **OE4:** Facilitar a comunicação entre a coordenação do projeto, os voluntários e as famílias dos alunos, reduzindo a dependência de canais informais.
- **OE5:** Assegurar transparência na prestação de contas a parceiros, apoiadores e órgãos de fiscalização, dada a natureza de OSCIP da entidade.

### 2.2.1 Estratégia de Migração dos Dados Atuais

Dado que o cenário atual do CECP é predominantemente baseado em documentos físicos (ver seção 1), a migração dos registros existentes para o sistema não será automatizada: os dados hoje em fichas de papel e nos documentos já digitalizados serão inseridos/associados manualmente na plataforma pela equipe administrativa do CECP durante a fase de implantação, com apoio da equipe de desenvolvimento na definição do processo de carga inicial. Esses materiais existentes poderão ser usados como fonte de apoio para esse cadastro manual, mas não serão importados diretamente por não seguirem um formato padronizado.
## 2.3 Características de Produto (mapeadas com os Objetivos Específicos do Produto)

A tabela abaixo é a fonte principal dos vínculos OE–CP. As fichas de requisitos definem os vínculos CP–RF e RF–RNF, exibidos no [painel do escopo](../../painel.md). A matriz e o grafo da antiga seção 8 são registros históricos, não representações da rastreabilidade vigente.

As características abrangem a visão de evolução do produto; sua presença nesta tabela não implica inclusão integral no MVP. A entrega de cada requisito está indicada em sua ficha.


| OE principal | Contribuição secundária | ID | Característica | Descrição resumida | Valor de negócio principal |
|---|---|---|---|---|---|
| OE2 | OE1, OE3 | CP1 | Gestão e acompanhamento de turmas | A solução deverá oferecer uma plataforma digital que permita a criação, gerenciamento e inativação das turmas, de modo que permita o gerenciamento digital igual ao atualmente utilizado de forma analógica sem ferir as regras de negócios. | Apoio à operação, melhoria na gestão das turmas e melhoria da experiência dos administradores. |
| OE5 | OE1 | CP2 | Registro de doações e prestação de contas | Capacidade de registrar as doações e os recursos recebidos pela instituição (bens, solicitações por ofício e repasses de parcerias), sem processamento de pagamento online nesta fase. | Maior controle e transparência sobre os recursos recebidos pela instituição. |
| OE4 | OE5 | CP3 | Gestão de conteúdo institucional | Capacidade de a coordenação publicar e manter atualizadas as informações institucionais da organização (atividades, eventos e resultados), substituindo a dependência do Instagram e de um site desatualizado como únicos canais de divulgação. | Aumento da visibilidade e transparência da organização perante a comunidade, doadores e avaliadores de editais. |
| OE1 | — | CP4 | Cadastro e histórico de alunos | Capacidade de manter o cadastro e o histórico dos alunos vinculados à instituição. | Centralização da informação e suporte a comprovações históricas. |
| OE2, OE3 | — | CP5 | Acompanhamento pedagógico e disciplinar do aluno | Os RF26 a RF29 cobrem frequência nas aulas do CECP, alertas de faltas e registro de medidas disciplinares, no pós-MVP. O registro e a consulta de desempenho escolar ainda dependem de definição funcional (seção 2.3.2). | Apoio à tomada de decisão e rastreabilidade; a cobertura escolar ainda não está especificada. |
| OE4 | — | CP6 | Comunicação com voluntários e famílias | Capacidade de comunicação entre a coordenação, os voluntários e as famílias dos alunos. | Comunicação mais organizada e rastreável. |
| OE1 | OE2 | CP7 | Matrícula online (pré-matrícula) | Início remoto da inscrição, com análise pela coordenação e confirmação presencial, respeitando a RN02. O envio do formulário não conclui a matrícula. Fluxo e lacunas na seção 2.3.1; requisitos pós-MVP. | Facilitar o primeiro contato e o preenchimento prévio, preservando a etapa presencial. |

### 2.3.1 Pré-matrícula e conclusão presencial

A [ata de 22/09, seção 6](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_22_09.md) registra o pré-cadastro online que, confirmado presencialmente com assinatura do termo, se torna cadastro definitivo, deixando o formato exato em aberto. A [ata de 24/09, seção 3, CP7](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_24_09.md) exige análise da coordenação e afasta a conversão automática pelo simples envio do formulário. A [ata de 08/10, seção 8](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_09_10.md) mantém a pré-matrícula com aprovação presencial.

O fluxo documentado distingue:

1. **Manifestação de interesse / pré-matrícula online:** o interessado preenche a solicitação e recebe um protocolo (RF35 a RF41). Essa etapa inicia o processo e não substitui a matrícula presencial.
2. **Análise pela coordenação:** o RF42 permite consultar e classificar a solicitação como aprovada, recusada ou em lista de espera. A definição operacional do estado “aprovada” ainda precisa ser conciliada com a confirmação presencial.
3. **Comparecimento e assinatura presencial:** a [RN02](../escopo/regras_de_negocio.md#rn02) permanece aplicável às inscrições iniciadas online; o aceite online não elimina essa exigência.
4. **Conclusão do cadastro:** o RF21 cobre o cadastro pela coordenação. A ligação entre a solicitação analisada e esse cadastro, o momento da conversão e a forma de registrar a confirmação presencial ainda não estão detalhados.

Essas lacunas estão registradas na [PEN10](../../painel.md#PEN10). Não se presume que mudar o estado para “aprovada” conclua a matrícula ou dispense a RN02. Os requisitos de CP7 permanecem pós-MVP.

### 2.3.2 Limite do acompanhamento escolar

A [RN15](../escopo/regras_de_negocio.md#rn15) registra a relação do negócio entre participação no CECP e desempenho/assiduidade na escola de origem. A [ata de 17/09, seção 3](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_17_09.md) reconhece a necessidade escolar, mas não define quais dados serão registrados nem como ocorrerá o acompanhamento; a [ata de 24/09, seção 1](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_24_09.md) descreve a prática informal existente.

Os RF26 a RF29 tratam da frequência nas aulas do CECP e de medidas disciplinares. O tipo e o nome da escola previstos no RF21 são dados cadastrais, não um histórico de desempenho escolar. Assim, a visão não considera o registro e a consulta de desempenho escolar cobertos pelos requisitos atuais nem os promete como entrega do MVP. A [PEN11](../../painel.md#PEN11) solicita a definição com o cliente sobre dados necessários, acesso, forma de acompanhamento e inclusão ou adiamento dessa capacidade; não há periodicidade, critério de rendimento ou automação definidos nesta revisão.

## 2.4 Tecnologias a Serem Utilizadas

As ferramentas que serão utilizadas diretamente para a construção da proposta para o CECP foram escolhidas de acordo com a necessidade do projeto. Para o frontend serão utilizados o HTML, CSS e JavaScript, que são amplamente conhecidos pela equipe e permitem a implementação de interfaces responsivas. No backend será utilizado o FastAPI, que permite um backend mínimo, mas eficiente para receber e processar as requisições e realizar a comunicação com o banco de dados. Para a persistência de dados será utilizado o MySQL, considerando as necessidades de armazenamento e gerenciamento de dados dos alunos e doações, e o SQLAlchemy, um ORM que facilita a comunicação entre a aplicação e o banco de dados.

Para o desenvolvimento do projeto, serão utilizados o Git e o GitHub para o controle de versão, compartilhamento e desenvolvimento do projeto, o GitHub Projects para a aplicação do framework de gestão baseado em Kanban. Para a documentação do projeto, serão utilizados o Word, que permite a escrita de documentos no formato .docx e .pdf, MkDocs e MkDocs Materials, que permitem o desenvolvimento de uma página web em Markdown. Também serão considerados mecanismos de segurança e privacidade dos dados para atender aos requisitos da LGPD e contribuir para a conformidade com a legislação, garantindo a qualidade, o alinhamento e o respeito à ética, que são pontos-chave para o desenvolvimento desse projeto.

## 2.5 Pesquisa de Mercado e Análise Competitiva

O mercado de soluções de gestão voltadas a projetos sociais e esportivos no Brasil é composto majoritariamente por sistemas genéricos de gestão escolar ou de academias, que não contemplam as particularidades de uma organização social sem fins lucrativos como o CECP. Entre as soluções existentes, destacam-se:

- **Sistemas de gestão para academias e escolinhas esportivas** (como Pacto Soluções, EVO ou Gestão Fit), voltados principalmente para controle financeiro, mensalidades e agenda de aulas funcionalidades pouco relevantes para uma entidade que não cobra mensalidade dos alunos e cujo foco central é o acompanhamento socioeducacional.
- **Sistemas de gestão escolar** (como o SIGE ou plataformas similares usadas por escolas particulares), que possuem módulos robustos de boletim e frequência, mas são voltados à gestão pedagógica formal de uma instituição de ensino, não a um projeto social que apenas monitora o desempenho do aluno em sua escola de origem.
- **Planilhas eletrônicas** (como Google Sheets ou Excel Online), amplamente utilizadas por organizações do porte do CECP por serem de fácil adoção, baixo custo e permitirem inclusive edição simultânea por múltiplos usuários, mas que não oferecem funcionalidades específicas do domínio da instituição, como alertas automáticos de frequência crítica, histórico estruturado de medidas disciplinares ou controle de acesso por perfil de usuário, dependendo de organização manual pela equipe.

A proposta se diferencia por ser uma solução enxuta e de baixo custo, desenhada especificamente para o modelo de funcionamento de projetos sociais esportivos, sem módulos financeiros ou pedagógicos complexos. A necessidade de relacionar frequência, desempenho escolar e permanência no projeto orienta a evolução do produto, com os limites de cobertura descritos na seção 2.3.2. Adicionalmente, por ser desenvolvida sob medida, a solução busca um custo de aquisição e manutenção compatível com a realidade orçamentária de uma OSCIP mantida por voluntariado.

Dessa forma, a proposta se posiciona como uma solução sob medida, enxuta e alinhada à realidade orçamentária e operacional de uma organização esportiva, algo que nenhuma solução genérica de mercado atende de forma nativa.

## 2.6 Viabilidade da Proposta

A proposta é viável no contexto da disciplina, considerando o acesso ao cliente, o escopo definido e a possibilidade de entrega incremental de um MVP funcional ao final do semestre. Embora a equipe ainda esteja em processo de consolidação do domínio sobre algumas tecnologias e integrações, o projeto foi estruturado de forma compatível com essa realidade, com sprints de no máximo uma semana a depender da complexidade das entregas, priorização das funcionalidades essenciais e validações frequentes com a cliente.
 
O principal risco técnico está no gerenciamento de dados, uma vez que a transição de processos hoje registrados em papel para um sistema digital exige modelagem cuidadosa das entidades (alunos, matrículas, turmas, frequência, medidas disciplinares e documentos de doações/prestação de contas), além de mecanismos que garantam integridade e consistência das informações migradas. Esse risco é mitigado por meio da definição incremental do modelo de dados junto à cliente, reduzindo a probabilidade de inconsistências propagarem-se para as demais funcionalidades do sistema.
 
Assim, a proposta é considerada viável, desde que:
 
- O escopo do MVP permaneça controlado;
- As prioridades sejam mantidas; e
- A equipe preserve a estratégia de aprendizado contínuo ao longo do desenvolvimento.

## 2.7 Benefícios Esperados

**Benefícios previstos no MVP:** maior controle das fichas e do histórico cadastral de alunos, apoio às operações selecionadas de turmas e divulgação pública de informações institucionais e eventos. Essa divulgação amplia o acesso da comunidade às informações do CECP e complementa os canais existentes; não equivale à comunicação dirigida com famílias e voluntários nem à disponibilização de documentos de prestação de contas.

**Benefícios dependentes do pós-MVP:** acompanhamento de frequência e medidas disciplinares (CP5), avisos dirigidos a voluntários e famílias (CP6), registro de doações e documentos de prestação de contas (CP2) e início remoto da inscrição por pré-matrícula (CP7), mantendo a confirmação presencial. A classificação de entrega é consultada nas fichas pelo [painel](../../painel.md).

**Benefício ainda dependente de definição funcional:** acompanhamento do desempenho escolar, conforme a seção 2.3.2. Ele não é apresentado como capacidade já coberta pela especificação vigente.
## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.1 | 18/09/2026 | Ajustando conforme o feedback da issue: Unidade 1 - Solução proposta #14| [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.2 | 14/11/2026 | Issues #24 e #35: conciliação da pré-matrícula com as fontes; lacunas de confirmação presencial e acompanhamento escolar; benefícios por entrega e fonte dos vínculos OE–CP | Renato Gameiro | Pendente |
