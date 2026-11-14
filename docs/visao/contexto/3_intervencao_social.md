# 3. Intervenção Social

A plataforma web de gestão do CECP tende a produzir uma intervenção social voltada à digitalização do acompanhamento socioeducacional de crianças, jovens e adultos, à reorganização do trabalho e ao fortalecimento da capacidade institucional de uma OSCIP que hoje opera de forma manual e descentralizada.

Os impactos abaixo pertencem à visão de evolução do produto, com a distinção entre MVP e pós-MVP da [seção 2.7](2_solucao_proposta.md#27-beneficios-esperados). O acompanhamento de desempenho escolar e seus eventuais alertas dependem da definição funcional indicada em [2.3.2](2_solucao_proposta.md#232-limite-do-acompanhamento-escolar), sem automação especificada nos RFs atuais.

Entre os __impactos pretendidos__, destacam-se:

- Tornar mais ágil e confiável o acompanhamento da condicionalidade pedagógica que sustenta a permanência do aluno no projeto (frequência e desempenho escolar);
- Reduzir a dependência de fichas em papel e documentos físicos, diminuindo o risco de perda de informações sobre alunos, turmas e doações;
- Dar visibilidade rápida a casos de baixa assiduidade ou queda de rendimento escolar, permitindo intervenção pedagógica mais oportuna por parte da coordenação;
- Garantir rastreabilidade nas medidas disciplinares aplicadas, tornando as decisões da coordenação mais transparentes e consistentes;
- Facilitar a comunicação entre coordenação, voluntários e famílias, reduzindo a dependência de canais informais;
- Fortalecer a presença institucional digital do CECP, ampliando sua capacidade de atender requisitos de editais públicos e de prestar contas a parceiros e apoiadores;
- Organizar o registro de doações, tornando a captação de recursos menos dependente de contatos informais.

Ao mesmo tempo, a solução pode gerar __efeitos emergentes__, não totalmente previstos, que precisam ser observados, como:

- Resistência ou sobrecarga inicial da equipe voluntária diante de uma ferramenta digital, mesmo sendo simples, em um contexto de perfis técnicos variados e alta rotatividade de voluntários;
- Risco de exclusão ou de tratamento desigual de famílias com menor familiaridade tecnológica ou acesso limitado à internet, especialmente em uma comunidade de baixa renda;
- Possível uso da centralização de dados sensíveis (desempenho escolar, medidas disciplinares, dados de menores de idade) de forma a reforçar estigmas ou rótulos sobre alunos, caso as informações não sejam manuseadas com cuidado;
- Dependência crescente do CECP em relação à própria plataforma e a quem souber operá-la, criando um tipo de fragilidade institucional (de "dependência de papel" para "dependência de sistema e de conhecimento técnico");
- Necessidade de atenção redobrada à proteção de dados pessoais de crianças e adolescentes, dado o caráter sensível das informações escolares e disciplinares armazenadas;
- Possível uso da automação de alertas (ex.: queda de rendimento) de forma mecânica, sem a mediação humana e o cuidado pedagógico que o projeto hoje pratica informalmente.

Com a identificação desses efeitos emergentes, faz-se necessário identificar ações que possam mitigá-los ou eliminá-los. A seguir, apresenta-se uma tabela com os efeitos emergentes e as respectivas ações para mitigá-los ou eliminá-los.

|Efeito emergente| Ação|
|      :----     |:----|
|Resistência ou sobrecarga incial da equipe voluntária | Desenvolver uma interface simples e intuitiva, acompanhada de uma documentação básica de uso, reduzindo a necessidade de conhecimento técnico para utilizar a plataforma. |
|Risco de exclusão ou de tratamento desigual de famílias | Manter canais de atendimento presenciais e alternativas não digitais, garantindo que o acesso aos serviços do CECP não dependa exclusivamente da plataforma. |
|Possível uso da centralização de dados sensíveis de forma a reforçar estigmas ou rótulos sobre alunos| Evitar a exposição desnecessária de informações sensíveis na plataforma, aplicando os princípios de finalidade, adequação e necessidade previstos no **art. 6º da Lei Geral de Proteção de Dados (LGPD)** e observando as hipóteses para o tratamento de dados pessoais sensíveis estabelecidas no **art. 11 da LGPD**, restringindo o acesso às informações aos usuários que realmente necessitem delas. |
|Dependência crescente do CECP em relação à própria plataforma e a quem souber operá-la | Evitar que processos essenciais dependam exclusivamente da plataforma, mantendo procedimentos alternativos para as atividades críticas e permitindo a continuidade do trabalho mesmo em caso de indisponibilidade do sistema. |
|Necessidade de atenção redobrada à proteção de dados pessoais de crianças e adolescentes | Aplicar as medidas previstas na **Lei Geral de Proteção de Dados (LGPD), especialmente os requisitos dos arts. 14 e 46**, que tratam do tratamento de dados pessoais de crianças e adolescentes e da adoção de medidas de segurança para proteção dos dados pessoais, respectivamente. |
|Possível uso da automação de alertas de forma mecânica, sem a mediação humana e o cuidado pedagógico | Utilizar os alertas apenas como mecanismos de apoio à equipe, exigindo análise e acompanhamento humano antes de qualquer decisão ou intervenção relacionada ao aluno. |

Assim, a intervenção social da solução não é apenas "digitalizar fichas de papel". Ela consiste em alterar a forma como a coordenação identifica e acompanha situações de risco escolar e social, como as decisões disciplinares são registradas e justificadas, como a instituição se comunica com as famílias e como ela se apresenta a financiadores e ao poder público exigindo que os requisitos do sistema considerem tanto os benefícios esperados para o acompanhamento socioeducacional quanto os riscos de exclusão digital.

## Referências legais e aplicação no projeto

A fundamentação legal das medidas acima é a [Lei nº 13.709/2018 (LGPD), texto oficial](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html):

| Referência | Implicação já considerada para a solução |
|---|---|
| Art. 6º, especialmente incisos I, II e III | Finalidade, adequação e necessidade orientam a limitação dos dados e da exposição de informações dos participantes. |
| Art. 11 | As hipóteses aplicáveis ao tratamento de dados pessoais sensíveis devem ser observadas; esta página não define uma nova hipótese de tratamento. |
| Art. 14 | O tratamento de dados de crianças e adolescentes exige atenção ao melhor interesse e às condições previstas no artigo. |
| Art. 46, caput e § 2º | Medidas técnicas e administrativas de proteção devem ser consideradas desde a concepção até a execução da solução. |

As medidas de acesso e proteção são especificadas nos [RNFs](../../painel.md#RNF13), especialmente RNF11 e RNF13. As decisões sobre quais informações escolares registrar permanecem na [PEN11](../../painel.md#PEN11); a revisão desta página não autoriza novas coletas nem define critérios escolares.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.1 | 10/09/2026 | Ajustando de acordo com os feedback da issue: [Unidade 1 - Intervenção social #15](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/issues/15) | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.2 | 14/11/2026 | Issues #24 e #35: transcrições legais substituídas por referências e implicações existentes; impactos sujeitos aos limites de cobertura e entrega | Renato Gameiro | Pendente |
