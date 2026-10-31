# Ata de Reunião: Detalhamento dos Requisitos do Módulo Público (CP3)

## 1. Identificação da reunião

**Projeto:** Sistema de Gestão do Centro Esportivo Cultural de Planaltina (SigCECP)  
**Data:** 21/10/2026 (confirmar, ver seção 8)  
**Modalidade:** Remota (videochamada)  
**Participantes pela equipe do projeto:** Marcos Vinicius Monteiro  
**Participante representando o CECP:** Pedro Augusto Cajado Coutinho (coordenação)  
**Responsável pelo registro:** Marcos Vinicius Monteiro  
**Iteração do cronograma:** 5  
**Pauta:** Detalhar os requisitos [RF13](../../../../visao/escopo/requisitos/RF13.md) a [RF20](../../../../visao/escopo/requisitos/RF20.md), da característica CP3 (Gestão de conteúdo institucional), levantando as regras de negócio necessárias para a equipe construir o MVP.

## 2. Contexto

Marcos lembrou que o escopo foi fechado e validado com o cliente nas reuniões anteriores, com a matriz de valor de negócio e esforço técnico, e que a etapa de levantamento de requisitos acabou. A partir da Iteração 5 começa a construção do sistema, e o primeiro passo é detalhar cada requisito do MVP.

Segundo o cronograma, os requisitos RF13 a RF20 são detalhados nesta iteração. Marcos explicou que a descrição básica de cada requisito não basta para construir o sistema: é preciso conhecer as **regras de negócio** da ONG, como a regra já citada de que a inscrição de aluno menor de 18 anos é feita com o responsável. Se a equipe errar uma regra, a reunião precisa ser refeita, o que atrasa os dois lados.

Durante a construção, haverá contato com o cliente cerca de **três vezes por semana**.

## 3. Identidade visual

- A ONG já possui identidade visual própria (logo e paleta de cores).
- Cores predominantes: **preto, branco e vermelho**. O amarelo também é usado, para dar destaque.
- Essas cores valem para eventos e demais materiais da ONG.
- O cliente se comprometeu a enviar a **logo** à equipe.

## 4. Conteúdo institucional (RF13 a RF16)

**Publicar ([RF13](../../../../visao/escopo/requisitos/RF13.md))**

- Somente a **coordenação** publica, depois de entrar no sistema com seu login. Os professores não publicam: pedem à coordenação (exemplo dado: um professor que quer divulgar um curso de um mês).
- Formatos aceitos: **texto, imagem e vídeo**. Áudio não é necessário.
- A ONG não tem modelo nem regra de formato para as publicações. A ideia do cliente é algo parecido com uma publicação livre (aviso, banner ou imagem informativa).
- O único campo obrigatório é o **título**. Não há conjunto fixo de dados, porque a publicação pode ser apenas uma imagem que já contém todas as informações.

**Editar ([RF14](../../../../visao/escopo/requisitos/RF14.md))**

- Somente a coordenação edita: alterar o texto, trocar ou remover foto e vídeo.
- Não é necessário indicar ao público que a publicação foi editada.

**Consultar ([RF15](../../../../visao/escopo/requisitos/RF15.md))**

- Qualquer visitante pode consultar as publicações na página pública, **sem login e sem cadastro**.

**Remover ([RF16](../../../../visao/escopo/requisitos/RF16.md))**

- Somente a coordenação remove.
- A remoção é **total**: o anúncio é excluído e deixa de ser visível para todos.

## 5. Eventos e campeonatos (RF17 a RF20)

**Publicar ([RF17](../../../../visao/escopo/requisitos/RF17.md))**

- Somente a coordenação publica. As mídias aceitas são texto, imagem e **vídeo opcional**.
- Informações do evento citadas pelo cliente:
  - título (nome do evento ou da competição), subtítulo (se houver) e descrição;
  - data, horário de início e horário de término;
  - local;
  - informações gerais, como pesagem (quando houver) e se haverá alimentação ou lanche;
  - pagamento, quando o evento for cobrado: valor, data limite e Pix (ou outros meios de pagamento).
