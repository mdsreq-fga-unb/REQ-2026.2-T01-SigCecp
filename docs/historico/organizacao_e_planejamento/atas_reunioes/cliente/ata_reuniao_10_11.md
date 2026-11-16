# Ata de Reunião: Teste de Aceite com o Cliente (Acesso e CP3) e Protótipo das Demais Telas do MVP

## 1. Identificação da reunião

**Projeto:** Sistema de Gestão do Centro Esportivo Cultural de Planaltina (SigCECP)  
**Data:** 10/11/2026 (gravação iniciada às 17:17; a data também é citada na reunião)  
**Modalidade:** a confirmar  
**Participantes pela equipe do projeto:** Marcos Vinicius Monteiro  
**Participante representando o CECP:** Pedro Augusto Cajado Coutinho (coordenação)  
**Responsável pelo registro:** Marcos Vinicius Monteiro  
**Iteração do cronograma:** 8  
**Pauta:** (1) Mostrar o andamento do MVP no painel do escopo; (2) apresentar o protótipo das telas restantes do MVP (acesso, turmas, alunos e coordenadores); (3) o cliente testar o sistema construído de acesso ([RF00](../../../../visao/escopo/requisitos/RF00.md) a [RF02](../../../../visao/escopo/requisitos/RF02.md)) e de conteúdo institucional e eventos ([RF13](../../../../visao/escopo/requisitos/RF13.md) a [RF20](../../../../visao/escopo/requisitos/RF20.md)).

## 2. Andamento apresentado

Marcos mostrou o [painel do escopo](../../../../painel.md) filtrado pelo MVP:

- **Acesso (RF00 a RF02)** e **conteúdo institucional e eventos (RF13 a RF20):** construídos, segundo a equipe.
- **Turmas (RF03, RF06 e RF07):** em andamento.
- **Alunos (RF21 a RF24):** previstos para uma ou duas semanas depois da reunião.

## 3. Protótipo das telas restantes do MVP

