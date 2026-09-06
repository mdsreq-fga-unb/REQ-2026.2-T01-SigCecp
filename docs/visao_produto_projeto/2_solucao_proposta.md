# 2 SOLUÇÃO PROPOSTA

## 2.1 Objetivo Geral do Produto

O objetivo do produto é fortalecer a gestão do Centro Esportivo Cultural de Planaltina DF (CECP) por meio de um sistema integrado de gestão de alunos e da instituição, substituindo o controle manual e descentralizado hoje utilizado pela instituição. A solução visa dar autonomia à coordenação, ampliar o alcance da instituição junto à comunidade e garantir transparência na prestação de contas a parceiros, apoiadores e órgãos de fiscalização, consolidando a capacidade organizacional da entidade.

## 2.2 Objetivos Específicos (OE) do Produto

- **OE1:** Centralizar os dados dos alunos em uma base tecnológica única, eliminando o uso de planilhas e registros manuais dispersos e viabilizando a gestão digital do CECP.
- **OE2:** Garantir o acompanhamento pontual da assiduidade e das condicionalidades pedagógicas dos alunos, permitindo à coordenação identificar rapidamente casos críticos e intervir antes da perda da vaga.
- **OE3:** Apoiar a aplicação e o histórico de medidas disciplinares (advertências, suspensões e desligamentos), garantindo rastreabilidade das decisões tomadas pela coordenação.
- **OE4:** Facilitar a comunicação entre a coordenação do projeto, os voluntários e as famílias dos alunos, reduzindo a dependência de canais informais.
- **OE5:** Assegurar transparência na prestação de contas a parceiros, apoiadores e órgãos de fiscalização, dada a natureza de OSCIP da entidade.

## 2.3 Características de Produto (mapeadas com os Objetivos Específicos do Produto)

A solução proposta para o CECP deverá contemplar, de forma preliminar, as seguintes características:

| OE principal | Contribuição secundária | ID | Característica | Descrição resumida | Valor de negócio principal |
|---|---|---|---|---|---|
| OE2 | OE1, OE3 | CP1 | Gestão e acompanhamento de turmas | A solução deverá oferecer uma plataforma digital que permita a criação, gerenciamento e exclusão das turmas, de modo que permita o gerenciamento digital igual ao atualmente utilizado de forma analógica sem ferir as regras de negócios. | Apoio à operação, melhoria na gestão das turmas e melhoria da experiência dos administradores. |
| OE1 | OE2 | CP2 | Formulário de matrícula online | A solução deverá oferecer um novo meio de matrículas para novos alunos no formato digital que não exija o comparecimento presencial do aluno, diminuindo as barreiras para a realização das matrículas. | Aumento da conversão de matrícula e diversificação de meios de matrícula. |
| OE5 | OE1 | CP3 | Canal online para doações | A solução deverá apoiar a realização do controle, atração e transparência das doações, de modo a tornar o processo mais simples e eficiente para os clientes e administradores. | Melhoria da experiência das doações, aumento de conversão e melhoria na gestão das doações recebidas e a serem recebidas. |
| OE4 | OE5 | CP4 | Canal online de divulgação digital | A solução deverá disponibilizar um canal de divulgação oficial dos eventos e acontecimentos da organização, a fim de melhorar a transparência, atrair novos alunos, doadores e atender aos requisitos de editais públicos. | Aumento da visibilidade e transparência da organização pelos doadores e alunos. |
| OE1 | OE5 | CP5 | Segurança, privacidade e conformidade | A solução deverá incorporar mecanismos e decisões de produto voltados à segurança, à privacidade e à conformidade com a LGPD, protegendo dados, transações e a operação digital do CECP. | Redução de riscos, fortalecimento da confiança na organização e sustentação do crescimento digital. |

## 2.4 Tecnologias a Serem Utilizadas

As ferramentas que serão utilizadas diretamente para a construção da proposta para o CECP foram escolhidas de acordo com a necessidade do projeto. Para o frontend serão utilizados o HTML, CSS e JavaScript, que são amplamente conhecidos pela equipe e permitem a implementação de interfaces responsivas. No backend será utilizado o FastAPI, que permite um backend mínimo, mas eficiente para receber e processar as requisições e realizar a comunicação com o banco de dados. Para a persistência de dados será utilizado o MySQL, considerando as necessidades de armazenamento e gerenciamento de dados dos alunos e doações, e o SQLAlchemy, um ORM que facilita a comunicação entre a aplicação e o banco de dados.

