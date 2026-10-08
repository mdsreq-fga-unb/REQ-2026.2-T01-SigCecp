# Priorização dos requisitos e definição do MVP
 
## 1. Critérios e escalas
 
**Valor de negócio (MoSCoW):** avaliado com o cliente, com a escala abaixo.
 
| Pontuação | Classificação | Interpretação |
|:---:|---|---|
| 4 | Tem que ter (Must have) | Indispensável para resolver o problema central ou viabilizar o produto |
| 3 | Deveria ter (Should have) | Muito importante, mas o produto pode operar temporariamente sem o requisito |
| 2 | Poderia ter (Could have) | Agrega valor, mas pode ser adiado sem comprometer o objetivo principal |
| 1 | Não precisa ter (Won't have now) | Não é prioritário para a versão atual |
 
**Esforço técnico:** avaliado pela equipe em três dimensões, todas orientadas no mesmo sentido (maior nota, maior dificuldade).
 
| Pontuação | Esforço | Complexidade | Lacuna de capacidade da equipe |
|:---:|---|---|---|
| 1 | Até 2 horas | Solução conhecida, com poucas dependências | A equipe domina plenamente o necessário |
| 2 | Entre 2 e 5 horas | Exige alguma investigação ou integração | Conhecimento suficiente, com pouca aprendizagem adicional |
| 3 | Entre 5 e 8 horas | Várias dependências ou incertezas técnicas | A equipe precisa desenvolver conhecimentos relevantes |
| 4 | Mais de 8 horas | Elevada incerteza, integração crítica ou tecnologia não dominada | A equipe ainda não possui os conhecimentos ou recursos |
 
**Consolidação:** o esforço técnico consolidado é a média simples de esforço, complexidade e lacuna de capacidade, com uma casa decimal. Para posicionar o RF na matriz (seção 3), o valor é arredondado para o inteiro mais próximo.
 
## 2. Avaliação consolidada
 
| Código | Requisito | Valor de negócio | Esforço | Complexidade | Lacuna | Esforço técnico |
|---|---|:---:|:---:|:---:|:---:|:---:|
| RF00 | Encerrar sessão | 4 | 1 | 1 | 2 | 1,3 |
| RF01 | Autenticar usuário | 4 | 2 | 2 | 2 | 2,0 |
| RF02 | Controlar acesso | 4 | 1 | 1 | 1 | 1,0 |
| RF03 | Cadastrar turma | 3 | 1 | 1 | 1 | 1,0 |
| RF04 | Editar turma | 2 | 1 | 1 | 1 | 1,0 |
| RF05 | Inativar turma | 2 | 1 | 1 | 1 | 1,0 |
| RF06 | Associar aluno à turma | 3 | 2 | 2 | 1 | 1,7 |
| RF07 | Consultar alunos de uma turma | 4 | 1 | 1 | 1 | 1,0 |
| RF08 | Registrar doação recebida | 1 | 2 | 2 | 2 | 2,0 |
| RF09 | Editar doação recebida | 1 | 2 | 2 | 2 | 2,0 |
| RF10 | Registrar documentos de prestação de contas | 1 | 3 | 2 | 2 | 2,3 |
| RF11 | Editar documentos de prestação de contas | 1 | 2 | 2 | 2 | 2,0 |
| RF12 | Consultar doações e prestações de contas | 1 | 2 | 2 | 1 | 1,7 |
| RF13 | Publicar conteúdo institucional | 4 | 3 | 2 | 2 | 2,3 |
| RF14 | Editar conteúdo institucional | 3 | 2 | 1 | 1 | 1,3 |
| RF15 | Consultar conteúdo institucional | 4 | 1 | 1 | 1 | 1,0 |
| RF16 | Remover conteúdo institucional | 4 | 1 | 1 | 1 | 1,0 |
| RF17 | Publicar evento | 3 | 1 | 1 | 1 | 1,0 |
| RF18 | Editar evento | 3 | 1 | 1 | 1 | 1,0 |
| RF19 | Remover evento | 3 | 1 | 1 | 1 | 1,0 |
| RF20 | Consultar eventos | 3 | 1 | 1 | 1 | 1,0 |
| RF21 | Cadastrar aluno | 4 | 2 | 2 | 2 | 2,0 |
| RF22 | Editar aluno | 4 | 1 | 1 | 1 | 1,0 |
| RF23 | Consultar ficha do aluno | 4 | 2 | 2 | 1 | 1,7 |
| RF24 | Inativar aluno | 3 | 2 | 1 | 2 | 1,7 |
| RF25 | Remover dados do aluno | 1 | 1 | 1 | 1 | 1,0 |
| RF26 | Registrar frequência | 2 | 2 | 2 | 2 | 2,0 |
| RF27 | Consultar frequência | 2 | 1 | 1 | 1 | 1,0 |
| RF28 | Emitir alerta de faltas críticas | 2 | 2 | 2 | 2 | 2,0 |
| RF29 | Registrar medida disciplinar | 3 | 1 | 1 | 1 | 1,0 |
| RF30 | Publicar aviso | 2 | 1 | 1 | 1 | 1,0 |
| RF31 | Consultar avisos | 2 | 1 | 1 | 1 | 1,0 |
| RF32 | Editar aviso | 2 | 1 | 1 | 1 | 1,0 |
| RF33 | Remover aviso | 2 | 1 | 1 | 1 | 1,0 |
| RF34 | Consultar histórico de avisos | 1 | 2 | 2 | 1 | 1,7 |
| RF35 | Acessar formulário de matrícula online | 4 | 1 | 1 | 1 | 1,0 |
| RF36 | Preencher dados do aluno | 4 | 1 | 1 | 1 | 1,0 |
| RF37 | Informar dados do responsável legal | 3 | 1 | 1 | 1 | 1,0 |
| RF38 | Registrar consentimento de dados pessoais | 4 | 2 | 2 | 2 | 2,0 |
| RF39 | Registrar termo de uso de imagem | 4 | 2 | 2 | 1 | 1,7 |
| RF40 | Informar pessoas autorizadas a retirar o aluno | 2 | 1 | 1 | 1 | 1,0 |
| RF41 | Emitir comprovante de solicitação | 3 | 2 | 2 | 2 | 2,0 |
| RF42 | Analisar solicitações de matrícula | 3 | 2 | 2 | 1 | 1,7 |

## 3. Matriz 4 × 4

![Matriz 4x4](img/matriz4x4.jpeg)

## 4. Definição do MVP
 
O MVP reúne **26 dos 43 RFs**. A seleção seguiu uma regra, aplicada a todos os requisitos:
 
1. **Posição na matriz:** entra no MVP o primeiro quadrante da matriz (seção 3), composto por: Prioridade máxima, Forte candidato ao MVP e Candidato ao MVP, o que resulta em 26 RFs.

 
## 5. Tratamento dos RNFs

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

## 6. Validação do MVP
 
A lista final do MVP foi validada com o cliente (CECP) em quatro momentos, registrados abaixo.
 
### Quem participou e quando
 
| Data | Participantes | Foco da validação |
|---|---|---|
| 22/09/2026 | Marcos; José Ivan do Nascimento e Sandra Barbosa Lopes (CECP) | Levantamento de RFs e RNFs, cada um com critério de aceite; ideia da matrícula online (RF35 a RF42), sugerida por Sandra |
| 24/09/2026 | Marcos; Pedro Augusto Cajado Coutinho e Marco Xavier Santana (CECP) | Entrevista sobre o acompanhamento disciplinar e priorização MoSCoW de todos os RFs e RNFs |
| Após 24/09/2026 (WhatsApp) | Marcos e o cliente | MoSCoW dos 9 RFs pendentes (RF00, RF07, RF09, RF11, RF16, RF18, RF20, RF32, RF33) |
| Após 24/09/2026 (áudio) | Marcos e o cliente | Unificação de RF08 a RF12 e política de remoção de dados do aluno (RF25) |
 
### RFs aprovados para o MVP
 
37 RFs: RF00 a RF04, RF06, RF07 e RF13 a RF42 (módulos listados na seção 4).
 
### RNFs aplicáveis ao MVP
 
- **Obrigatórios:** RNF01, RNF03, RNF04, RNF05, RNF06, RNF09, RNF10, RNF11, RNF12 e RNF13.
- **Associados a RFs do MVP:** RNF02 e RNF07 (módulo público).
### Requisitos para entregas futuras
 
- **RFs:** RF05 e RF08 a RF12.
- **RNFs:** RNF08 (acesso simultâneo), classificado como evolutivo.
### Ajustes solicitados
 
- **RF28:** limite do alerta de faltas críticas alterado de 10 para 8 faltas (22/09).
- **Módulo público:** resolução mínima de 360px para exibição sem sobreposição ou corte (RNF02, 22/09).
