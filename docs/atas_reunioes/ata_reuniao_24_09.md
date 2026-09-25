# Ata de Reunião - Entrevista com Professor e Priorização de Requisitos (CECP)

**Data:** 24 de setembro de 2026  
**Modalidade:** Presencial  
**Participantes pela equipe do projeto:** Marcos Vinicius Monteiro  
**Participantes representando o CECP:** Pedro Augusto Cajado Coutinho e o professor Marcos Xavier Santana, conhecido como **"Marcão"** (professor de Judô e Jiu-Jitsu)  
**Pauta:** Entrevista com o professor Marcão sobre o acompanhamento pedagógico e disciplinar dos alunos; Sessão de priorização dos requisitos já levantados, usando o método **MoSCoW** (Tem que ter / Deveria ter / Poderia ter / Não precisa ter)

## 1. Entrevista com o professor Marcão, acompanhamento disciplinar e pedagógico

Marcos entrevistou o professor Marcão especificamente sobre como funcionam, hoje, as sanções aplicadas aos alunos e o acompanhamento do desempenho escolar deles, ponto que a equipe precisava detalhar melhor com quem lida diretamente com isso no dia a dia.

**Situação atual relatada pelo professor:**
- Não existe hoje nenhum sistema digital para acompanhar se os alunos realmente cumprem os requisitos exigidos (ex.: comprovação de bom desempenho escolar, necessária para evoluir de faixa), o controle depende, em grande parte, da **boa-fé do aluno**, sem verificação sistemática de todos os casos;
- Quando um aluno apresenta um comportamento que não condiz com o esperado, a primeira ação do professor é sempre **conversar**, buscando entender a situação antes de qualquer sanção;
- **Não existe uma escala padronizada de sanções**, as medidas evoluem de forma subjetiva, a critério de cada professor, conforme o caso;
- O professor tenta tomar decisões de forma coletiva, conversando com os demais professores "como um comitê", mas isso **não é um processo formalizado** e nem sempre é seguido à risca;
- **Não existe nenhum registro histórico** das conversas ou sanções aplicadas a um aluno. Segundo o professor, se outro profissional assumir a turma no futuro, não terá como saber que determinada situação já ocorreu com aquele aluno, por falta de qualquer histórico ou registro físico.

Esse relato reforça diretamente a necessidade de um módulo de acompanhamento pedagógico/disciplinar com registro de frequência e de medidas disciplinares vinculado ao histórico do aluno (RF17–RF20, ver seção 3).

### Reapresentação do projeto ao professor

Como o professor Marcão não participava das reuniões anteriores, Marcos reapresentou o contexto e os objetivos do projeto a ele: um sistema para reduzir a dependência do papel e dar mais autonomia e controle à coordenação da ONG. Foram reapresentados os objetivos específicos (centralizar os dados dos alunos, garantir o acompanhamento e o histórico de medidas disciplinares, facilitar a comunicação entre os voluntários, garantir transparência para parceiros e editais) e a lista de funcionalidades já levantadas anteriormente (gestão de turmas, registro de doações, gestão de conteúdo institucional, cadastro/histórico do aluno, acompanhamento pedagógico/disciplinar, comunicação, pré-matrícula).

## 2. Dinâmica da sessão de priorização (MoSCoW)

Encerrada a entrevista, a reunião seguiu para uma dinâmica de priorização: Marcos leu, um a um, os requisitos já levantados anteriormente, e pediu que Pedro e o professor classificassem cada um como:
- **Tem que ter**, essencial, sem ele o sistema não cumpre seu propósito;
- **Deveria ter**, importante e de alto valor, porém não bloqueante para a primeira entrega;
- **Poderia ter**, desejável no futuro, mas não prioritário agora;
- **Não precisa ter**, não será considerado (por ora).

Marcos explicou que o objetivo é definir o escopo do **primeiro produto funcional** (MVP), já que o projeto completo é grande demais para ser entregue de uma vez.

## 3. Requisitos priorizados nesta reunião

> Cada linha reflete a classificação dada ao vivo por Pedro e/ou pelo professor Marcão durante a leitura dos requisitos. A coluna **ID** referencia o requisito equivalente no documento oficial de RFs/RNFs (seção 8 do documento de Visão do Produto e Projeto), ver ressalvas na seção 6.

### Autenticação e controle de acesso
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF01 | Autenticar usuário (login obrigatório para identificar quem faz cada ação) | **Tem que ter** | Justificado também pela LGPD |
| RF02 | Restringir funcionalidades administrativas exclusivamente ao perfil da coordenação | **Tem que ter** | |

### Gestão e acompanhamento de turmas (CP1)
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF03 | Cadastrar turma | **Tem que ter** |  |
| RF04 | Editar turma | **Tem que ter** |  |
| RF05 | Inativar turma, preservando o histórico de alunos e frequências vinculadas a ela | **Poderia ter** |  |
| - | Remover turma de forma definitiva (excluindo também o histórico associado) | **Não precisa ter** | Recusado explicitamente: decidiram que informações de histórico não devem poder ser apagadas dessa forma; coerente com a ausência desse item como RF separado no documento oficial |
| RF06 | Associar aluno a uma turma | **Tem que ter** |  |

