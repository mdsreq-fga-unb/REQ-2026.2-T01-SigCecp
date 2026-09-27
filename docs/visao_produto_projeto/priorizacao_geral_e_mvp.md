## 1. Avaliação do valor de negócio

A avaliação de negócio foi realizada com o cliente e a equipe do CECP ao longo de quatro momentos, em setembro de 2026: na reunião presencial de 22/09/2026, com José Ivan do Nascimento (presidente) e Sandra Barbosa Lopes (tesoureira), na qual boa parte dos requisitos foi apresentada e validada funcionalidade por funcionalidade; na reunião presencial de 24/09/2026, com o cliente Pedro Augusto Cajado Coutinho e o professor Marco Xavier Santana ("Marcão"), na qual os requisitos foram lidos um a um e classificados ao vivo pelo método MoSCoW; em uma validação complementar por WhatsApp, que fechou a classificação dos RFs que haviam ficado pendentes após a reunião de 24/09; e em uma validação complementar por áudio, que resolveu as inconsistências remanescentes entre os requisitos de doações/prestação de contas (RF08 a RF12) e definiu a política de remoção de dados do aluno mediante pedido formal (RF25).

### Critérios e escala utilizados

A equipe utilizou o método **MoSCoW**, associado à escala numérica de 1 a 4 definida no modelo da atividade:

