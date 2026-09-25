# 2 SOLUÇÃO PROPOSTA


## 2.1 Objetivo Geral do Produto

O objetivo do produto é fortalecer a gestão do Centro Esportivo Cultural de Planaltina DF (CECP) por meio de um sistema de gestão de alunos e da instituição, substituindo o controle manual e descentralizado hoje utilizado pela instituição. A solução visa dar autonomia à coordenação, ampliar o alcance da instituição junto à comunidade e garantir transparência na prestação de contas a parceiros, apoiadores e órgãos de fiscalização, consolidando a capacidade organizacional da entidade. Do ponto de vista técnico, a solução será composta por uma única plataforma integrada, organizada em dois módulos que compartilham a mesma base de dados:

__Módulo público__: divulgação institucional e manifestação de interesse online (etapa que antecede a matrícula, a qual permanece presencial).
__Módulo administrativo__: cadastro e matrícula de alunos, turmas, frequência e situação pedagógica, medidas disciplinares, comunicação com voluntários e famílias, registro de doações e captação de recursos, e documentos de prestação de contas.

## 2.2 Objetivos Específicos (OE) do Produto

- **OE1:** Centralizar os dados dos alunos em uma base tecnológica única, eliminando o uso de documentos físicos e registros manuais dispersos e viabilizando a gestão digital do CECP.
- **OE2:** Garantir o acompanhamento pontual da assiduidade e das condicionalidades pedagógicas dos alunos, permitindo à coordenação identificar rapidamente casos críticos e intervir antes da perda da vaga.
- **OE3:** Apoiar a aplicação e o histórico de medidas disciplinares (advertências, suspensões e desligamentos), garantindo rastreabilidade das decisões tomadas pela coordenação.
- **OE4:** Facilitar a comunicação entre a coordenação do projeto, os voluntários e as famílias dos alunos, reduzindo a dependência de canais informais.
- **OE5:** Assegurar transparência na prestação de contas a parceiros, apoiadores e órgãos de fiscalização, dada a natureza de OSCIP da entidade.

### 2.2.1 Estratégia de Migração dos Dados Atuais

Dado que o cenário atual do CECP é predominantemente baseado em documentos físicos (ver seção 1), a migração dos registros existentes para o sistema não será automatizada: os dados hoje em fichas de papel e nos documentos já digitalizados serão inseridos/associados manualmente na plataforma pela equipe administrativa do CECP durante a fase de implantação, com apoio da equipe de desenvolvimento na definição do processo de carga inicial. Esses materiais existentes poderão ser usados como fonte de apoio para esse cadastro manual, mas não serão importados diretamente por não seguirem um formato padronizado.
## 2.3 Características de Produto (mapeadas com os Objetivos Específicos do Produto)

A solução proposta para o CECP deverá contemplar, de forma preliminar, as seguintes características:


| OE principal | Contribuição secundária | ID | Característica | Descrição resumida | Valor de negócio principal |
|---|---|---|---|---|---|
| OE2 | OE1, OE3 | CP1 | Gestão e acompanhamento de turmas | A solução deverá oferecer uma plataforma digital que permita a criação, gerenciamento e inativação das turmas, de modo que permita o gerenciamento digital igual ao atualmente utilizado de forma analógica sem ferir as regras de negócios. | Apoio à operação, melhoria na gestão das turmas e melhoria da experiência dos administradores. |
| OE5 | OE1 | CP2 | Registro de doações e prestação de contas | Capacidade de registrar as doações e os recursos recebidos pela instituição (bens, solicitações por ofício e repasses de parcerias), sem processamento de pagamento online nesta fase. | Maior controle e transparência sobre os recursos recebidos pela instituição. |
| OE4 | OE5 | CP3 | Gestão de conteúdo institucional | Capacidade de a coordenação publicar e manter atualizadas as informações institucionais da organização (atividades, eventos e resultados), substituindo a dependência do Instagram e de um site desatualizado como únicos canais de divulgação. | Aumento da visibilidade e transparência da organização perante a comunidade, doadores e avaliadores de editais. |
| OE1 | — | CP4 | Cadastro e histórico de alunos | Capacidade de manter o cadastro e o histórico dos alunos vinculados à instituição. | Centralização da informação e suporte a comprovações históricas. |
| OE2, OE3 | — | CP5 | Acompanhamento pedagógico e disciplinar do aluno | Capacidade de acompanhar a frequência e a situação pedagógica dos alunos e de registrar medidas disciplinares aplicadas. | Redução da evasão, apoio à tomada de decisão e rastreabilidade. |
| OE4 | — | CP6 | Comunicação com voluntários e famílias | Capacidade de comunicação entre a coordenação, os voluntários e as famílias dos alunos. | Comunicação mais organizada e rastreável. |
| OE1 | OE2 | CP7 | Matrícula online | A solução deverá oferecer um novo meio de matrículas para novos alunos no formato digital que não exija o comparecimento presencial do aluno, diminuindo as barreiras para a realização das matrículas. | Aumento da conversão de matrícula e diversificação de meios de matrícula. |

## 2.4 Tecnologias a Serem Utilizadas

As ferramentas que serão utilizadas diretamente para a construção da proposta para o CECP foram escolhidas de acordo com a necessidade do projeto. Para o frontend serão utilizados o HTML, CSS e JavaScript, que são amplamente conhecidos pela equipe e permitem a implementação de interfaces responsivas. No backend será utilizado o FastAPI, que permite um backend mínimo, mas eficiente para receber e processar as requisições e realizar a comunicação com o banco de dados. Para a persistência de dados será utilizado o MySQL, considerando as necessidades de armazenamento e gerenciamento de dados dos alunos e doações, e o SQLAlchemy, um ORM que facilita a comunicação entre a aplicação e o banco de dados.