Para o desenvolvimento do projeto, serão utilizados o Git e o GitHub para o controle de versão, compartilhamento e desenvolvimento do projeto, o GitHub Projects para a aplicação do framework de gestão baseado em Kanban. Para a documentação do projeto, serão utilizados o Word, que permite a escrita de documentos no formato .docx e .pdf, MkDocs e MkDocs Materials, que permitem o desenvolvimento de uma página web em Markdown. Também serão considerados mecanismos de segurança e privacidade dos dados para atender aos requisitos da LGPD e contribuir para a conformidade com a legislação, garantindo a qualidade, o alinhamento e o respeito à ética, que são pontos-chave para o desenvolvimento desse projeto.

## 2.5 Pesquisa de Mercado e Análise Competitiva

O mercado de soluções de gestão voltadas a projetos sociais e esportivos no Brasil é composto majoritariamente por sistemas genéricos de gestão escolar ou de academias, que não contemplam as particularidades de uma organização social sem fins lucrativos como o CECP. Entre as soluções existentes, destacam-se:

- **Sistemas de gestão para academias e escolinhas esportivas** (como Pacto Soluções, EVO ou Gestão Fit), voltados principalmente para controle financeiro, mensalidades e agenda de aulas — funcionalidades pouco relevantes para uma entidade que não cobra mensalidade dos alunos e cujo foco central é o acompanhamento socioeducacional.
- **Sistemas de gestão escolar** (como o SIGE ou plataformas similares usadas por escolas particulares), que possuem módulos robustos de boletim e frequência, mas são voltados à gestão pedagógica formal de uma instituição de ensino, não a um projeto social que apenas monitora o desempenho do aluno em sua escola de origem.
- **Planilhas eletrônicas e formulários avulsos**, atualmente utilizados por organizações do porte do CECP, que resolvem parcialmente o problema, mas não oferecem histórico consolidado, alertas automáticos ou acesso simultâneo por múltiplos voluntários.

A proposta se diferencia por ser uma solução enxuta e de baixo custo, desenhada especificamente para o modelo de funcionamento de projetos sociais esportivos: sem módulos financeiros ou pedagógicos complexos, mas com foco direto no vínculo entre frequência, desempenho escolar e permanência do aluno no projeto — que é a regra de negócio central do CECP e não é atendida por nenhuma das soluções de mercado existentes de forma nativa. Adicionalmente, por ser desenvolvida sob medida, a solução tem custo de aquisição e manutenção compatível com a realidade orçamentária de uma OSCIP mantida por voluntariado.

Dessa forma, a proposta se posiciona como uma solução sob medida, enxuta e alinhada à realidade orçamentária e operacional de uma organização esportiva, algo que nenhuma solução genérica de mercado atende de forma nativa.

## 2.6 Viabilidade da Proposta

A proposta é viável no contexto da disciplina, considerando o acesso ao cliente, o escopo definido e a possibilidade de entrega incremental de um MVP funcional ao final do semestre. Embora a equipe ainda esteja em processo de consolidação do domínio sobre algumas tecnologias e integrações, o projeto foi estruturado de forma compatível com essa realidade, com sprints de no máximo uma semana a depender da complexidade das entregas, priorização das funcionalidades essenciais e validações frequentes com a cliente.

O principal risco técnico está no gerenciamento de dados, uma vez que a transição de processos hoje registrados em papel para um sistema digital exige modelagem cuidadosa das entidades (alunos, matrículas, mensalidades, turmas e frequência), além de mecanismos que garantam integridade e consistência das informações migradas. Esse risco é mitigado por meio da definição incremental do modelo de dados junto à cliente, reduzindo a probabilidade de inconsistências propagarem-se para as demais funcionalidades do sistema.

Assim, a proposta é considerada viável, desde que:

- O escopo do MVP permaneça controlado;
- As prioridades sejam mantidas; e
- A equipe preserve a estratégia de aprendizado contínuo ao longo do desenvolvimento.

## 2.7 Benefícios Esperados

- **Para o Cliente:** Maior controle e facilidade de acesso às fichas de inscrição dos alunos e das doações, permitindo um armazenamento de dados mais compacto por não necessitar de diversas fichas de papel e facilitando o gerenciamento dos dados e das turmas.
- **Para o Aluno que vai se matricular (Usuário):** Outra opção de fazer matrícula nas turmas, removendo a necessidade de ir presencialmente ao estabelecimento para fazer a matrícula.
- **Para os avaliadores do edital (Usuário):** Uma interface e disposição dos dados necessários para a avaliação de acordo com as normas dos editais.
- **Para quem irá realizar uma doação (Usuário):** Um novo meio de registrar os itens que serão doados, permitindo uma comunicação facilitada.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) |  |