- **Regra de negócio:** o evento só é publicado com todas as informações obrigatórias. A ONG já adota a prática de não divulgar nada vago, e o sistema deve **impedir a publicação** quando faltar informação. O cliente concordou que isso também gera disciplina, porque evita correções posteriores e dúvidas.
- O cliente enviou por WhatsApp um exemplo real, o cartaz da graduação de judô (data, local, horário, valor, prazo de pagamento, Pix e itens inclusos, como faixa e certificado).

**Editar ([RF18](../../../../visao/escopo/requisitos/RF18.md))**

- Somente a coordenação edita (exemplo: corrigir uma data errada).
- A coordenação fica responsável por **avisar os alunos** sobre a alteração, e pode usar a própria página institucional para isso (por exemplo, um aviso "Mudança no campeonato"). O aluno não precisa ver, no sistema, que o evento foi editado.

**Consultar ([RF20](../../../../visao/escopo/requisitos/RF20.md))**

- A coordenação precisa de uma **lista de todos os eventos**, para consultar e editar, semelhante à listagem de competições do site de referência citado pelo cliente (na transcrição, "Zenpo"; conferir o nome).
- Estados do evento: **em breve** (ainda vai ocorrer), **em andamento** e **encerrado**. O cliente confirmou que não há outros estados.
- A consulta pública funciona como a do conteúdo institucional: qualquer pessoa, sem login.

## 6. Decisões

- Conteúdo institucional: título obrigatório e demais campos livres ([DEC06](../../../../visao/escopo/decisoes.md)).
- Somente a coordenação publica, edita e remove; a consulta é pública e sem login ([DEC07](../../../../visao/escopo/decisoes.md)).
- Remoção definitiva e responsabilidade da coordenação de avisar sobre alterações ([DEC08](../../../../visao/escopo/decisoes.md)).
- Evento só é publicado com todos os campos obrigatórios; vídeo opcional ([DEC09](../../../../visao/escopo/decisoes.md)).
- Estados do evento: em breve, em andamento e encerrado ([DEC10](../../../../visao/escopo/decisoes.md)).
- Identidade visual: preto, branco e vermelho, com amarelo para destaque ([DEC11](../../../../visao/escopo/decisoes.md)).

## 7. Encaminhamentos

| Ação | Responsável | Prazo |
| :--- | :--- | :--- |
| Enviar a logo da ONG | Cliente | A definir |
| Consolidar o detalhamento de RF13 a RF20 com as regras acima | Equipe | A definir |
| Prototipar as telas de publicação, edição, consulta e remoção | Equipe | Próxima reunião |
| Apresentar o protótipo ao cliente para aprovação | Equipe e cliente | Em cerca de 2 a 3 dias |
| Dúvidas rápidas por WhatsApp | Todos | Contínuo |

Depois da aprovação do protótipo, a equipe constrói e, no final, mostra ao cliente o resultado.

## 8. Ocorrências e pendências

- A conexão do cliente caiu no meio da reunião e ele voltou por outro dispositivo (tablet). Não foi possível compartilhar a tela nem gravar a reunião pela plataforma, então a gravação foi feita pelo celular.
- **Pendências:** confirmar a data da reunião (o arquivo de gravação indica 21/10, e o cronograma prevê reuniões em 22/10 e 23/10); confirmar o nome do site de referência.
- Na recapitulação dos campos obrigatórios, o subtítulo foi tratado como "se houver" e o cliente concordou. Esse ponto diverge da ficha do [RF17](../../../../visao/escopo/requisitos/RF17.md), que o lista como obrigatório (ver [decisões e pendências](../../../../visao/escopo/decisoes.md)).

*Ata elaborada a partir da transcrição da reunião remota entre Marcos Vinicius Monteiro e Pedro Augusto Cajado Coutinho, representante do CECP, para conhecimento e alinhamento da equipe do projeto.*

*Gravação: [Reunião 21/10/2026](../../../gravacoes/reunioes_cliente/reuniao_audio_21_10.md).*
