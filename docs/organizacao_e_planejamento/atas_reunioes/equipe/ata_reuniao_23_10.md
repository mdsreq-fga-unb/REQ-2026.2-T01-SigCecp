# Ata de Reunião - Evidências de Engenharia de Requisitos, Revisão do MVP e Replanejamento

## 1. Identificação da reunião

**Projeto:** Sistema de Gestão do Centro Esportivo Cultural de Planaltina (SigCECP) **Data:** 23/10/2026 **Modalidade:** Remota (chamada de vídeo gravada, cerca de 34 minutos)  
**Participantes:** Ana Paula, Rafael, Alexandre, Maria Eduarda, Júlia, Marcos  
**Pauta:** Atendimento à issue 26 do professor, centralização dos requisitos, registro das evidências de engenharia de requisitos, revisão das estimativas de esforço e complexidade, redefinição do MVP, atualização da documentação e do cronograma, e organização das atividades da equipe.

## 2. Centralização dos requisitos

O professor apontou, na issue 26, requisitos duplicados em diferentes partes do repositório, o que gera inconsistências quando uma cópia é atualizada e as outras não. Ficou decidido manter os requisitos estruturados na seção de requisitos do documento original. A seção antes chamada de backlog passa a se chamar **escopo**, com links para os requisitos e indicação dos que fazem parte do MVP. O mesmo princípio vale para as demais evidências: quando a informação já estiver registrada em outro local, será usada uma referência em vez de repetir o conteúdo.

## 3. Redefinição do MVP

Após a reunião de priorização com a técnica MoSCoW, o MVP foi apresentado ao cliente, mas isso ainda não equivale à aprovação formal, também cobrada pelo professor. O feedback apontou ainda um desalinhamento entre os objetivos do produto (assiduidade, comunicação e prestação de contas) e as funcionalidades previstas no MVP. A equipe definiu um escopo mais enxuto, priorizando:

- **Módulo público**
- **Gestão de alunos**
- **Gestão de turmas**

Funcionalidades complexas ou não essenciais, como frequências, alertas e doações, foram consideradas para exclusão. O gráfico de requisitos será removido da documentação, pois seu custo de manutenção superava o benefício, e as mudanças de escopo serão justificadas formalmente (restrições de tempo, capacidade da equipe e alinhamento entre objetivos e MVP).

## 4. Revisão das estimativas de esforço e complexidade

O feedback indicou que requisitos de persistência de dados, validação, segurança, testes e integração receberam estimativas baixas, pois a equipe considerou principalmente o esforço de programação. A planilha usa a **moda** das respostas e, em caso de empate, o **menor valor** (por exemplo, com as respostas 1, 1, 1, 2, 2, 2 e 3, a moda é 1). Marcos prefere desempatar pelo maior valor ou usar a média, e Ana Paula defende incluir critérios além de esforço e complexidade de programação. Ganhou força a proposta de refazer o formulário de estimativas, considerando a capacidade real da equipe em uma sprint de uma semana, e de explicitar o critério de desempate no relatório.

## 5. Registro das evidências e página de acompanhamento

A equipe reconheceu que várias técnicas de engenharia de requisitos foram usadas sem evidência formal no repositório: o brainstorming entre desenvolvedores (reunião no Discord sem gravação), o levantamento de novos requisitos, os critérios de aceitação (ficaram em mensagens de WhatsApp), a revisão por pares e a prototipação. A partir de agora, reuniões e atividades serão registradas por gravação, áudio, foto ou ata, com links no repositório.

Ana Paula propôs uma página centralizada de acompanhamento e Rafael sugeriu o formato de **log**, com data e horário, descrição da atividade, participantes e links para as evidências. Para o versionamento pedido pelo professor, os registros devem ser simples e usar referências sempre que possível.

## 6. Seção 7, prototipação e planejamento

A seção 7, que descreve o papel do analista de requisitos, não reflete a prática da equipe (por exemplo, reuniões presenciais que não ocorreram). Houve consenso em retirar ou generalizar as citações nominais, pois a engenharia de requisitos é responsabilidade de todos. Como proposta, Ana Paula prepara as reuniões e Marcos as conduz.

Quanto ao planejamento, a prototipação no Figma será centralizada em uma única pessoa. O cronograma será ajustado depois do detalhamento dos requisitos do MVP, e o planejamento semanal será feito aos domingos ou segundas, distribuindo tarefas conforme a disponibilidade de cada integrante, com prazos para integrar as entregas.

## 7. Decisões

- **Requisitos centralizados:** manter os requisitos na seção original e substituir cópias por links; a seção de escopo indica os requisitos do MVP (seção 2).
- **MVP enxuto:** priorizar módulo público, gestão de alunos e gestão de turmas, remover o gráfico de requisitos e justificar as mudanças de escopo (seção 3).
- **Registro de evidências:** gravar ou registrar as atividades de engenharia de requisitos e disponibilizá-las no repositório (seção 5).
- **Seção 7:** retirar ou generalizar as atribuições nominais do analista de requisitos (seção 6).
- **Cronograma:** ajustar após o detalhamento dos requisitos do MVP (seção 6).

## 8. Próximas etapas e pendências

- **Marcos:** conferir o escopo atualizado do MVP com o cliente e verificar a aprovação formal.
- **Marcos:** refazer o formulário de estimativas considerando a complexidade real e a capacidade da equipe, e remover o gráfico de requisitos.
- **Marcos:** consolidar o escopo do MVP (módulo público, alunos e turmas).
- **Ana Paula:** elaborar em Markdown o rascunho da página de acompanhamento (log) antes da próxima entrega.
- **Ana Paula:** revisar a seção 7 e organizar a centralização da prototipação em uma única pessoa.
- **Todo o grupo:** revisar os objetivos do projeto para ficarem coerentes com o MVP, ajustar o cronograma e organizar o planejamento semanal.
- **Pendente:** definir o critério final de desempate da moda (menor valor, maior valor ou média).