As telas seguem o mesmo estilo das telas de CP3. Só há versão para computador, porque todas são funções da coordenação ([DEC13](../../../../painel.md#DEC13)).

- **Acesso:** tela "Entrar na Coordenação", com usuário no formato do CECP (por exemplo, CECP0001) e senha. A mesma tela aparece com mensagem de erro quando os dados estão errados, depois de sair e quando o acesso não é autorizado.
- **Menu da coordenação:** é a primeira tela depois do login e dá acesso a todas as áreas.
- **Turmas:** lista com modalidade, dias, horário e quantidade de alunos, e acesso aos alunos da turma. A tela de cadastro pede modalidade, dias e horários de início e de término, todos obrigatórios; se algum estiver vazio, o sistema não salva e mostra qual falta. Uma turma sem alunos permite selecionar alunos já cadastrados. Na própria turma é possível abrir a ficha de cada aluno.
- **Alunos:**
    - A ficha do aluno tem botão de imprimir, dados cadastrais, turma, saúde e anexos. Ela mostra as pendências de documentos (por exemplo, certificado de graduação, foto 3x4 e atestado para o esporte) e permite baixar cada anexo enviado.
    - O histórico mostra as turmas do aluno, inclusive as encerradas.
    - A inativação pede confirmação. O aluno inativado mostra a data em que foi inativado.
    - No cadastro, faltar campo obrigatório (por exemplo, o nome da mãe) impede salvar. Quando não houver o dado, deve-se preencher algo como "não aplicável"; o nome do pai é opcional.
    - A turma precisa ser cadastrada antes do aluno.
- **Coordenadores:** tela para criar coordenador com nome, usuário, perfil (só existe o de coordenador), situação (ativo ou inativo), senha inicial e confirmação da senha, todos obrigatórios. Hoje, o usuário de acesso é criado pelo terminal.

**Avaliação do cliente:** Pedro achou as telas intuitivas e disse que, por ele, estão aprovadas. Ele vai mostrá-las às outras pessoas do CECP e trazer o retorno; Marcos enviará o PDF das telas.

**Retorno anterior sobre o tamanho da letra:** o José Ivan havia pedido letras maiores nas telas de CP3. Segundo o que foi dito na reunião, os demais que viram (Sandra, William, Amanda e o próprio Pedro) acharam o tamanho adequado. Ficou combinado que o sistema mantém o tamanho atual e que uma letra maior pode ser considerada para a página institucional "Quem somos", depois do MVP.

## 4. Teste do sistema pelo cliente

O sistema rodava no computador de Marcos, exposto por uma porta para o cliente acessar: não é um ambiente publicado. O cliente executou a maior parte das operações; Marcos demonstrou as tentativas de acesso indevido, a mudança de estado dos eventos e a consulta ao banco de dados.

| Requisito | O que foi testado | Resultado |
| :--- | :--- | :--- |
| [RF01](../../../../visao/escopo/requisitos/RF01.md) Autenticar usuário | O cliente criou o seu usuário (pelo terminal) e entrou com ele; Marcos tentou entrar com usuário ou senha errados | Entrou com os dados corretos; as tentativas erradas foram recusadas e registradas como "não autorizado" |
| [RF02](../../../../visao/escopo/requisitos/RF02.md) Controlar acesso | Marcos acessou o endereço da lista de eventos da coordenação sem estar logado | Acesso negado |
| [RF00](../../../../visao/escopo/requisitos/RF00.md) Encerrar sessão | O cliente saiu da área da coordenação. O trecho não aparece na transcrição da gravação; foi confirmado pela equipe em 14/11/2026 | Voltou à tela de login |
| [RF13](../../../../visao/escopo/requisitos/RF13.md) Publicar conteúdo | Publicou conteúdos com título, texto, imagem e vídeo (com e sem som) | Publicado e exibido no módulo público |
| [RF14](../../../../visao/escopo/requisitos/RF14.md) Editar conteúdo | O cliente editou um conteúdo pelo celular | Edição feita; pelo celular a tela é ruim de usar |
| [RF15](../../../../visao/escopo/requisitos/RF15.md) Consultar conteúdo | Viu a página institucional no computador e no celular | O conteúdo mais recente aparece em destaque; a página se adapta ao celular |
| [RF16](../../../../visao/escopo/requisitos/RF16.md) Remover conteúdo | Removeu conteúdos | Confirmação exibida; o conteúdo saiu do site e do banco de dados (mostrado na reunião) e não pode ser recuperado |
| [RF17](../../../../visao/escopo/requisitos/RF17.md) Publicar evento | Publicou um evento cobrado (valor e meio de pagamento em dinheiro), com alimentação e pesagem marcadas como não se aplica | Publicado com o estado "em breve" |
| [RF18](../../../../visao/escopo/requisitos/RF18.md) Editar evento | Marcos mudou a data do evento para hoje e depois para o passado | O estado mudou sozinho para "em andamento" e depois para "encerrado" |
| [RF20](../../../../visao/escopo/requisitos/RF20.md) Consultar eventos | Viu a lista pública e a lista da coordenação | Lista com os estados e as contagens de cada um |
| [RF19](../../../../visao/escopo/requisitos/RF19.md) Remover evento | Removeu o evento | Confirmação exibida; o evento saiu do banco de dados |

**Observações do teste:**

- As telas da coordenação funcionam no celular, mas não foram feitas para ele e ficam ruins de usar, como já combinado ([DEC13](../../../../painel.md#DEC13)).
- No celular, várias imagens de uma publicação aparecem uma embaixo da outra, e imagens grandes ficam cortadas.
- **Pedido do cliente:** ao clicar em uma imagem, ela deve se expandir. A equipe vai fazer essa função.

## 5. Decisões

- O cliente testou e aceitou o acesso (RF00 a RF02) e o conteúdo institucional e eventos (RF13 a RF20).
- O protótipo das telas de turmas, alunos, acesso e coordenadores foi aprovado pelo representante do cliente; falta o retorno das demais pessoas do CECP.
- Imagens das publicações serão expansíveis ao clicar.
- O tamanho da letra do sistema é mantido; uma letra maior pode ser avaliada para a página "Quem somos", depois do MVP ([DEC22](../../../../painel.md#DEC22)).

## 6. Encaminhamentos

| Ação | Responsável | Prazo |
| :--- | :--- | :--- |
| Enviar o PDF das telas de turmas, alunos e coordenadores ao cliente | Marcos | Após a reunião |
| Mostrar as telas às demais pessoas do CECP e trazer o retorno (pode ser gravado) | Cliente | Próximos dias |
| Implementar a expansão de imagem ao clicar | Equipe | A definir |
| Construir turmas (RF03, RF06 e RF07) e alunos (RF21 a RF24) | Equipe | Próximas uma ou duas semanas |

## 7. Ocorrências e pendências

- A criação de usuários da coordenação é feita pelo terminal. A tela de gestão de coordenadores foi prototipada, mas não tem requisito funcional correspondente ([PEN20](../../../../painel.md#PEN20)).
- Durante o teste, o site travou uma vez ao carregar um vídeo.
- Trechos de conversa pessoal da gravação, sem relação com o projeto, não foram registrados.

*Ata elaborada a partir da transcrição da gravação da reunião entre Marcos Vinicius Monteiro e Pedro Augusto Cajado Coutinho, representante do CECP, para conhecimento e alinhamento da equipe do projeto.*

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 14/11/2026 | Ata criada a partir da transcrição da gravação de 10/11/2026 | — | — |
| 1.1 | 14/11/2026 | Teste do RF00 (encerrar sessão) incluído, conforme confirmado pela equipe; o trecho não aparece na transcrição | — | — |
