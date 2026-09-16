# 4. Estratégias de Engenharia de Software

## 4.1. Estratégia Priorizada

- **Abordagem:** Híbrida
- **Ciclo de Vida:** Iterativo e Incremental
- **Processo:** RAD
- **Framework de gestão de trabalho:** Kanban, aplicado por meio do GitHub Projects

### Por que a abordagem híbrida

A equipe adota uma abordagem híbrida porque o projeto exige as duas orientações ao mesmo tempo. De um lado, o contato com a coordenação do CECP é esporádico e os requisitos ainda estão emergindo, o que pede ciclos curtos, prototipagem e adaptação. De outro, o sistema tratará dados pessoais de menores de idade, o que exige disciplina documental: requisitos declarados, critérios de aceitação verificáveis e rastreabilidade das decisões. Uma abordagem puramente ágil deixaria a segunda exigência descoberta, e uma abordagem dirigida por plano consumiria o semestre em especificação antes de qualquer validação com o cliente.

O RAD foi escolhido como processo justamente por ser classificado como processo híbrido/adaptativo, combinando fases definidas com prototipagem e envolvimento intenso do usuário.

## 4.2. Quadro Comparativo

A fim de fundamentar a escolha do processo de desenvolvimento, o quadro a seguir compara o RAD e o OpenUP a partir de características relevantes para o contexto do projeto.

| Características | OpenUP | RAD |
| --- | --- | --- |
| **Classificação** | Processo abrangente, na forma de versão simplificada e leve do Unified Process, que equilibra disciplina e agilidade mantendo natureza iterativa e incremental. | Processo híbrido/adaptativo, com ênfase em prototipagem rápida e iterativa como alternativa ao planejamento extensivo. |
| **Fases do Processo** | Concepção, Elaboração, Construção e Transição, com ênfase em arquitetura nas fases iniciais. | Planejamento de Requisitos, Design do Usuário, Construção e Cutover (implantação final). |
| **Tratamento de Requisitos** | Requisitos capturados por casos de uso leves ou histórias de usuário desde a Concepção, refinados progressivamente, priorizando itens de maior risco ou valor. | Requisitos de alto nível no planejamento, com o detalhamento emergindo durante a prototipagem. Os protótipos servem simultaneamente de especificação e validação. |
| **Papel do Cliente** | Colaboração próxima e regular com stakeholders ao longo de todas as iterações, por meio de revisões e demonstrações. | Colaboração intensa e concentrada nos workshops de Design do Usuário, com feedback imediato sobre protótipos funcionais. |
| **Documentação** | Enxuta, porém estruturada: Visão, Lista de Requisitos e Modelo de Casos de Uso simplificado. | Mínima, focada em interface, fluxos de dados e modelos de banco de dados, produzida apenas quando necessária. |
| **Velocidade de Entrega** | Ciclos de feedback rápidos, com investimento inicial maior em arquitetura e estruturação das fases. | Prioridade máxima. Indicado para projetos com prazos muito curtos, com visualização precoce do sistema por meio de protótipos. |
| **Cenários Adequados** | Equipes pequenas e co-localizadas, sistemas não críticos, organizações migrando gradualmente do tradicional para o ágil. | Prazos curtos, escopo modularizável, ênfase em interface do usuário e requisitos difíceis de articular verbalmente, porém fáceis de visualizar. |
| **Limitações** | Menos orientação para equipes inexperientes e possível insuficiência para sistemas de grande escala. | Menor adequação a sistemas de missão crítica, risco de negligenciar requisitos não funcionais e necessidade de comprometimento dos usuários nas validações. |
| **Adaptação ao Projeto do CECP** | Viável. A estruturação por casos de uso desde a Concepção daria tratamento mais natural às regras de negócio e aos requisitos não funcionais, mas exige disponibilidade regular do cliente em todas as iterações, o que não corresponde à rotina de uma coordenação voluntária com reuniões esporádicas. | Adequado ao contexto, desde que adaptado. O protótipo é o artefato que a coordenação consegue avaliar sem intermediação técnica, e o escopo é modular. As limitações do processo quanto a requisitos não funcionais e regras de negócio exigem complementos explícitos, descritos na seção 4.3. |

