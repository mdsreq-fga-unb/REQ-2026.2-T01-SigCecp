# 7. Interação entre Equipe e Cliente

## 7.1 Composição da Equipe

| Papel | Descrição | Responsável | Participantes |
|---|---|---|---|
| Líder / Gerente de Projeto | Coordenação geral do projeto, alinhamento com o cliente, gestão de prazos e entregas | Rafael | Rafael |
| Desenvolvedor | Implementação das funcionalidades do sistema | Marcos | Alexandre, Ana, Enzo, Renato, Maria, Rafael, Marcos |
| Analista de QA | Garante a qualidade do produto, executando testes de funcionalidade e usabilidade | Renato | Rafael, Marcos, Maria, Renato |
| Analista de Requisitos | Facilita e registra o processo de descoberta, análise, negociação e validação dos requisitos junto às fontes relevantes | Ana | Alexandre, Enzo, Marcos, Renato, Maria, Rafael, Ana |

> **Nota:** A participação nas atividades de Engenharia de Requisitos é mandatória para todos os membros da equipe. O papel do Analista de Requisitos na prática está detalhado na seção "Atuação do Analista de Requisitos", abaixo.

### Atuação do Analista de Requisitos na Prática

Na prática, a facilitação conduzida por Ana ocorre da seguinte forma:

1. **Antes da reunião com o cliente:** Ana organiza a pauta com base nas dúvidas e pendências levantadas pela equipe durante a semana (registradas no grupo interno de WhatsApp e nas Issues do GitHub), definindo quais funcionalidades ou dúvidas precisam de validação com Pedro, Ivan ou Sandra.
2. **Durante a reunião:** Ana conduz a conversa fazendo perguntas abertas para captar necessidades reais (não apenas pedidos superficiais), registra as respostas em tempo real e, quando identifica ambiguidade (ex.: "o sistema deve avisar rápido sobre falta de frequência"), pergunta imediatamente por critérios concretos (quanto tempo, em que situação) antes de encerrar o ponto.
3. **Em caso de divergência entre a equipe técnica e o cliente:** Ana atua como intermediária, "traduzindo" a limitação técnica em linguagem acessível ao cliente e, na direção oposta, traduzindo a necessidade do cliente em termos que a equipe de desenvolvimento consiga implementar — sem tomar a decisão final sozinha, mas conduzindo a negociação até que as duas partes cheguem a um acordo viável.
4. **Depois da reunião:** Ana registra as decisões tomadas como uma Issue no GitHub (com a label `decision`) e atualiza a Ata resumida no site do projeto, garantindo que toda a equipe (mesmo quem não participou da reunião) tenha acesso ao que foi definido.

## 7.2 Comunicação

### Ferramentas de Comunicação

- **WhatsApp:** utilizado em dois grupos — um grupo com o cliente, para comunicações rápidas, dúvidas pontuais e confirmações de datas/atividades; e outro grupo com a equipe, para alinhamento interno do dia a dia.
- **Google Meet ou Teams:** utilizado para as reuniões semanais da equipe e para as reuniões com o cliente.
- **Discord:** utilizado eventualmente pela equipe para comunicação interna, com uso reduzido no momento por limitações na transmissão de tela.
- **GitHub Projects:** ferramenta de gerenciamento do backlog, controle de tarefas e acompanhamento do progresso do projeto.
- **GitHub Issues:** utilizado para o registro formal de decisões, aprovações, pendências e solicitações de mudança ao longo do projeto, com labels específicas para categorização (ex.: `decision`, `pending`, `change-request`).

### Disponibilidade do Cliente e Stakeholders

O representante do cliente, Pedro Augusto Cajado Coutinho, confirmou disponibilidade para reuniões via videoconferência nas **segundas, quartas e sextas-feiras, a partir das 17h**, com possibilidade de encontros adicionais aos finais de semana em caso de necessidade.

Ivan (professor de jiu-jitsu do CECP, também envolvido na administração do projeto) e Sandra (dona do projeto/responsável administrativa) confirmaram disponibilidade em **qualquer dia da semana, a partir das 20:30**, com preferência por encontros **presenciais**.

Com base nessa disponibilidade, a equipe adota a seguinte rotina real de reuniões:

