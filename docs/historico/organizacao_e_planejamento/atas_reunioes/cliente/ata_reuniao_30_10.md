# Ata de Reunião: Validação do Protótipo e do Escopo do MVP (CP3)

## 1. Identificação da reunião

**Projeto:** Sistema de Gestão do Centro Esportivo Cultural de Planaltina (SigCECP)  
**Data:** 30/10/2026 (confirmar, ver seção 8)  
**Modalidade:** Remota (videochamada, com compartilhamento de tela)  
**Participantes pela equipe do projeto:** Marcos Vinicius Monteiro  
**Participante representando o CECP:** Pedro Augusto Cajado Coutinho (coordenação)  
**Responsável pelo registro:** Marcos Vinicius Monteiro  
**Iteração do cronograma:** 5 (design do usuário), com a revisão do MVP prevista para a Iteração 6  
**Pauta:** (1) Apresentar o protótipo das telas de [RF13](../../../../visao/escopo/requisitos/RF13.md) a [RF20](../../../../visao/escopo/requisitos/RF20.md) e obter a validação do cliente; (2) rever o escopo do MVP; (3) alinhar como a construção seguirá.

## 2. Protótipo apresentado

O protótipo tem **18 telas**, navegáveis em sequência. Marcos explicou que se trata de um protótipo estático: os elementos não respondem a cliques, e a navegação é feita pela setinha para o lado.

**Módulo público**

- **Página institucional:** menu superior com acesso à página institucional, aos eventos e à área da coordenação. A publicação mais recente aparece em **destaque** no topo. Abaixo, a seção "Por dentro do CECP" lista todas as publicações, com **paginação** quando houver mais do que cabe na tela, e há um rodapé.
- **Tela de uma publicação:** título, imagem, vídeo e demais conteúdos.
- **Lista de eventos:** eventos nos estados **em breve**, **em andamento** e **encerrado**, com **filtro** por estado.
- **Tela do evento** (exemplo: Copa de Judô 2026): todas as informações, como cobrança, Pix, data limite de pagamento, alimentação, pesagem e vídeo (opcional).

**Área da coordenação**

- Telas de **publicar** e de **editar** conteúdo institucional (editar permite alterar texto, remover ou substituir imagem e vídeo).
- Tela de **listagem** das publicações, com botões de editar e remover.
- Tela de **confirmação de remoção**: antes de excluir, o sistema pergunta se a coordenação realmente quer remover, porque a exclusão é definitiva e não pode ser desfeita.
- Sequência equivalente para **eventos**: publicar, editar, listar e confirmar remoção.

**Comportamentos demonstrados**

- No formulário de evento, o botão de publicar fica **desabilitado (cinza)** enquanto algum campo obrigatório estiver vazio.
- Se o evento for **gratuito**, as informações de pagamento não aparecem. Se for cobrado, valor, data limite e meio de pagamento passam a ser exigidos.

**Telas para celular**

- Há **quatro telas** para celular: página institucional, publicação, lista de eventos e evento.
- As telas da coordenação existem **somente para computador**. Pelo que foi dito nas reuniões, essas operações não serão feitas pelo celular. Além disso, quem preenche (por exemplo, o José Ivan) poderia se confundir no celular. O cliente concordou.

## 3. Feedback e validação do cliente

- O cliente achou o resultado **agradável visualmente** e disse que ficou "perfeito", como imaginava.
- Não apontou ajustes nem itens de que não tenha gostado.
- **O protótipo foi aprovado pelo cliente.**
- O cliente pode mostrar o protótipo à Sandra e a quem mais quiser, e comentou que faria isso e traria o retorno à equipe.

## 4. Escopo do MVP

Marcos compartilhou a matriz com as notas de valor de negócio (do cliente) e de esforço técnico (da equipe). Entram no MVP, neste primeiro momento, os itens marcados em verde:

- **Acesso:** encerrar sessão, autenticar e controlar acesso (RF00 a RF02);
- **Turmas:** cadastrar turma, associar alunos a uma turma e consultar alunos de uma turma (RF03, RF06 e RF07);
- **Módulo público:** conteúdo institucional e eventos, já detalhados e prototipados (RF13 a RF20);
- **Alunos:** cadastrar aluno, editar aluno, consultar a ficha de um aluno e inativar aluno (RF21 a RF24).

Os demais requisitos **continuam existindo**, mas não são prioridade agora. O cliente confirmou que entendeu e **validou o escopo do MVP**.

## 5. Como a construção seguirá

- Cada parte do sistema segue o mesmo ciclo: (1) reunião de detalhamento dos requisitos e regras de negócio, (2) apresentação do design ao cliente, (3) ajustes e nova validação, (4) construção. O cliente dá o feedback sobre o design e, se não gostar, a equipe ajusta e espera nova validação antes de construir.
- A equipe vai detalhar o máximo de requisitos possível em cada sequência, para não perder tempo.
- A construção começa na **próxima segunda-feira (02/11/2026)**, e o MVP deve ficar pronto em **3 a 4 semanas**.
- O cliente combinou conversar na segunda-feira para organizar o detalhamento da próxima parte.

## 6. Decisões

- Protótipo das telas de RF13 a RF20 aprovado pelo cliente ([DEC12](../../../../visao/escopo/decisoes.md)).
- Telas da coordenação somente para computador; celular apenas com as quatro telas públicas ([DEC13](../../../../visao/escopo/decisoes.md)).
- Evento gratuito não exibe dados de pagamento, e o botão de publicar fica desabilitado até todos os campos obrigatórios serem preenchidos ([DEC14](../../../../visao/escopo/decisoes.md)).
- Confirmação antes de remover, já prevista, foi prototipada para conteúdo e eventos ([DEC02](../../../../visao/escopo/decisoes.md)).
- Escopo do MVP, com 18 RFs, validado pelo cliente ([DEC03](../../../../visao/escopo/decisoes.md)).

## 7. Encaminhamentos

| Ação | Responsável | Prazo |
| :--- | :--- | :--- |
| Mostrar o protótipo à Sandra e a outras pessoas interessadas e trazer o retorno | Cliente | Próximos dias |
| Conversar para organizar o detalhamento da próxima parte do MVP | Equipe e cliente | Segunda-feira (02/11/2026) |
| Iniciar a construção do sistema | Equipe | A partir de 02/11/2026 |
| Reuniões de detalhamento dos próximos requisitos do MVP | Equipe e cliente | Conforme o cronograma |
| Dúvidas rápidas por WhatsApp | Todos | Contínuo |

## 8. Ocorrências e pendências

- Houve troca de plataforma de chamada no início, com o link enviado por WhatsApp, para permitir o compartilhamento de tela.
- **Pendências:** confirmar a data da reunião (o vídeo foi publicado em 30/10/2026); confirmar o retorno do cliente depois de mostrar o protótipo à Sandra.

*Ata elaborada a partir da transcrição da reunião remota entre Marcos Vinicius Monteiro e Pedro Augusto Cajado Coutinho, representante do CECP, para conhecimento e alinhamento da equipe do projeto.*

*Gravação: [Design do usuário, Iteração 5](../../../designUser_iteracao5.md).*
