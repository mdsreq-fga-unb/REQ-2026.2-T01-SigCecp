# 4. Estratégias de Engenharia de Software

## 4.1. Estratégia Priorizada

- **Abordagem:** Híbrida
- **Ciclo de Vida:** Iterativo e Incremental
- **Processo:** RAD

## 4.2. Quadro Comparativo

A fim de fundamentar a escolha do processo de desenvolvimento, o quadro a seguir compara o RAD e o OpenUP a partir de características relevantes para o contexto do projeto.

| Características | OpenUP | RAD |
| --- | --- | --- |
| **Abordagem Geral** | Versão simplificada e leve do Unified Process, que equilibra disciplina e agilidade, mantendo natureza iterativa e incremental. | Processo híbrido/adaptativo com ênfase em prototipagem rápida e iterativa como alternativa ao planejamento extensivo. |
| **Fases do Processo** | Concepção, Elaboração, Construção e Transição, com ênfase em arquitetura nas fases iniciais. | Planejamento de Requisitos, Design do Usuário, Construção e Cutover (implantação final). |
| **Tratamento de Requisitos** | Requisitos capturados por casos de uso leves ou histórias de usuário, refinados progressivamente, priorizando itens de maior risco ou valor. | Requisitos de alto nível no planejamento; o detalhamento emerge durante a prototipagem, com os protótipos servindo simultaneamente de especificação e validação. |
| **Papel do Cliente** | Colaboração próxima e regular com stakeholders ao longo de todas as iterações, por meio de revisões e demonstrações. | Colaboração intensa e concentrada nos workshops de Design do Usuário, com feedback imediato sobre protótipos funcionais. |
| **Documentação** | Enxuta, porém estruturada: Visão, Lista de Requisitos e Modelo de Casos de Uso simplificado. | Mínima, focada em interface, fluxos de dados e modelos de banco de dados, produzida apenas quando necessária. |
| **Velocidade de Entrega** | Ciclos de feedback rápidos, mas com investimento inicial maior em arquitetura e estruturação das fases. | Prioridade máxima: indicado para projetos com prazos muito curtos, com visualização precoce do sistema por meio de protótipos. |
| **Cenários Adequados** | Equipes pequenas e co-localizadas, sistemas não críticos, organizações migrando gradualmente do tradicional para o ágil. | Prazos curtos, requisitos bem definidos (mas sujeitos a ajustes), escopo modularizável e ênfase em interface do usuário. |
| **Limitações** | Menos orientação para equipes inexperientes; pode ser insuficiente para sistemas de grande escala. | Menor adequação a sistemas de missão crítica; risco de negligenciar requisitos não funcionais; exige comprometimento dos usuários nas validações. |
| **Adaptação ao Projeto do CECP** | Viável, porém o investimento em arquitetura e estruturação de fases consome parte do semestre sem gerar as validações visuais rápidas de que a coordenação voluntária precisa. | Ideal para o contexto: requisitos centrais já mapeados, validação por protótipos/wireframes prevista na ER, escopo modular (alunos, frequência, boletins, doações) e prazo de um semestre para entrega de um MVP funcional. |

## 4.3. Justificativa

Com base nas características do projeto e no contexto do CECP, o RAD é o processo mais adequado pelos seguintes motivos:

**Requisitos centrais conhecidos e escopo enxuto**

O levantamento realizado junto à coordenação do CECP já permitiu identificar com clareza o núcleo do problema (cadastro de alunos, frequência, acompanhamento escolar e registro de doações), e essas funcionalidades formam módulos bem delimitados, exatamente o cenário adequado ao RAD: requisitos bem definidos, ainda que sujeitos a ajustes, em um escopo que permite modularização.

**Prototipação como núcleo do processo e da ER**

A equipe definiu, nas atividades de Engenharia de Requisitos, o uso de wireframes e protótipos como técnica de representação e validação de requisitos. No RAD, os protótipos funcionam simultaneamente como especificação e validação, evoluindo até o sistema final, o que garante alinhamento direto entre o processo de desenvolvimento e as técnicas de ER adotadas.

**Forma de participação compatível com o cliente**

A colaboração no RAD concentra-se nos momentos de design e validação de protótipos, com feedback imediato sobre versões funcionais. Esse formato é compatível com a dinâmica de contato do CECP, reuniões periódicas por videoconferência e canais de mensagens, permitindo que a coordenação voluntária participe de forma efetiva em momentos-chave, sem exigir acompanhamento diário do desenvolvimento.

**Prazo da disciplina e entrega de MVP**

O RAD é indicado para projetos com prazos muito curtos onde a velocidade de entrega é prioritária. Com um semestre para entregar um MVP funcional, a ênfase do processo em prototipagem rápida e construção acelerada favorece a entrega de valor dentro do prazo da disciplina.

**Natureza do sistema compatível com as limitações do processo**

As limitações do RAD concentram-se em sistemas de grande escala ou missão crítica, o que não corresponde à plataforma proposta, um sistema de gestão de pequeno porte, centrado em interface e fluxos de cadastro. Para mitigar o risco de negligência aos requisitos não funcionais, a equipe manterá sua declaração e verificação explícitas nas atividades de Engenharia de Requisitos.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.1 | 06/09/2026 | Substituição do Scrum pelo OpenUP no quadro comparativo e revisão da justificativa da escolha do RAD | [Enzo Costa](https://github.com/enzocostaj) | 