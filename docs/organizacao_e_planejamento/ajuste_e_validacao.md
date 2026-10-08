# Ajuste e Validação de Requisitos

Ajuste e validação dos requisitos baseado nos feedbacks oferecidos pela equipe Squad Guerreiros

| Código | Problema identificado | Ajuste proposto | Decisão da Equipe | Ajuste Realizado |
|---|---|---|---|---|
| RF01/RF02/RF17/RF21/RF22 | RF01 e RF02 restringem o acesso à coordenação, mas RF17, RF21 e RF22 exigem outros perfis. | Definir a lista oficial de perfis e alinhar RF01, RF02, RF17, RF21, RF22 e RNF11 a ela. | Parcialmente Aceito | No RF17 foi ajustado para que somente a coordenação registre a frequência dos alunos; RF21 e RF22 foram corrigidos quanto à escrita. RF01 e RF02 foram mantidos. |
| RF22 | Não descreve como o sistema identifica o destinatário de um aviso restrito. | Definir se avisos são públicos ou restritos e, se restritos, como o destinatário é identificado. | Aceito | RF22 corrigido quanto à escrita. |
| RF10 | Reúne publicar e editar conteúdo institucional no mesmo requisito. | Separar em requisitos de publicar e editar. | Aceito | RF10 foi dividido em dois requisitos (RF13 e RF14). |
| RF06 | Reúne associar e remover associação de aluno a turma no mesmo requisito. | Separar em "Associar aluno à turma" e "Remover aluno da turma". | Não Aceito | A funcionalidade descrita não necessita de outro requisito. |
| RF16/RF20 | "Inativar aluno" (RF16) e "desligamento" (RF20) podem descrever o mesmo evento. | Explicar a relação entre os dois e referenciar um requisito no outro. | Não Aceito | Não há duplicidade, os termos referenciados são sinônimos. |
| RF (ausente) | A seção 2.1 prevê manifestação de interesse online, mas não há RF correspondente. | Confirmar se permanece no escopo e incluir o RF correspondente. | Não Aceito | Não cobre a realidade do produto. |
| RF (ausente) | A solução prevê acompanhar desempenho escolar (CP5/OE2), mas RF17-RF20 só cobrem frequência e medida disciplinar. | Confirmar com o cliente quais dados escolares serão acompanhados e especificar os RFs necessários. | Aceito | Foi adicionada uma CP que engloba a solução do problema apontado (CP7). |
| RF (ausente) | Não há RF para cadastrar voluntários e famílias, nem para vincular família a aluno. | Incluir RFs de cadastro de voluntários/famílias e de vínculo família-aluno. | Não Aceito | Não cobre a realidade do produto. |
| RNF04 | Preservação de histórico repete o comportamento já descrito em RF05 e RF16. | Manter a regra em um só lugar (RF ou RNF) e referenciar o outro. | Não Aceito | Feedback não está claro. |
| RNF09 | Logs de operações críticas está classificado como Suportabilidade. | Reclassificar como Segurança ou justificar a classificação atual. | Aceito | O requisito agora está na seção de Segurança. |
| RNF08 | Não está vinculado a nenhum RF/OE na matriz 8.3. | Vincular o RNF08 a um RF/OE na matriz. | Aceito | Vinculado à Matriz de Rastreabilidade. |
| RNF04 | Cita "aluno (CP5)", mas RF16 (inativar aluno) pertence ao CP4. | Corrigir a CP associada e conferir a matriz. | Aceito | CP associada corrigida. |
| RNF13/RNF04/RF05/RF16 | RNF13 exige atender pedidos de eliminação de dados, mas RF05, RF14, RF16 e RNF04 exigem preservar histórico. | Definir quando a eliminação se aplica e quando o histórico deve ser mantido, validando com o cliente. | Parcialmente Aceito | Foi criado um novo requisito para resolver o conflito (RF25). |
| RNF (ausente) | Nada sobre backup e recuperação de dados, nem sobre comunicação segura (HTTPS, expiração de sessão). | Incluir RNF de backup e RNF de comunicação segura/gestão de sessão. | Não Aceito | Os requisitos de segurança já cobrem a proteção dos dados pessoais. |
