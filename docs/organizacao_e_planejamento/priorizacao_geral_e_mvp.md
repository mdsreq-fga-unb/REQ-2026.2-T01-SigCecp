# Evidências da priorização dos requisitos

## 1. Critérios e escalas
 
Os critérios e as escalas de pontuação estão na seção 10.2.1 do Backlog de Produto: **o valor de negócio (MoSCoW) vai de 1 a 4**, e **o esforço técnico é avaliado em três dimensões (esforço, complexidade e lacuna de capacidade da equipe), também de 1 a 4**. Neste documento, cada dimensão da equipe foi consolidada pela moda das respostas individuais, e o esforço técnico (ET) é a média simples das três dimensões, com uma casa decimal. Para posicionar o RF na matriz, o ET é arredondado para o inteiro mais próximo.

## 2. Origem das notas do cliente

As notas de valor de negócio foram atribuídas pelo cliente em reuniões de priorização MoSCoW. Foram realizadas duas reuniões desse tipo, porque a primeira precisou ser refeita: nela, cerca de 36 dos 42 requisitos entraram no MVP, que deixou de ser mínimo e passou a ser praticamente o produto inteiro. Na segunda reunião, o conceito de MVP foi explicado ao cliente e a classificação foi refeita. As notas da seção 3 resultam dessa priorização refeita, e a ata de 08/10/2026 registra a reunião.

| Data | Participantes | Foco | Situação |
|---|---|---|---|
| 24/09/2026 | Marcos; Pedro Augusto Cajado Coutinho e Marco Xavier Santana (CECP) | Primeira priorização MoSCoW dos RFs e RNFs | Refeita, por ter deixado quase todo o sistema dentro do MVP |
| 08/10/2026 | Marcos; Pedro (CECP) | Nova priorização MoSCoW, após explicação do conceito de MVP ao cliente | Vigente |

[Gravação completo do dia 24/09](../gravacoes/reunioes_cliente/reuniao_audio_24_09.md) e [Ata de reunião do dia 24/09](atas_reunioes/cliente/ata_reuniao_24_09.md)

[Gravação completo do dia 08/10](../gravacoes/reunioes_cliente/reuniao_audio_09_10.md) e [Ata de reunião do dia 09/10](atas_reunioes/cliente/ata_reuniao_09_10.md)

## 3. Origem das notas da equipe

- **Escala de esforço, complexidade e lacuna de capacidade:** definida na reunião interna da equipe em 26/09/2026 (Meet), com Ana, Enzo, Maria, Marcos, Rafael e Renato. Foram definidas as faixas de horas do esforço técnico e mantidos os critérios de complexidade e capacidade estabelecidos pelo professor da disciplina;
- **Votação:** como a ferramenta de votação em tempo real apresentou erro, a avaliação foi concluída por formulário (Google Forms), em 26/09/2026, entre 19:13 e 21:56. Foram registradas seis respostas: Maria Eduarda, Rafael, Enzo, Ana Paula, Renato e Alexandre. Para cada RF, cada resposta traz três valores, na ordem esforço, complexidade e lacuna de capacidade;
- **RF00 e RF01:** foram avaliados na reunião de 26/09, antes da falha da ferramenta de votação, e por isso não constam na exportação do formulário;
- **Consolidação:** moda das respostas de cada dimensão, e média simples das três dimensões para o esforço técnico (ver seção 2);
- **Registro bruto:** a seção 6 reproduz todas as respostas do formulário, a moda calculada a partir delas e o valor adotado na seção 3.