### Doações e prestação de contas (CP2)
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF07 | Registrar uma doação recebida | **Poderia ter** | |
| RF08 | Registrar documento de prestação de contas (notas fiscais, registros fotográficos e audiovisuais vinculados) | **Tem que ter** | Justificado por já ser prática atual da ONG (fotos postadas no Instagram como comprovação) |
| RF09 | Consultar doações e prestações de contas já registradas | **Não precisa ter** | |

### Gestão de conteúdo institucional (CP3, módulo público)
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF10 | Publicar informações institucionais, fotos e vídeos no módulo público | **Tem que ter** | |
| RF10* | Editar esse conteúdo | **Tem que ter** | |
| RF11 | Publicar eventos | **Tem que ter** |  |
| - | Remover eventos | **Tem que ter** | Não há RF próprio no documento oficial para "remover evento", só "publicar" (RF11) e "consultar" (RF12); vale conferir se ficou de fora por descuido |
| RF12 | Permitir que qualquer visitante (sem login) consulte o conteúdo publicado | **Tem que ter** ||

### Cadastro e histórico do aluno (CP4)
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF13 | Coordenação cadastrar um novo aluno, com dados cadastrais e documentação exigida | **Tem que ter** | Houve dúvida inicial se o cadastro seria feito pelo próprio aluno ou pela coordenação, ficou definido que esse cadastro específico é feito **pela coordenação** (o autocadastro do interessado é tratado à parte, na matrícula online, RF25 a RF32) |
| RF14 | Editar dados do aluno | **Tem que ter** |  |
| RF15 | Consultar a ficha do aluno | **Tem que ter** | Restrito à coordenação |
| RF16 | Inativar aluno | **Tem que ter** | |
| RF16* | Remover do sistema os dados críticos de um aluno (ex.: RG, comprovante de residência), mediante pedido do responsável legal ou do próprio aluno maior de idade | **Não precisa ter** | Rejeitado por ora: Pedro argumentou que a ONG frequentemente precisa enviar o histórico completo de fichas, inclusive de alunos que já saíram, quando solicitado por órgãos públicos (para comprovar a rotatividade do projeto), o que tornaria essa remoção problemática. **Conflito relevante:** o próprio documento oficial exige, em RNF13, suporte a "solicitação de eliminação quando cabível" por força da LGPD|

### Acompanhamento pedagógico e disciplinar (CP5)
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF17 | Registrar a frequência dos alunos em cada aula de uma turma | **Tem que ter** |  |
| RF18 | Consultar a frequência | **Tem que ter** |  |
| RF19 | Emitir alerta de faltas críticas (limite definido pela própria ONG) | **Tem que ter** | Professor destacou que isso ajudaria bastante, já que hoje não há como mensurar precisamente as faltas de um aluno |
| RF20 | Registrar medida disciplinar (advertência, suspensão, desligamento) para um aluno, vinculada ao seu histórico | **Tem que ter** | Reforçado pelo relato do professor na seção 1 sobre a falta de qualquer registro hoje |

### Comunicação com voluntários e famílias (CP6)
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF21 | Publicar aviso no módulo público | **Tem que ter** |  |
| RF22 | Consultar aviso | **Tem que ter** | |
| RF23 | Direcionar aviso a um público específico (voluntários, famílias, ou ambos) | **Tem que ter** | |
| RF24 | Consultar o histórico de avisos publicados, incluindo o destinatário de cada um | **Tem que ter** ||

### Matrícula online / pré-matrícula (CP7)
| ID | Requisito | Prioridade | Observação |
|---|---|---|---|
| RF25 | Acessar o formulário de matrícula por link público, sem necessidade de login | **Tem que ter** |  |
| RF26 | Preencher dados do aluno no formulário, **sem** pedir, por enquanto, documentos como identidade | **Tem que ter** | |
| RF27 | Informar dados do responsável legal, obrigatório para menores de 18 anos | **Tem que ter** |  |
| RF28 | Registrar o consentimento ao termo de tratamento de dados pessoais como condição obrigatória para concluir a matrícula | **Tem que ter** | Sem aceite, não é possível se matricular |
| RF29 | Registrar o aceite ao termo de uso de imagem | **Tem que ter** | Pedro relatou um caso concreto em que um responsável se recusou terminantemente a autorizar o uso da imagem do filho ("a última reunião com o Ivan foi sobre isso"), o que reforçou a necessidade desse termo explícito. |
| RF31 | Emitir comprovante de solicitação (número de protocolo) após o envio do formulário | **Tem que ter** | Para o interessado acompanhar se a pré-matrícula foi aceita |
| RF30 | Informar pessoa(s) autorizada(s) a retirar o aluno (nome e contato), obrigatório para menores de idade | **Tem que ter** | |
| RF32 | Coordenação analisar a solicitação de matrícula recebida, definindo-a como aprovada, recusada ou em lista de espera, gerando o cadastro definitivo do aluno se aprovada | **Tem que ter** | Reforçado que a matrícula feita pelo formulário é sempre uma **pré-matrícula**: nunca vira cadastro definitivo automaticamente, sem passar por essa análise da coordenação |