## 4.3. Justificativa

Com base nas características do projeto e no contexto do CECP, o RAD é o processo mais adequado pelos seguintes motivos:

**Requisitos difíceis de articular e escopo modularizável**

O levantamento junto à coordenação do CECP identificou com clareza o núcleo do problema, que envolve o cadastro de alunos, o acompanhamento de frequência e desempenho escolar, o registro de medidas disciplinares e o controle de doações. As decisões detalhadas sobre cada um desses módulos, porém, continuam em aberto, e a coordenação descreve sua rotina em termos de prática cotidiana, não em termos de requisito. Esse é precisamente o cenário que o RAD atende, no qual os requisitos são difíceis de articular verbalmente mas fáceis de reconhecer quando visualizados. O escopo também se organiza em módulos bem delimitados, o que permite construção incremental.

**Prototipação como núcleo do processo e da Engenharia de Requisitos**

A equipe definiu, nas atividades de Engenharia de Requisitos da seção 5, o uso de wireframes e protótipos como técnica de representação e validação. No RAD os protótipos funcionam simultaneamente como especificação e validação, evoluindo até o sistema final, o que garante alinhamento direto entre o processo de desenvolvimento e as técnicas de ER adotadas.

A equipe reconhece, entretanto, que o protótipo não é um artefato suficiente. Ele representa interface e fluxo, mas não expressa regra de negócio, critério de aceitação, requisito não funcional, decisão de modelagem de dados ou exigência de segurança e privacidade. Por esse motivo o processo é adotado com os complementos declarados ao final desta seção.

**Forma de participação compatível com o cliente**

A colaboração no RAD concentra-se nos momentos de design e validação de protótipos, com feedback imediato sobre versões funcionais. Esse formato é compatível com a dinâmica de contato do CECP, feita por reuniões periódicas de videoconferência e canais de mensagens, e permite que a coordenação voluntária participe de forma efetiva em momentos-chave, sem exigir acompanhamento diário do desenvolvimento.

**Prazo da disciplina e entrega de MVP**

O RAD é indicado para projetos com prazos muito curtos, nos quais a velocidade de entrega é prioritária. Com um semestre para entregar um MVP funcional, a ênfase do processo em prototipagem rápida e construção acelerada favorece a entrega de valor dentro do prazo.

**Natureza do sistema compatível com as limitações do processo**

Para mitigar o risco de negligência aos requisitos não funcionais, a equipe manterá sua declaração e verificação explícitas nas atividades de Engenharia de Requisitos.

### Adaptações do RAD ao contexto do projeto

O RAD apoia a especificação no protótipo, que representa interface e fluxo, mas não expressa alguns tipos de requisito. O quadro abaixo declara qual artefato cobre cada um deles.

| Aspecto não coberto pelo protótipo | Artefato complementar |
| --- | --- |
| Regras de negócio | Declaração textual da regra, vinculada à issue do requisito |
| Requisitos não funcionais | Lista numerada de RNF, conforme a seção 5 |
| Critérios de aceitação | Critérios verificáveis associados a cada requisito funcional |
| Decisões sobre dados | Modelo de dados versionado, refinado a cada iteração de Design |
| Segurança, privacidade e LGPD | RNF específicos derivados da característica CP5 |

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.1 | 06/09/2026 | Substituição do Scrum pelo OpenUP no quadro comparativo e revisão da justificativa da escolha do RAD | [Enzo Costa](https://github.com/enzocostaj) | 
| 1.2 | 15/09/2026 | Adequação ao feedback do professor: inclusão do Kanban como framework de gestão, justificativa da abordagem híbrida, revisão da criticidade do sistema e inclusão do quadro de adaptações do processo. | [Enzo Costa](https://github.com/enzocostaj) |