## 4. Votos individuais da equipe e moda por requisito
[Link das respostas](https://docs.google.com/spreadsheets/d/1w43YidhI-SG2slsPVc1zn649ojb0jqVa/edit?usp=sharing&ouid=100774418245311560339&rtpof=true&sd=true). Um observação, cada célula de voto traz os valores na ordem esforço, complexidade e lacuna

## 5. Notas por requisito
 
Cada linha mostra a nota de valor de negócio (cliente), as três notas de esforço técnico (equipe) e o esforço técnico (ET) calculado como a média das três.
 
| Código | Requisito | Valor de negócio (cliente) | MoSCoW | Esforço | Complexidade | Lacuna | ET (média) |
|---|---|:---:|---|:---:|:---:|:---:|:---:|
| RF00 | Encerrar sessão | 4 | Tem que ter | 1 | 1 | 2 | 1,3 |
| RF01 | Autenticar usuário | 4 | Tem que ter | 2 | 2 | 2 | 2,0 |
| RF02 | Controlar acesso | 4 | Tem que ter | 1 | 1 | 1 | 1,0 |
| RF03 | Cadastrar turma | 3 | Deveria ter | 1 | 1 | 1 | 1,0 |
| RF04 | Editar turma | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF05 | Inativar turma | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF06 | Associar aluno à turma | 3 | Deveria ter | 2 | 2 | 1 | 1,7 |
| RF07 | Consultar alunos de uma turma | 4 | Tem que ter | 1 | 1 | 1 | 1,0 |
| RF08 | Registrar doação recebida | 1 | Não precisa ter | 2 | 2 | 2 | 2,0 |
| RF09 | Editar doação recebida | 1 | Não precisa ter | 2 | 2 | 2 | 2,0 |
| RF10 | Registrar documentos de prestação de contas | 1 | Não precisa ter | 3 | 2 | 2 | 2,3 |
| RF11 | Editar documentos de prestação de contas | 1 | Não precisa ter | 2 | 2 | 2 | 2,0 |
| RF12 | Consultar doações e prestações de contas | 1 | Não precisa ter | 2 | 2 | 1 | 1,7 |
| RF13 | Publicar conteúdo institucional | 4 | Tem que ter | 3 | 2 | 2 | 2,3 |
| RF14 | Editar conteúdo institucional | 3 | Deveria ter | 2 | 1 | 1 | 1,3 |
| RF15 | Consultar conteúdo institucional | 4 | Tem que ter | 1 | 1 | 1 | 1,0 |
| RF16 | Remover conteúdo institucional | 4 | Tem que ter | 1 | 1 | 1 | 1,0 |
| RF17 | Publicar evento | 3 | Deveria ter | 1 | 1 | 1 | 1,0 |
| RF18 | Editar evento | 3 | Deveria ter | 1 | 1 | 1 | 1,0 |
| RF19 | Remover evento | 3 | Deveria ter | 1 | 1 | 1 | 1,0 |
| RF20 | Consultar eventos | 3 | Deveria ter | 1 | 1 | 1 | 1,0 |
| RF21 | Cadastrar aluno | 4 | Tem que ter | 2 | 2 | 2 | 2,0 |
| RF22 | Editar aluno | 4 | Tem que ter | 1 | 1 | 1 | 1,0 |
| RF23 | Consultar ficha do aluno | 4 | Tem que ter | 2 | 2 | 1 | 1,7 |
| RF24 | Inativar aluno | 3 | Deveria ter | 2 | 1 | 2 | 1,7 |
| RF25 | Remover dados do aluno | 1 | Não precisa ter | 1 | 1 | 1 | 1,0 |
| RF26 | Registrar frequência | 2 | Poderia ter | 2 | 2 | 2 | 2,0 |
| RF27 | Consultar frequência | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF28 | Emitir alerta de faltas críticas | 2 | Poderia ter | 2 | 2 | 2 | 2,0 |
| RF29 | Registrar medida disciplinar | 3 | Deveria ter | 1 | 1 | 1 | 1,0 |
| RF30 | Publicar aviso | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF31 | Consultar avisos | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF32 | Editar aviso | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF33 | Remover aviso | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF34 | Consultar histórico de avisos | 1 | Não precisa ter | 2 | 2 | 1 | 1,7 |
| RF35 | Acessar formulário de matrícula online | 4 | Tem que ter | 1 | 1 | 1 | 1,0 |
| RF36 | Preencher dados do aluno | 4 | Tem que ter | 1 | 1 | 1 | 1,0 |
| RF37 | Informar dados do responsável legal | 3 | Deveria ter | 1 | 1 | 1 | 1,0 |
| RF38 | Registrar consentimento de dados pessoais | 4 | Tem que ter | 2 | 2 | 2 | 2,0 |
| RF39 | Registrar termo de uso de imagem | 4 | Tem que ter | 2 | 2 | 1 | 1,7 |
| RF40 | Informar pessoas autorizadas a retirar o aluno | 2 | Poderia ter | 1 | 1 | 1 | 1,0 |
| RF41 | Emitir comprovante de solicitação | 3 | Deveria ter | 2 | 2 | 2 | 2,0 |
| RF42 | Analisar solicitações de matrícula | 3 | Deveria ter | 2 | 2 | 1 | 1,7 |
 