- **Reunião de equipe (semanal):** toda semana, para alinhamento interno de progresso e prioridades.
- **Reunião com Pedro (semanal):** uma reunião por semana de desenvolvimento, dentro da janela seg/qua/sex 17h, para apresentar avanços e validar entregas em andamento.
- **Reunião presencial com Ivan e/ou Sandra (quando necessário):** agendada conforme a demanda de validação de funcionalidades ligadas à gestão de turmas (Ivan) ou às decisões administrativas/financeiras (Sandra), aproveitando a disponibilidade noturna presencial de ambos.
- **Validações assíncronas por WhatsApp:** usadas quando um ajuste é pequeno o suficiente para não exigir uma reunião completa (ex.: aprovação de um texto de tela, confirmação de uma regra pontual), evitando sobrecarregar a agenda do cliente com reuniões desnecessárias.

Essa rotina foi desenhada para caber dentro do ritmo real de trabalho da equipe (reuniões internas semanais) sem exigir mais disponibilidade do cliente do que ele já confirmou.

### Registro de Decisões, Aprovações e Mudanças

Todas as decisões, aprovações, pendências e solicitações de mudança são registradas em:

- **Issues do GitHub**, categorizadas por labels específicas;
- **Ata resumida das reuniões** com o cliente, publicada no site do projeto (GitHub Pages), contendo decisões tomadas e pendências em aberto.

## 7.3 Processo de Validação

O processo de validação segue a lógica do processo RAD, ocorrendo em múltiplos momentos ao longo do desenvolvimento. Para tornar isso concreto, usamos como exemplo a funcionalidade de **matrícula online (CP2)**:

1. **Elicitação e Análise:** durante a reunião semanal com Pedro, Ana levanta os campos obrigatórios da ficha de matrícula (hoje em papel) e as regras de validação (ex.: idade mínima), registrando tudo como rascunho de requisito na Issue correspondente.

2. **Definition of Ready (DoR) — aplicação prática:** antes de Marcos começar a implementar a tela de matrícula, a equipe confere, na própria Issue, uma checklist:
   - [ ] Campos da ficha confirmados com o cliente (nome, responsável, modalidade, turma)
   - [ ] Regra de idade mínima documentada e validada
   - [ ] Protótipo/wireframe da tela aprovado por Pedro
   
   Só quando os três itens estão marcados a tarefa entra em desenvolvimento.

3. **Avaliação de Protótipos:** o wireframe da tela de matrícula é mostrado a Pedro (e, se envolver dados de turma, a Ivan) antes da implementação final, permitindo ajustes de campos ou fluxo sem custo de retrabalho de código.

4. **Definition of Done (DoD) — aplicação prática:** ao terminar a implementação, Renato confere:
   - [ ] Cadastro salva corretamente todos os campos no banco
   - [ ] Validações de idade mínima funcionam (testadas com casos limite)
   - [ ] Sem erros no console/logs
   - [ ] Aprovação visual da equipe (a tela corresponde ao protótipo aprovado)
   
   Só depois disso a funcionalidade é considerada "pronta" tecnicamente — mas isso não substitui a validação com o cliente.

5. **Validação Final com Usuários:** a funcionalidade pronta é apresentada a Pedro na reunião semanal seguinte, onde ele testa o fluxo real de matrícula e confirma (ou não) que atende à necessidade real do CECP, não apenas à especificação técnica escrita.

Esse mesmo fluxo (Elicitação → DoR → Protótipo → Desenvolvimento → DoD → Validação com cliente) se repete para as demais características do produto (CP1, CP3, CP4, CP5), ajustando quais stakeholders participam de cada etapa conforme o tema (Ivan para turmas, Sandra para doações e relatórios).

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.1 | 12/09/2026 | Correções da issue #22: composição da equipe, disponibilidade do cliente, definições de iteração/unidade, registro de decisões, ampliação de stakeholders e processo de validação | Maria Eduarda | — |
| 1.2 | 21/09/2026 | Adição da disponibilidade de Ivan e Sandra e detalhamento dos papéis na ampliação de stakeholders | Maria Eduarda | — |
| 1.3 | 22/09/2026 | Revisão para tornar o documento prático: remoção das definições de iteração/unidade, aplicação concreta de DoR/DoD com exemplo real (matrícula online), e detalhamento da atuação prática do Analista de Requisitos | Maria Eduarda | — |