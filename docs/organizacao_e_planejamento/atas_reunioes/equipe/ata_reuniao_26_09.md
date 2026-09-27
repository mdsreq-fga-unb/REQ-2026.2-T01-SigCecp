# Ata de Reunião - Priorização de Requisitos

## 1. Identificação da reunião

**Projeto:** Sistema de Gestão do Centro Esportivo Cultural de Planaltina (SigCECP)
**Data:** 26/09/2026
**Modalidade:** Meet  
**Participantes:** Ana, Enzo, Maria, Marcos, Rafael, Renato  
**Pauta:** Definição do esforço técnico, estabeleceu-se a escala de horas para a implementação com base em critérios técnicos, avaliação dos requisitos funcionais, discussão sobre a remoção de dados de alunos e conformidade legal vigente, mudança para votação assíncrona e criação de formulário online para continuidade da avaliação após falha na ferramenta.

## 2. Contexto e metodologia da reunião
 
Rafael e Marcos abriram a reunião para dar continuidade à priorização dos requisitos, desta vez focando na etapa de **esforço técnico**, etapa seguinte à avaliação de valor de negócio, que já havia sido feita anteriormente com o cliente (CECP). Rafael sugeriu conduzir a dinâmica como um planejamento baseado em cartas (nos moldes de Planning Poker), em que a equipe votaria os valores e justificaria os extremos (ou usaria a média das respostas). Inicialmente, porém, optaram por discutir os critérios de forma verbal antes de partir para a votação.
 
## 3. Definição da escala de esforço técnico
 
O grupo (Rafael, Marcos, Renato, Enzo e Maria Eduarda) debateu e definiu a escala de horas usada para classificar o esforço técnico de implementação de cada requisito:
 
| Classificação | Faixa de horas |
|---|---|
| Baixo | até 2 horas |
| Moderado | de 2 a 5 horas |
| Alto | de 5 a 8 horas |
| Muito alto | mais de 8 horas |
 
## 4. Critérios de complexidade técnica e capacidade da equipe
 
Marcos e Rafael decidiram manter os critérios de avaliação já pré-estabelecidos pelo professor da disciplina para as dimensões de **complexidade técnica** e **capacidade da equipe**, considerando aspectos como: uso de soluções já conhecidas pela equipe, dependências entre requisitos, incertezas técnicas envolvidas, e o domínio de conhecimento necessário das pessoas responsáveis pela implementação.
 
## 5. Tentativa de uso de ferramenta de votação (Planning Poker)
 
Rafael apresentou uma ferramenta online de planejamento para conduzir a votação dos requisitos, configurando um baralho de cartas numérico para facilitar a contagem dos votos, e convidou os demais participantes para a plataforma.
 
## 6. Avaliação inicial dos requisitos funcionais e limitação da ferramenta
 
Rafael iniciou a votação pelos primeiros requisitos funcionais, cobrindo funcionalidades como encerramento de sessão (logout), autenticação de usuários e controle de acesso, avaliando esforço, complexidade e capacidade para cada um. No meio do processo, porém, a ferramenta apresentou um **erro de limite de votação**, impedindo que a equipe continuasse a avaliação por essa via.
 
## 7. Discussão sobre exclusão de dados de alunos e conformidade legal (RF16)
 
Rafael levantou um ponto crítico sobre o requisito funcional de remoção de dados críticos de alunos (RF16, na numeração do documento oficial de RFs/RNFs), apontando um conflito aparente entre esse requisito e a necessidade de manter registros para prestação de contas e conformidade legal o mesmo ponto de tensão já sinalizado em atas anteriores desta equipe entre esse requisito e a exigência de conformidade com a LGPD.
 
Marcos esclareceu o ponto: a instituição já possui documentos de autorização preenchidos pelos responsáveis, além das fichas de inscrição dos alunos. Com base nisso, ficou definido que a exclusão, quando solicitada, apagará **apenas** os dados críticos específicos, identidade, CPF e comprovante de residência, mantendo-se os demais registros do aluno no sistema, em conformidade com a organização legal já adotada pela ONG.
 
Esse esclarecimento resolve, ao menos parcialmente, a divergência apontada nas atas de reuniões anteriores entre o RF16 (remoção de dados críticos) e o RNF13 (conformidade com a LGPD), falta apenas, conforme as próximas etapas (seção 9), validar formalmente com os stakeholders (CECP) se essa definição de "dados críticos" e a documentação legal existente são de fato suficientes.
 
## 8. Mudança para avaliação assíncrona via formulário
 
Diante da limitação técnica da ferramenta de votação, Rafael sugeriu migrar a avaliação para um formulário do Google Forms, preenchido de forma assíncrona pela equipe. Essa mudança também teve a vantagem de permitir a participação do Alexandre, que não estava presente nesta reunião. Marcos criou e publicou o formulário, orientando os demais participantes a preenchê-lo o quanto antes, e informou que a próxima reunião do grupo ocorrerá somente após a terça-feira seguinte.
 
## 9. Decisões
 
- **Definição dos parâmetros de esforço técnico:** o grupo estabeleceu as faixas de horas para classificar o esforço técnico em baixo, moderado, alto e muito alto (seção 3).
- **Adoção de formulário para estimativas assíncronas:** o grupo decidiu migrar a votação e estimativa dos requisitos para um formulário do Google, preenchido de forma assíncrona (seção 8).
- **Diretriz para exclusão de dados sensíveis:** o grupo determinou que o requisito de exclusão de dados de alunos apagará apenas os documentos específicos (identidade, CPF, comprovante de residência), utilizando os termos de consentimento já existentes (seção 7).

## 10. Próximas etapas e pendências

- **Marcos:** validar com os stakeholders (CECP) os requisitos ainda não discutido.
- **Todo o grupo:** após o prazo do formulário, consolidar as respostas recebidas, utilizando a **moda** dos valores coletados para definir os níveis finais de esforço, complexidade e capacidade de cada requisito.

*Os dados da conversa foi disponível no link: https://drive.google.com/drive/folders/1RiaA4gz3h7QuemGTX4gGLs_4oQRTVMH1?usp=sharing*