| Pontuação | Classificação (MoSCoW) | Interpretação |
|:---:|---|---|
| 4 | Tem que ter (Must have) | Indispensável para resolver o problema central ou viabilizar o produto |
| 3 | Deveria ter (Should have) | Muito importante, mas o produto ainda pode operar temporariamente sem o requisito |
| 2 | Poderia ter (Could have) | Agrega valor, mas pode ser adiado sem comprometer o objetivo principal |
| 1 | Não precisa ter (Won't have now) | Não é prioritário para a versão atual |

### Avaliação de negócio dos RFs (realizada com o cliente)

| Código | Requisito | Valor de negócio | Avaliado com o cliente? | Justificativa do cliente |
|---|---|:---:|:---:|---|
| RF00 | Encerrar sessão | 4 | Sim | Confirmado via WhatsApp: "tem que ter" |
| RF01 | Autenticar usuário | 4 | Sim | Login obrigatório para identificar quem faz cada ação; justificado também pela LGPD |
| RF02 | Controlar acesso | 4 | Sim | Restringir funcionalidades administrativas exclusivamente ao perfil da coordenação |
| RF03 | Cadastrar turma | 4 | Sim | Sem observação adicional registrada |
| RF04 | Editar turma | 4 | Sim | Sem observação adicional registrada |
| RF05 | Inativar turma | 2 | Sim | Classificado como "poderia ter"; a remoção definitiva (excluindo também o histórico) foi recusada explicitamente pelo cliente |
| RF06 | Associar aluno à turma | 4 | Sim | Sem observação adicional registrada |
| RF07 | Consultar alunos de uma turma | 4 | Sim | Confirmado via WhatsApp: "tem que ter" |
| RF08 | Registrar doação recebida | 2 | Sim | Áudio: uniformizado como "poderia ter", já que o cliente reconheceu obrigação legal sobre o tratamento desses dados |
| RF09 | Editar doação recebida | 2 | Sim | WhatsApp: "não tem que ter"; revisado no áudio para "poderia ter", uniformizando com RF08, RF10, RF11, RF12 |
| RF10 | Registrar documentos de prestação de contas | 2 | Sim | Já é prática atual da ONG (fotos no Instagram como comprovação); rebaixado no áudio de "tem que ter" para "poderia ter", para manter coerência com o restante do grupo |
| RF11 | Editar documentos de prestação de contas | 2 | Sim | WhatsApp: "não tem que ter"; revisado no áudio para "poderia ter", resolvendo a inconsistência com RF10 |
| RF12 | Consultar doações e prestações de contas | 2 | Sim | Áudio: revisado de "não precisa ter" para "poderia ter" |
| RF13 | Publicar conteúdo institucional | 4 | Sim | Sem observação adicional registrada |
| RF14 | Editar conteúdo institucional | 4 | Sim | Sem observação adicional registrada |
| RF15 | Consultar conteúdo institucional | 4 | Sim | Consulta liberada a qualquer visitante, sem necessidade de login |
| RF16 | Remover conteúdo institucional | 2 | Sim | Confirmado via WhatsApp: "poderia ter" |
| RF17 | Publicar evento | 4 | Sim | Sem observação adicional registrada |
| RF18 | Editar evento | 4 | Sim | Confirmado via WhatsApp: "tem que ter" |
| RF19 | Remover evento | 4 | Sim | Item citado como "tem que ter" na reunião, mesmo sem RF próprio identificado na ata na época |
| RF20 | Consultar eventos | 4 | Sim | Confirmado via WhatsApp: "tem que ter" |
| RF21 | Cadastrar aluno | 4 | Sim | Definido que o cadastro é feito pela coordenação (o autocadastro do interessado é tratado à parte, na matrícula online) |
| RF22 | Editar aluno | 4 | Sim | Sem observação adicional registrada |
| RF23 | Consultar ficha do aluno | 4 | Sim | Consulta restrita à coordenação |
| RF24 | Inativar aluno | 4 | Sim | Sem observação adicional registrada |
| RF25 | Remover dados do aluno | 2 | Sim | A ONG passa a remover os dados do aluno mediante pedido do titular ou responsável legal, substituindo a posição anterior de retenção irrestrita; essa remoção é independente da inativação (RF24) e atende diretamente à exigência de eliminação de dados prevista na LGPD (RNF13) |
| RF26 | Registrar frequência | 4 | Sim | Sem observação adicional registrada |
| RF27 | Consultar frequência | 4 | Sim | Sem observação adicional registrada |
| RF28 | Emitir alerta de faltas críticas | 4 | Sim | Professor destacou que ajudaria bastante, pois hoje não há como mensurar precisamente as faltas de um aluno |
| RF29 | Registrar medida disciplinar | 4 | Sim | Reforçado pelo relato do professor sobre a falta de qualquer registro hoje (decisão informal, baseada em boa-fé) |
| RF30 | Publicar aviso | 4 | Sim | Sem observação adicional registrada |
| RF31 | Consultar avisos | 4 | Sim | Sem observação adicional registrada |
| RF32 | Editar aviso | 4 | Sim | Confirmado via WhatsApp: "tem que ter" |
| RF33 | Remover aviso | 2 | Sim | Confirmado via WhatsApp: "poderia ter" |
| RF34 | Consultar histórico de avisos | 4 | Sim | Sem observação adicional registrada |
| RF35 | Acessar formulário de matrícula online | 4 | Sim | Sem observação adicional registrada |
| RF36 | Preencher dados do aluno | 4 | Sim | Por enquanto, sem exigir documentos como identidade |
| RF37 | Informar dados do responsável legal | 4 | Sim | Obrigatório para menores de 18 anos |
| RF38 | Registrar consentimento de dados pessoais | 4 | Sim | Sem aceite, não é possível se matricular |
| RF39 | Registrar termo de uso de imagem | 4 | Sim | Pedro relatou caso concreto de um responsável que se recusou a autorizar o uso da imagem do filho, reforçando a necessidade do termo explícito |
| RF40 | Informar pessoas autorizadas a retirar o aluno | 4 | Sim | Obrigatório para menores de idade |
| RF41 | Emitir comprovante de solicitação | 4 | Sim | Permite ao interessado acompanhar se a pré-matrícula foi aceita |
| RF42 | Analisar solicitações de matrícula | 4 | Sim | Reforçado que a matrícula pelo formulário é sempre uma pré-matrícula: só vira cadastro definitivo após essa análise da coordenação |

## 2. Avaliação do esforço técnico

**Esforço**

| Pontuação | Interpretação       | Descrição            |
|-----------|---------------------|-----------------------|
| 1         | Esforço baixo        | até 2 horas           |
| 2         | Esforço moderado     | entre 2 e 5 horas     |
| 3         | Esforço alto         | entre 5 e 8 horas    |
| 4         | Esforço muito alto   | mais de 8 horas      |

**Complexidade**

| Pontuação | Interpretação                                                            |
|-----------|----------------------------------------------------------------------------|
| 1         | Utiliza solução conhecida, com poucas dependências                          |
| 2         | Exige alguma investigação ou integração                                    |
| 3         | Possui várias dependências ou incertezas técnicas                          |
| 4         | Apresenta elevada incerteza, integração crítica ou tecnologia não dominada  |

**Capacidade da equipe**

Para manter todas as escalas orientadas no mesmo sentido, recomenda-se avaliar a lacuna de capacidade:

| Pontuação | Interpretação                                                     |
|-----------|---------------------------------------------------------------------|
| 1         | A equipe domina plenamente os conhecimentos necessários             |
| 2         | A equipe possui conhecimento suficiente, com pouca aprendizagem adicional |
| 3         | A equipe precisa desenvolver conhecimentos relevantes                |
| 4         | A equipe ainda não possui os conhecimentos ou recursos necessários   |

A equipe deverá explicar como as avaliações serão consolidadas. Uma possibilidade é calcular:


O resultado poderá ser arredondado ou convertido para uma escala de 1 a 4, desde que a regra seja definida previamente e aplicada de forma consistente.

## 3. Consolidação das avaliações

| Código | Requisito | Valor de negócio | Justificativa do cliente | Esforço | Complexidade | Lacuna de capacidade | Esforço técnico consolidado |
|--------|-----------|:---:|---|:---:|:---:|:---:|:---:|
| RF00 | Encerrar sessão | 4 | Confirmado via WhatsApp: "tem que ter" | 1 | 1 | 2 | 1,3 |
| RF01 | Autenticar usuário | 4 | Login obrigatório; justificado também pela LGPD | 2 | 2 | 2 | 2,0 |
| RF02 | Controlar acesso | 4 | Restringir funcionalidades administrativas ao perfil da coordenação | 1 | 1 | 1 | 1,0 |
| RF03 | Cadastrar turma | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF04 | Editar turma | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF05 | Inativar turma | 2 | Classificado como "poderia ter"; remoção definitiva do histórico foi recusada | 1 | 1 | 1 | 1,0 |
| RF06 | Associar aluno à turma | 4 | Sem observação adicional registrada | 2 | 2 | 1 | 1,7 |
| RF07 | Consultar alunos de uma turma | 4 | Confirmado via WhatsApp: "tem que ter" | 1 | 1 | 1 | 1,0 |
| RF08 | Registrar doação recebida | 2 | Áudio: uniformizado como "poderia ter" | 2 | 2 | 2 | 2,0 |
| RF09 | Editar doação recebida | 2 | Áudio: revisado de "não tem que ter" para "poderia ter" | 2 | 2 | 2 | 2,0 |
| RF10 | Registrar documentos de prestação de contas | 2 | Áudio: rebaixado de "tem que ter" para "poderia ter" | 3 | 2 | 2 | 2,3 |
| RF11 | Editar documentos de prestação de contas | 2 | Áudio: revisado de "não tem que ter" para "poderia ter" | 2 | 2 | 2 | 2,0 |
| RF12 | Consultar doações e prestações de contas | 2 | Áudio: revisado para "poderia ter" | 2 | 2 | 1 | 1,7 |
| RF13 | Publicar conteúdo institucional | 4 | Sem observação adicional registrada | 3 | 2 | 2 | 2,3 |
| RF14 | Editar conteúdo institucional | 4 | Sem observação adicional registrada | 2 | 1 | 1 | 1,3 |
| RF15 | Consultar conteúdo institucional | 4 | Consulta liberada a qualquer visitante, sem necessidade de login | 1 | 1 | 1 | 1,0 |
| RF16 | Remover conteúdo institucional | 2 | Confirmado via WhatsApp: "poderia ter" | 1 | 1 | 1 | 1,0 |
| RF17 | Publicar evento | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF18 | Editar evento | 4 | Confirmado via WhatsApp: "tem que ter" | 1 | 1 | 1 | 1,0 |
| RF19 | Remover evento | 4 | Citado como "tem que ter" na reunião, mesmo sem RF próprio identificado na ata na época | 1 | 1 | 1 | 1,0 |
| RF20 | Consultar eventos | 4 | Confirmado via WhatsApp: "tem que ter" | 1 | 1 | 1 | 1,0 |
| RF21 | Cadastrar aluno | 4 | Definido que o cadastro é feito pela coordenação | 2 | 2 | 2 | 2,0 |
| RF22 | Editar aluno | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF23 | Consultar ficha do aluno | 4 | Consulta restrita à coordenação | 2 | 2 | 1 | 1,7 |
| RF24 | Inativar aluno | 4 | Sem observação adicional registrada | 2 | 1 | 2 | 1,7 |
| RF25 | Remover dados do aluno | 2 | Remoção mediante pedido formal do titular ou responsável legal | 1 | 1 | 1 | 1,0 |
| RF26 | Registrar frequência | 4 | Sem observação adicional registrada | 2 | 2 | 2 | 2,0 |
| RF27 | Consultar frequência | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF28 | Emitir alerta de faltas críticas | 4 | Professor destacou que ajudaria bastante | 2 | 2 | 2 | 2,0 |
| RF29 | Registrar medida disciplinar | 4 | Reforçado pelo relato do professor sobre a falta de registro hoje | 1 | 1 | 1 | 1,0 |
| RF30 | Publicar aviso | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF31 | Consultar avisos | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF32 | Editar aviso | 4 | Confirmado via WhatsApp: "tem que ter" | 1 | 1 | 1 | 1,0 |
| RF33 | Remover aviso | 2 | Confirmado via WhatsApp: "poderia ter" | 1 | 1 | 1 | 1,0 |
| RF34 | Consultar histórico de avisos | 4 | Sem observação adicional registrada | 2 | 2 | 1 | 1,7 |
| RF35 | Acessar formulário de matrícula online | 4 | Sem observação adicional registrada | 1 | 1 | 1 | 1,0 |
| RF36 | Preencher dados do aluno | 4 | Por enquanto, sem exigir documentos como identidade | 1 | 1 | 1 | 1,0 |
| RF37 | Informar dados do responsável legal | 4 | Obrigatório para menores de 18 anos | 1 | 1 | 1 | 1,0 |
| RF38 | Registrar consentimento de dados pessoais | 4 | Sem aceite, não é possível se matricular | 2 | 2 | 2 | 2,0 |
| RF39 | Registrar termo de uso de imagem | 4 | Caso concreto relatado por Pedro | 2 | 2 | 1 | 1,7 |
| RF40 | Informar pessoas autorizadas a retirar o aluno | 4 | Obrigatório para menores de idade | 1 | 1 | 1 | 1,0 |
| RF41 | Emitir comprovante de solicitação | 4 | Permite ao interessado acompanhar se a pré-matrícula foi aceita | 2 | 2 | 2 | 2,0 |
| RF42 | Analisar solicitações de matrícula | 4 | Matrícula pelo formulário é sempre pré-matrícula | 2 | 2 | 1 | 1,7 |

## 4. Construção da matriz 4 × 4

Os RFs foram posicionados na matriz cruzando o **valor de negócio** com o **esforço técnico consolidado**, arredondado para a escala inteira de 1 a 4 (regra: 1,0-1,4 = 1; 1,5-2,4 = 2; 2,5-3,4 = 3; 3,5-4,0 = 4).

| Valor de negócio ↓ / Esforço técnico → | 1 (Baixo) | 2 (Moderado) | 3 (Alto) | 4 (Muito alto) |
|---|---|---|---|---|
| **4 (Muito alto)** | **Prioridade máxima (21):** RF00, RF02, RF03, RF04, RF07, RF14, RF15, RF17, RF18, RF19, RF20, RF22, RF27, RF29, RF30, RF31, RF32, RF35, RF36, RF37, RF40 | **Forte candidato ao MVP (13):** RF01, RF06, RF13, RF21, RF23, RF24, RF26, RF28, RF34, RF38, RF39, RF41, RF42 | *(nenhum RF)* | *(nenhum RF)* |
| **3 (Alto)** | *(nenhum RF)* | *(nenhum RF)* | *(nenhum RF)* | *(nenhum RF)* |
| **2 (Moderado)** | **Avaliar oportunidade (4):** RF05, RF16, RF25, RF33 | **Entrega futura (5):** RF08, RF09, RF10, RF11, RF12 | *(nenhum RF)* | *(nenhum RF)* |
| **1 (Baixo)** | *(nenhum RF)* | *(nenhum RF)* | *(nenhum RF)* | *(nenhum RF)* |

### Leitura da matriz

- **Quadrante "Prioridade máxima" (valor 4, esforço 1), 21 RFs**: autenticação/acesso (RF00, RF02), gestão de turmas (RF03, RF04, RF07), conteúdo institucional e eventos (RF14, RF15, RF17 a RF20), avisos (RF22, RF27, RF29 a RF32), matrícula online (RF35 a RF37, RF40).
- **Quadrante "Forte candidato ao MVP" (valor 4, esforço 2), 13 RFs**: autenticação de fato (RF01), turmas (RF06), conteúdo institucional (RF13), cadastro/edição/consulta/inativação de aluno (RF21, RF23, RF24), frequência e disciplina (RF26, RF28), avisos (RF34), LGPD/consentimento (RF38, RF39), matrícula (RF41, RF42).
- **RF05, RF16, RF25 e RF33** ficaram em "avaliar oportunidade": valor de negócio moderado (2), mas esforço técnico baixo.
- **RF08, RF09, RF10, RF11, RF12** ficaram em "entrega futura": valor de negócio moderado (2) e esforço técnico moderado, coerente com a classificação "poderia ter" dada pelo cliente.

## 5. Definição dos RFs do MVP

Após a construção da matriz 4×4 (seção 4), a equipe selecionou os RFs que integrarão o MVP com base na posição na matriz, na necessidade de formar um fluxo de uso minimamente completo e nas dependências entre requisitos.

### RFs selecionados para o MVP (37 de 43)

**Acesso e controle de usuários** (base de todo o fluxo, precisam ser implementados primeiro)
- RF00 - Encerrar sessão
- RF01 - Autenticar usuário
- RF02 - Controlar acesso

**Gestão e acompanhamento de turmas (CP1)**
- RF03 - Cadastrar turma
- RF04 - Editar turma
- RF06 - Associar aluno à turma
- RF07 - Consultar alunos de uma turma

**Gestão de conteúdo institucional (CP3)**
- RF13 - Publicar conteúdo institucional
- RF14 - Editar conteúdo institucional
- RF15 - Consultar conteúdo institucional
- RF16 - Remover conteúdo institucional
- RF17 - Publicar evento
- RF18 - Editar evento
- RF19 - Remover evento
- RF20 - Consultar eventos

**Cadastro e histórico de alunos (CP4)**
- RF21 - Cadastrar aluno
- RF22 - Editar aluno
- RF23 - Consultar ficha do aluno
- RF24 - Inativar aluno
- RF25 - Remover dados do aluno

**Acompanhamento pedagógico e disciplinar (CP5)**
- RF26 - Registrar frequência
- RF27 - Consultar frequência
- RF28 - Emitir alerta de faltas críticas
- RF29 - Registrar medida disciplinar


**Comunicação com voluntários e famílias (CP6)**
- RF30 - Publicar aviso
- RF31 - Consultar avisos
- RF32 - Editar aviso
- RF33 - Remover aviso
- RF34 - Consultar histórico de avisos

**Matrícula online (CP7)**
- RF35 - Acessar formulário de matrícula online
- RF36 - Preencher dados do aluno
- RF37 - Informar dados do responsável legal
- RF38 - Registrar consentimento de dados pessoais
- RF39 - Registrar termo de uso de imagem
- RF40 - Informar pessoas autorizadas a retirar o aluno
- RF41 - Emitir comprovante de solicitação
- RF42 - Analisar solicitações de matrícula

### Justificativa da seleção

O conjunto acima cobre todas as posições de "Prioridade máxima" e "Forte candidato ao MVP" da matriz (seção 4), e forma um fluxo de uso completo: um usuário se autentica (RF00-RF02), cadastra e organiza turmas (RF03-RF04, RF06-RF07), matricula e acompanha alunos (RF21-RF24, RF26-RF29), aplica medidas disciplinares quando necessário (RF29), divulga e gerencia conteúdo institucional e eventos (RF13-RF20), comunica-se com famílias e voluntários (RF30-RF34) e recebe pré-matrículas pelo módulo público (RF35-RF42).

**RF16 (remover conteúdo institucional), RF25 (remover dados do aluno) e RF33 (remover aviso)** ficaram posicionados no quadrante "avaliar oportunidade" da matriz (valor de negócio 2, esforço técnico baixo). A equipe decidiu incluir os três no MVP pela mesma lógica: são RFs de baixo esforço técnico (1,0), e cada um completa um par funcional já presente no MVP (RF16 acompanha RF13/RF14/RF15, RF25 tem peso legal via RNF13/LGPD, e RF33 acompanha RF30/RF31/RF32). Deixar apenas a criação/edição/consulta sem a remoção correspondente geraria um fluxo incompleto nesses três módulos.

Nenhum dos RFs selecionados apresentou combinação de valor alto com esforço alto ou muito alto na matriz, então não foi necessário decompor, reduzir escopo ou planejar entrega parcial de nenhum item.

### RFs não incluídos no MVP (6 de 43)

| RF | Motivo da exclusão |
|---|---|
| RF05 — Inativar turma | Valor de negócio moderado (2), classificado como "poderia ter" pelo cliente; a remoção definitiva de turma foi recusada, mas a inativação em si pode ser adiada sem comprometer o fluxo mínimo |
| RF08 — Registrar doação recebida | Valor de negócio moderado (2) e esforço técnico moderado; classificado como "poderia ter" |
| RF09 — Editar doação recebida | Valor de negócio moderado (2) e esforço técnico moderado; decorrência direta de RF08 |
| RF10 — Registrar documentos de prestação de contas | Valor de negócio moderado (2) e o maior esforço técnico do conjunto (2,3); apesar de já ser prática atual da ONG, não é indispensável para a solução mínima |
| RF11 — Editar documentos de prestação de contas | Valor de negócio moderado (2) e esforço técnico moderado; decorrência direta de RF10 |
| RF12 — Consultar doações e prestações de contas | Valor de negócio moderado (2) e esforço técnico moderado |

## 6. Tratamento dos RNFs

| ID | Descrição | Classificação | Justificativa |
|---|---|---|---|
| RNF01 | Interface que permite ao usuário realizar tarefas sem precisar de muito tempo de aprendizado ou treinamento para voluntários sem experiência técnica (CP1, CP3, CP4, CP5) | **Obrigatório para o MVP** | Critério de aceite validado com o cliente em 23/09 (usuários novatos cumprem tarefas em até 8 min, 80% de sucesso); aplica-se a todos os fluxos administrativos selecionados no MVP |
| RNF02 | O módulo público deve adaptar sua interface ao tamanho da tela, mantendo legibilidade e organização em diferentes resoluções | **Associado a RFs do MVP** | Aplica-se especificamente aos RFs do módulo público presentes no MVP: RF13-RF20 (conteúdo institucional/eventos), RF30-RF34 (avisos) e RF35-RF42 (matrícula online) |
| RNF03 | Feedback ao usuário em ações críticas, como registrar frequência, aplicar medida disciplinar e inativar aluno ou turma | **Obrigatório para o MVP** | Cobre ações críticas presentes no MVP: RF26 (registrar frequência), RF29 (medida disciplinar), RF24 (inativar aluno) e RF25 (remover dados do aluno) |
| RNF04 | Preservação de histórico ao inativar turma ou aluno | **Obrigatório para o MVP** | Condição para RF24 (inativar aluno), que está no MVP. |
| RNF05 | O sistema deve solicitar confirmação antes da execução de ações críticas que possam alterar ou inativar registros relevantes | **Obrigatório para o MVP** | Aplica-se a RF24 (inativar aluno), RF25 (remover dados) e RF29 (medida disciplinar), todos no MVP |
| RNF06 | Resposta das consultas internas em até 3s (ficha do aluno, frequência, turmas) | **Obrigatório para o MVP** | Critério de aceite validado com o cliente; aplica-se diretamente a RF07 (consultar alunos de turma), RF23 (ficha do aluno) e RF27 (consultar frequência), todos no MVP |
| RNF07 | Carregamento da página pública em até 5s (CP2, CP3) | **Associado a RFs do MVP** | Aplica-se ao módulo público do MVP: RF15 (conteúdo institucional), RF20 (eventos), RF31 (avisos) e RF35 (formulário de matrícula) |
| RNF08 | O sistema deve suportar o acesso simultâneo de usuários autenticados sem ultrapassar os limites de desempenho definidos para as operações internas | **Evolutivo** | Relevante para escala (10 sessões simultâneas), mas não bloqueia a entrega inicial do MVP com a equipe reduzida de coordenação da ONG |
| RNF09 | Logs de operações críticas | **Obrigatório para o MVP** | Segurança mínima exigida para toda criação/edição/inativação/remoção presente no MVP (turma, aluno, medida disciplinar) |
| RNF10 | O sistema deve utilizar padrões e tecnologias web atuais e amplamente adotados, garantindo compatibilidade com navegadores modernos | **Obrigatório para o MVP** | Condição mínima de suportabilidade para qualquer usuário (coordenação, voluntário, família) acessar o sistema |
| RNF11 | Controle de acesso por perfil (coordenação, professor/voluntário, família) | **Obrigatório para o MVP** | Diretamente associado a RF00-RF02 (sessão, autenticação, controle de acesso), base de segurança de todo o sistema no MVP |
| RNF12 | Senhas com hash e dados sensíveis criptografados | **Obrigatório para o MVP** | Segurança mínima indispensável, mesmo tendo sido classificado como "poderia ter" no MoSCoW ao vivo  divergência já registrada nas lições aprendidas da equipe |
| RNF13 | O sistema deve tratar os dados pessoais de acordo com os princípios, direitos dos titulares e requisitos de segurança e tratamento estabelecidos pela LGPD (Lei nº 13.709/2018), incluindo solicitação de eliminação quando cabível | **Obrigatório para o MVP** | Obrigatório por lei para RF38 (consentimento de dados pessoais), RF21 (cadastro de aluno) e RF25 (remoção de dados), todos no MVP. |

Nenhum RNF foi classificado como "não aplicável ao MVP": mesmo os que dependem de funcionalidades em menor escala (como RNF08, ligado a uso simultâneo) foram tratados como evolutivos, já que a plataforma como um todo  não só o MVP  precisa estar preparada para crescer.
## 7. Validação do MVP

A validação dos requisitos foi realizada em quatro momentos ao longo de setembro de 2026: duas reuniões presenciais, uma validação complementar por WhatsApp e uma validação complementar por áudio.

### Reunião de 22/09/2026 (Apresentação e validação de requisitos)
- **Quem participou:** pela equipe, Marcos; pelo CECP, José Ivan do Nascimento (presidente) e Sandra Barbosa Lopes (tesoureira)
- **O que foi validado:** apresentação, funcionalidade por funcionalidade, do levantamento de requisitos consolidado até então: gestão e acompanhamento de turmas (RF03-RF07), cadastro/edição/consulta/inativação de aluno (RF21-RF24), direito de imagem e uso de dados dos alunos (RF39), gestão de conteúdo institucional (RF13-RF17), acompanhamento pedagógico e disciplinar (frequência e alerta de faltas, RF26-RF28), além de todos os RNFs de usabilidade, responsividade, desempenho, log de auditoria, controle de acesso, segurança e LGPD, cada um já com um critério de aceite proposto pela equipe e confirmado ao vivo
- **Ideia validada em princípio nessa reunião:** a matrícula/pré-cadastro online (RF35-RF42), sugerida por Sandra Barbosa Lopes durante a apresentação, com o formato exato ainda a ser desenhado pela equipe
- **Sem dúvidas remanescentes:** José Ivan do Nascimento e Sandra Barbosa Lopes confirmaram, ao final, não ter dúvidas sobre o que foi apresentado

### Reunião de 24/09/2026 (Entrevista com o professor e priorização MoSCoW)
- **Quem participou:** pela equipe, Marcos; pelo CECP, Pedro Augusto Cajado Coutinho e o professor Marco Xavier Santana ("Marcão")
- **O que foi validado:** entrevista com o professor sobre a situação atual do acompanhamento disciplinar (hoje informal, sem registro histórico, dependente da boa-fé do aluno e da decisão subjetiva de cada professor), seguida da priorização MoSCoW de todos os RFs e RNFs já levantados, item por item; base usada para os valores de negócio da seção 3 e para a matriz da seção 4

### Validação complementar por WhatsApp (após 24/09/2026)
- **Quem participou:** Marcos e o cliente
- **O que foi validado:** classificação MoSCoW dos 9 RFs que haviam ficado pendentes após a reunião de 24/09 (RF00, RF07, RF09, RF11, RF16, RF18, RF20, RF32, RF33), além da regra de retenção de dados do aluno após a saída (relacionada a RF25)
- **Regra de retenção de dados definida nesse momento:** os dados do aluno permanecem arquivados mesmo após a saída, para fins de prestação de contas e histórico de aluno, sem divulgação ou acesso a terceiros; escopo confirmado como abrangendo todos os dados (nome, graduação, tempo que ficou, dados pessoais); quanto ao RG especificamente, o cliente mantinha a posição de guardá-lo, mas reconheceu que, se a LGPD exigir a remoção, ela deve prevalecer
- **Pendência identificada nesse momento:** classificação final de RF11 (editar documentos de prestação de contas) ficou em aberto, o cliente havia dito inicialmente "não tem que ter", mas reconheceu, na própria conversa, uma inconsistência com RF10 (registrar documento de prestação de contas, então "tem que ter"), sem confirmar o novo valor
    - **Resolução da inconsistência** entre RF08-RF12 (doações e prestação de contas), unificando todos como "poderia ter"; e definição da política de remoção de dados do aluno mediante pedido formal (RF25)
    - **Decisão sobre RF08-RF12:** todos classificados como "poderia ter", já que o cliente reconheceu obrigação legal sobre o tratamento desses dados, mas sem prioridade máxima; isso rebaixou RF10 (antes "tem que ter") e resolveu a pendência de RF11, uniformizando o grupo inteiro
    - **Decisão sobre RF25:** a ONG passa a remover os dados do aluno mediante pedido formal do titular ou responsável legal, substituindo a posição anterior de retenção irrestrita; essa remoção é independente da inativação (RF24) e atende diretamente à exigência de eliminação de dados prevista na LGPD (RNF13).

### Decisões e ajustes registrados nas quatro validações
- **Aprovado:** o núcleo de gestão de turmas, cadastro de aluno, acompanhamento pedagógico/disciplinar, conteúdo institucional, avisos e matrícula online, RFs que compõem o MVP definido na seção 5
- **Ajuste solicitado:** o alerta de faltas críticas (RF28) teve seu limite negociado ao vivo em 22/09, de 10 faltas (referência informal já usada no judô) para 8 faltas, dando à coordenação tempo de agir antes do limite máximo
- **Ajuste solicitado:** a qualidade mínima de imagem no módulo público foi definida em 22/09 como 360px.
- **Recusado:** exclusão definitiva de aluno ou turma (apenas inativação é permitida, confirmada nas duas reuniões como regra de negócio, RN01)
- **Definido:** a coexistência entre RF24 (inativar aluno) e RF25 (remover dados do aluno): são ações distintas e independentes, a inativação ocorre normalmente ao aluno sair do CECP, enquanto a remoção só se dá mediante pedido formal do titular ou responsável legal, não havendo conflito entre RF25, RNF04 e RNF13
- **Resolvido:** a inconsistência entre RF08-RF12, uniformizados como "poderia ter" na validação por áudio