Para o desenvolvimento do projeto, serão utilizados o Git e o GitHub para o controle de versão, compartilhamento e desenvolvimento do projeto, o GitHub Projects para a aplicação do framework de gestão baseado em Kanban. Para a documentação do projeto, serão utilizados o Word, que permite a escrita de documentos no formato .docx e .pdf, MkDocs e MkDocs Materials, que permitem o desenvolvimento de uma página web em Markdown. Também serão considerados mecanismos de segurança e privacidade dos dados para atender aos requisitos da LGPD e contribuir para a conformidade com a legislação, garantindo a qualidade, o alinhamento e o respeito à ética, que são pontos-chave para o desenvolvimento desse projeto.

## 2.5 Pesquisa de Mercado e Análise Competitiva

O mercado de soluções de gestão voltadas a projetos sociais e esportivos no Brasil é composto majoritariamente por sistemas genéricos de gestão escolar ou de academias, que não contemplam as particularidades de uma organização social sem fins lucrativos como o CECP. Entre as soluções existentes, destacam-se:

- **Sistemas de gestão para academias e escolinhas esportivas** (como Pacto Soluções, EVO ou Gestão Fit), voltados principalmente para controle financeiro, mensalidades e agenda de aulas funcionalidades pouco relevantes para uma entidade que não cobra mensalidade dos alunos e cujo foco central é o acompanhamento socioeducacional.
- **Sistemas de gestão escolar** (como o SIGE ou plataformas similares usadas por escolas particulares), que possuem módulos robustos de boletim e frequência, mas são voltados à gestão pedagógica formal de uma instituição de ensino, não a um projeto social que apenas monitora o desempenho do aluno em sua escola de origem.
- **Planilhas eletrônicas** (como Google Sheets ou Excel Online), amplamente utilizadas por organizações do porte do CECP por serem de fácil adoção, baixo custo e permitirem inclusive edição simultânea por múltiplos usuários, mas que não oferecem funcionalidades específicas do domínio da instituição, como alertas automáticos de frequência crítica, histórico estruturado de medidas disciplinares ou controle de acesso por perfil de usuário, dependendo de organização manual pela equipe.

A proposta se diferencia por ser uma solução enxuta e de baixo custo, desenhada especificamente para o modelo de funcionamento de projetos sociais esportivos: sem módulos financeiros ou pedagógicos complexos, mas com foco direto no vínculo entre frequência, desempenho escolar e permanência do aluno no projeto que é a regra de negócio central do CECP e não é atendida por nenhuma das soluções de mercado existentes de forma nativa. Adicionalmente, por ser desenvolvida sob medida, a solução tem custo de aquisição e manutenção compatível com a realidade orçamentária de uma OSCIP mantida por voluntariado.

Dessa forma, a proposta se posiciona como uma solução sob medida, enxuta e alinhada à realidade orçamentária e operacional de uma organização esportiva, algo que nenhuma solução genérica de mercado atende de forma nativa.

## 2.6 Viabilidade da Proposta

A proposta é viável no contexto da disciplina, considerando o acesso ao cliente, o escopo definido e a possibilidade de entrega incremental de um MVP funcional ao final do semestre. Embora a equipe ainda esteja em processo de consolidação do domínio sobre algumas tecnologias e integrações, o projeto foi estruturado de forma compatível com essa realidade, com sprints de no máximo uma semana a depender da complexidade das entregas, priorização das funcionalidades essenciais e validações frequentes com a cliente.
 
O principal risco técnico está no gerenciamento de dados, uma vez que a transição de processos hoje registrados em papel para um sistema digital exige modelagem cuidadosa das entidades (alunos, matrículas, turmas, frequência, medidas disciplinares e documentos de doações/prestação de contas), além de mecanismos que garantam integridade e consistência das informações migradas. Esse risco é mitigado por meio da definição incremental do modelo de dados junto à cliente, reduzindo a probabilidade de inconsistências propagarem-se para as demais funcionalidades do sistema.
 
Assim, a proposta é considerada viável, desde que:
 
- O escopo do MVP permaneça controlado;
- As prioridades sejam mantidas; e
- A equipe preserve a estratégia de aprendizado contínuo ao longo do desenvolvimento.

## 2.7 Benefícios Esperados

- **Para o Cliente:** Maior controle e facilidade de acesso às fichas, ao histórico e às doações dos alunos, com acompanhamento consolidado de frequência, situação pedagógica e medidas disciplinares, reduzindo a dependência de fichas de papel e facilitando o gerenciamento dos dados e das turmas.
- **Para o candidato a aluno (Usuário):** Outra opção de manifestar interesse em participar do CECP de forma remota, removendo a necessidade de comparecer presencialmente para dar o primeiro passo (a matrícula em si permanece presencial).
- **Para os voluntários e famílias (Usuário):** Um canal de comunicação mais direto com a coordenação, reduzindo a dependência de canais informais.
- **Para os avaliadores do edital (Usuário):** Uma interface e disposição dos dados e documentos de prestação de contas necessários para a avaliação de acordo com as normas dos editais.
- **Para a coordenação, em relação às doações:** Um novo meio de registrar e acompanhar os itens e recursos recebidos, permitindo maior controle e transparência.
## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.1 | 18/09/2026 | Ajustando conforme o feedback da issue: Unidade 1 - Solução proposta #14| [Marcos Monteiro](https://github.com/montmarcos) |  |