### Requisitos não funcionais
| ID | Requisito / critério de aceite | Prioridade | Observação |
|---|---|---|---|
| RNF01 | Interface utilizável sem treinamento prévio, tarefa concluída em até 8 minutos por 80% dos usuários novos | **Tem que ter** | -|
| RNF02 | Conteúdo deve se adaptar a qualquer tamanho de tela, sem cortes | **Tem que ter** | |
| RNF03 | Mensagem de sucesso/erro exibida em até 2 segundos após uma ação crítica | **Tem que ter** | |
| RNF05 | Confirmação obrigatória antes de qualquer ação crítica (ex.: remover/inativar aluno) | **Tem que ter** | Reforçado por um relato: uma pessoa clicou por curiosidade em um link e apagou um formulário inteiro no "último dia" de inscrições; só não houve prejuízo porque havia uma versão já impressa/salva à parte |
| RNF04 | Preservação do histórico ao inativar turma/aluno | **Tem que ter** | - |
| RNF06 | Consultas internas da coordenação devem responder em até 3 segundos | **Tem que ter** | - |
| RNF07 | Página pública deve carregar em até 5 segundos | |
| RNF08 | Suportar ao menos 10 sessões autenticadas simultâneas sem perder desempenho | **Tem que ter** | - |
| RNF09 | Registrar (log) toda ação crítica, com data/hora e usuário responsável | **Tem que ter** | Reforçado pelo relato de um incidente em que precisa ser possível identificar quem realizou uma ação crítica |
| RNF10 | Utilizar tecnologias atuais, compatíveis com os principais navegadores | **Tem que ter** | - |
| RNF11 | Bloquear acesso direto a funcionalidades administrativas por link/rota, retornando erro de não autorizado | **Tem que ter** | |
| RNF12 | Senhas armazenadas em hash e dados sensíveis nunca em texto claro | **Poderia ter** | |
| RNF13 | Conformidade com a LGPD (Lei nº 13.709/2018) no tratamento de dados pessoais | **Tem que ter** | Justificativa direta: "se envolve lei, tem que ter" |

## 4. Ideia levantada durante a discussão de valor (não classificada formalmente)

Durante a conversa sobre o que teria "alto valor" ou "baixo valor" para o projeto, foi levantada a ideia de permitir que o **próprio aluno já cadastrado** tivesse uma conta de acesso limitado no sistema, podendo, por exemplo, se inscrever sozinho em um evento futuro (citado o exemplo de uma nova competição), sem precisar passar pela coordenação. Alunos novos (ainda não cadastrados) continuariam se cadastrando pelo processo tradicional. A ideia foi bem recebida, mas **não chegou a ser classificada no MoSCoW** nesta reunião, e também não consta no documento oficial de RFs, fica como sugestão a ser avaliada posteriormente pela equipe.

## 5. Considerações finais sobre valor (alto x baixo)

Ao final, foi pedido que os participantes resumissem, com suas próprias palavras, o que consideravam de alto e de baixo valor para o projeto:
- O professor Marcão resumiu que as funcionalidades de **alto valor** são as voltadas à **coordenação e aos alunos**, enquanto as de **baixo valor**, por ora, são as relacionadas a **doações e aos bens recebidos** pelo projeto, o que é coerente com as prioridades atribuídas na tabela da seção 3 (a maior parte dos itens de doação ficou como "poderia ter" ou "não precisa ter", enquanto praticamente todos os itens de turma/aluno/acompanhamento ficaram como "tem que ter").
- Marcos reforçou que esse levantamento e priorização, feitos neste mês, servem justamente para fechar bem o escopo antes de a equipe entrar na etapa de construção do sistema.

## 6. Observações sobre o documento oficial de RFs/RNFs

1. **RNF12 (segurança de senha) teve prioridade rebaixada ao vivo:** apesar de o documento oficial listar hash de senha e criptografia como requisito formal (sem indicar MoSCoW), na sessão de priorização isso foi classificado como "poderia ter", o que está em conflito com a exigência de LGPD (RNF13) na mesma lista, como já destacado na seção 3.
2. **"Remover evento" (levantado nesta reunião) não tem RF correspondente** no documento oficial, só "publicar evento" (RF11) e "consultar conteúdo" (RF12), verificar se essa funcionalidade ficou de fora por esquecimento.

---

*Ata elaborada a partir da transcrição de reunião presencial com participação de Marcos Vinicius Monteiro, Pedro Augusto Cajado Coutinho e do professor Marco Xavier Santana ("Marcão"), representantes do CECP, e do documento oficial de Requisitos Funcionais e Não Funcionais fornecido posteriormente pela equipe, para conhecimento e alinhamento do restante da equipe do projeto.*

*Os audios completos estão disponível no link: https://drive.google.com/drive/folders/1RiaA4gz3h7QuemGTX4gGLs_4oQRTVMH1?usp=sharing*