# 2 SOLUÇÃO PROPOSTA


## 2.1 Objetivo Geral do Produto

O objetivo do produto é fortalecer a gestão do Centro Esportivo Cultural de Planaltina DF (CECP) por meio de um sistema de gestão de alunos e da instituição, substituindo o controle manual e descentralizado hoje utilizado pela instituição. A solução visa dar autonomia à coordenação, ampliar o alcance da instituição junto à comunidade. Do ponto de vista técnico, a solução será composta por uma única plataforma integrada, organizada em dois módulos que compartilham a mesma base de dados:

__Módulo público__: divulgação institucional e solicitação de matrícula online (pré-matrícula). A solicitação é analisada pela coordenação, e a matrícula só é efetivada presencialmente, com a assinatura dos termos pelo responsável legal ([RN02](../../painel.md#RN02)).
__Módulo administrativo__: cadastro e matrícula de alunos, turmas, frequência, medidas disciplinares, comunicação com voluntários e famílias, registro de doações e captação de recursos, e documentos de prestação de contas.

## 2.2 Objetivos Específicos (OE) do Produto

- **OE1:** Centralizar os dados dos alunos em uma base tecnológica única, eliminando o uso de documentos físicos e registros manuais dispersos e viabilizando a gestão digital do CECP.
- **OE2:** Garantir o acompanhamento pontual da assiduidade dos alunos nas aulas do CECP, permitindo à coordenação identificar rapidamente casos críticos e intervir antes da perda da vaga. Como premissa da equipe, ainda pendente de confirmação com o cliente ([DEC15](../../painel.md#DEC15), [PEN10](../../painel.md#PEN10)), o acompanhamento do desempenho na escola de origem, que também condiciona a permanência ([RN15](../../painel.md#RN15)), fica fora do sistema, sem registro de notas nem situação escolar.
- **OE3:** Apoiar a aplicação e o histórico de medidas disciplinares (advertências, suspensões e desligamentos), garantindo rastreabilidade das decisões tomadas pela coordenação.
- **OE4:** Facilitar a comunicação entre a coordenação do projeto, os voluntários e as famílias dos alunos, reduzindo a dependência de canais informais.
- **OE5:** Assegurar transparência na prestação de contas a parceiros, apoiadores e órgãos de fiscalização, dada a natureza de OSCIP da entidade.

### 2.2.1 Estratégia de Migração dos Dados Atuais

Dado que o cenário atual do CECP é predominantemente baseado em documentos físicos (ver seção 1), a migração dos registros existentes para o sistema não será automatizada: os dados hoje em fichas de papel e nos documentos já digitalizados serão inseridos/associados manualmente na plataforma pela equipe administrativa do CECP durante a fase de implantação, com apoio da equipe de desenvolvimento na definição do processo de carga inicial. Esses materiais existentes poderão ser usados como fonte de apoio para esse cadastro manual, mas não serão importados diretamente por não seguirem um formato padronizado.

**Como será feito (DEC32):** não haverá migração em lote. Depois da entrega, a própria coordenação cadastra os alunos ativos pelo sistema ([RF21](../escopo/requisitos/RF21.md)), aos poucos, usando as fichas em papel como fonte. A equipe apoia na primeira semana.

## 2.3 Características de Produto (mapeadas com os Objetivos Específicos do Produto)

A solução proposta para o CECP deverá contemplar, de forma preliminar, as seguintes características:


| OE principal | Contribuição secundária | ID | Característica | Descrição resumida | Valor de negócio principal |
|---|---|---|---|---|---|
| OE2 | OE1, OE3 | CP1 | Gestão e acompanhamento de turmas | A solução deverá oferecer uma plataforma digital que permita a criação, gerenciamento e inativação das turmas, de modo que permita o gerenciamento digital igual ao atualmente utilizado de forma analógica sem ferir as regras de negócios. | Apoio à operação, melhoria na gestão das turmas e melhoria da experiência dos administradores. |
| OE5 | OE1 | CP2 | Registro de doações e prestação de contas | Capacidade de registrar as doações e os recursos recebidos pela instituição (bens, solicitações por ofício e repasses de parcerias), sem processamento de pagamento online nesta fase. | Maior controle e transparência sobre os recursos recebidos pela instituição. |
| OE4 | OE5 | CP3 | Gestão de conteúdo institucional | Capacidade de a coordenação publicar e manter atualizadas as informações institucionais da organização (atividades, eventos e resultados), substituindo a dependência do Instagram e de um site desatualizado como únicos canais de divulgação. | Aumento da visibilidade e transparência da organização perante a comunidade, doadores e avaliadores de editais. |
| OE1 | — | CP4 | Cadastro e histórico de alunos | Capacidade de manter o cadastro e o histórico dos alunos vinculados à instituição. | Centralização da informação e suporte a comprovações históricas. |
| OE2, OE3 | — | CP5 | Acompanhamento de frequência e disciplinar do aluno | Capacidade de acompanhar a frequência dos alunos nas aulas do CECP e de registrar as medidas disciplinares aplicadas. A restrição a frequência e medidas disciplinares, deixando informações da escola de origem (notas, situação escolar) fora do escopo, é uma premissa da equipe ainda pendente de confirmação com o cliente (DEC15/PEN10). | Redução da evasão, apoio à tomada de decisão e rastreabilidade. |
| OE4 | — | CP6 | Comunicação com voluntários e famílias | Capacidade de comunicação entre a coordenação, os voluntários e as famílias dos alunos. | Comunicação mais organizada e rastreável. |
| OE1 | OE2 | CP7 | Matrícula online | A solução deverá oferecer um formulário público para que interessados enviem a solicitação de matrícula sem precisar comparecer para dar o primeiro passo. A coordenação analisa a solicitação (aprovada, recusada ou lista de espera); a aprovada é concluída presencialmente, com a assinatura dos termos pelo responsável legal ([RN02](../../painel.md#RN02)), e só então o aluno passa a ter cadastro definitivo ([RF21](../escopo/requisitos/RF21.md)). | Aumento da conversão de matrícula e diversificação de meios de matrícula. |

## 2.4 Tecnologias a Serem Utilizadas

As ferramentas que serão utilizadas diretamente para a construção da proposta para o CECP foram escolhidas de acordo com a necessidade do projeto. Para o frontend serão utilizados o HTML, CSS e JavaScript, que são amplamente conhecidos pela equipe e permitem a implementação de interfaces responsivas. No backend será utilizado o FastAPI, que permite um backend mínimo, mas eficiente para receber e processar as requisições e realizar a comunicação com o banco de dados. Para a persistência de dados será utilizado o MySQL, considerando as necessidades de armazenamento e gerenciamento de dados dos alunos e doações, e o SQLAlchemy, um ORM que facilita a comunicação entre a aplicação e o banco de dados.

Para o desenvolvimento do projeto, serão utilizados o Git e o GitHub para o controle de versão, compartilhamento e desenvolvimento do projeto, o GitHub Projects para a aplicação do framework de gestão baseado em Kanban. Para a documentação do projeto, serão utilizados o Word, que permite a escrita de documentos no formato .docx e .pdf, MkDocs e MkDocs Materials, que permitem o desenvolvimento de uma página web em Markdown. Também serão considerados mecanismos de segurança e privacidade dos dados para atender aos requisitos da LGPD e contribuir para a conformidade com a legislação, garantindo a qualidade, o alinhamento e o respeito à ética, que são pontos-chave para o desenvolvimento desse projeto.

## 2.5 Pesquisa de Mercado e Análise Competitiva

O mercado de soluções de gestão voltadas a projetos sociais e esportivos no Brasil é composto majoritariamente por sistemas genéricos de gestão escolar ou de academias, que não contemplam as particularidades de uma organização social sem fins lucrativos como o CECP. Entre as soluções existentes, destacam-se:

- **Sistemas de gestão para academias e escolinhas esportivas** (como Pacto Soluções, EVO ou Gestão Fit), voltados principalmente para controle financeiro, mensalidades e agenda de aulas funcionalidades pouco relevantes para uma entidade que não cobra mensalidade dos alunos e cujo foco central é o acompanhamento socioeducacional.
- **Sistemas de gestão escolar** (como o SIGE ou plataformas similares usadas por escolas particulares), que possuem módulos robustos de boletim e frequência, mas são voltados à gestão pedagógica formal de uma instituição de ensino, não a um projeto social que apenas monitora o desempenho do aluno em sua escola de origem.
- **Planilhas eletrônicas** (como Google Sheets ou Excel Online), amplamente utilizadas por organizações do porte do CECP por serem de fácil adoção, baixo custo e permitirem inclusive edição simultânea por múltiplos usuários, mas que não oferecem funcionalidades específicas do domínio da instituição, como alertas automáticos de frequência crítica, histórico estruturado de medidas disciplinares ou controle de acesso por perfil de usuário, dependendo de organização manual pela equipe.

A proposta se diferencia por ser uma solução enxuta e de baixo custo, desenhada especificamente para o modelo de funcionamento de projetos sociais esportivos: sem módulos financeiros ou pedagógicos complexos, mas com foco na frequência, nas medidas disciplinares e na permanência do aluno no projeto. A relação com o desempenho escolar é uma regra de negócio do CECP, cujo acompanhamento no sistema permanece pendente de confirmação com o cliente (DEC15/PEN10). Adicionalmente, por ser desenvolvida sob medida, a solução tem custo de aquisição e manutenção compatível com a realidade orçamentária de uma OSCIP mantida por voluntariado.

Dessa forma, a proposta se posiciona como uma solução sob medida, enxuta e alinhada à realidade orçamentária e operacional de uma organização esportiva, algo que nenhuma solução genérica de mercado atende de forma nativa.

## 2.6 Viabilidade da Proposta

A proposta é viável no contexto da disciplina, considerando o acesso ao cliente, o escopo definido e a possibilidade de entrega incremental de um MVP funcional ao final do semestre. Embora a equipe ainda esteja em processo de consolidação do domínio sobre algumas tecnologias e integrações, o projeto foi estruturado de forma compatível com essa realidade, com sprints de no máximo uma semana a depender da complexidade das entregas, priorização das funcionalidades essenciais e validações frequentes com a cliente.
 
O principal risco técnico está no gerenciamento de dados, uma vez que a transição de processos hoje registrados em papel para um sistema digital exige modelagem cuidadosa das entidades (alunos, matrículas, turmas, frequência, medidas disciplinares e documentos de doações/prestação de contas), além de mecanismos que garantam integridade e consistência das informações migradas. Esse risco é mitigado por meio da definição incremental do modelo de dados junto à cliente, reduzindo a probabilidade de inconsistências propagarem-se para as demais funcionalidades do sistema.
 
Quanto ao esforço, os 18 RFs do MVP somam até cerca de 45 horas de implementação, incluindo persistência, validação, segurança e testes, frente a cerca de 168 horas disponíveis da equipe nas Iterações 5 a 10. O cálculo e a justificativa da matriz estão na [seção 10.2.3 do backlog](../../historico/10_backlog_produto.md#1023-justificativa-da-matriz-e-viabilidade-do-mvp).
 
Assim, a proposta é considerada viável, desde que:
 
- O escopo do MVP permaneça controlado;
- As prioridades sejam mantidas; e
- A equipe preserve a estratégia de aprendizado contínuo ao longo do desenvolvimento.

## 2.7 Benefícios Esperados

- **Para o Cliente:** Maior controle e facilidade de acesso às fichas e ao histórico dos alunos, reduzindo a dependência de fichas de papel e facilitando o gerenciamento dos dados e das turmas. O acompanhamento consolidado de frequência e de medidas disciplinares e o registro de doações são incrementos pós-MVP.
- **Para o candidato a aluno (Usuário):** Outra opção de solicitar a matrícula no CECP de forma remota, removendo a necessidade de comparecer presencialmente para dar o primeiro passo (a matrícula é concluída presencialmente). *Pós-MVP.*
- **Para os voluntários e famílias (Usuário):** Um canal de comunicação mais direto com a coordenação, reduzindo a dependência de canais informais. *Pós-MVP.*
- **Para os avaliadores do edital (Usuário):** Uma interface e disposição dos dados e documentos de prestação de contas necessários para a avaliação de acordo com as normas dos editais. *Pós-MVP.*
- **Para a coordenação, em relação às doações:** Um novo meio de registrar e acompanhar os itens e recursos recebidos, permitindo maior controle e transparência. *Pós-MVP.*
- **Para a comunidade (Usuário):** Informações institucionais e eventos atualizados em um canal próprio, sem depender apenas do Instagram. *No MVP.*

## 2.8 O que o MVP entrega

O MVP tem 18 RFs ([DEC03](../../painel.md#DEC03), validado pelo cliente em 30/10/2026). Ele não entrega todos os objetivos: os demais RFs são incrementos pós-MVP, que entram se houver capacidade e validação do cliente.

| OE | No MVP | Fora do MVP (pós-MVP) | Situação no MVP |
| :--- | :--- | :--- | :--- |
| OE1 | Cadastro, edição, consulta e inativação do aluno (RF21 a RF24); turmas (RF03, RF06, RF07) | Remoção de dados (RF25); matrícula online (CP7) | Atendido em parte |
| OE2 | — | Frequência e alertas (RF26 a RF28) | Não atendido |
| OE3 | — | Medidas disciplinares (RF29) | Não atendido |
| OE4 | Divulgação institucional e eventos (RF13 a RF20) | Avisos para voluntários e famílias (CP6) | Atendido em parte |
| OE5 | Divulgação pública de atividades e resultados (RF13 a RF20, contribuição secundária) | Doações e prestação de contas (CP2) | Não atendido |

O acesso à área administrativa (RF00 a RF02) é pré-requisito de todos os itens do MVP.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.1 | 18/09/2026 | Ajustando conforme o feedback da issue: Unidade 1 - Solução proposta #14| [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.2 | 14/11/2026 | Issue #24: fluxo da matrícula online consolidado (pré-matrícula online e efetivação presencial, RN02) em 2.1 e CP7; OE2 e CP5 restritos a frequência e disciplina (desempenho escolar fora do escopo); benefícios marcados como MVP ou pós-MVP; nova seção 2.8 | — |  |
| 1.3 | 15/11/2026 | Issue #33: seção 2.6 compara o esforço estimado do MVP com as horas disponíveis da equipe | — |  |
