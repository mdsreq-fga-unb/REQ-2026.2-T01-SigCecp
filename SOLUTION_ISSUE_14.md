# Solution for Issue #14

## 🛠️ Proposed Solution (by Aditya Waghamare)

### Analysis
The issue points out several gaps and inconsistencies in the Unidade 1 requirements document for the SigCecp project:
1. **Unmapped Specific Objectives (OEs)**: OE1 (Centralizing student data lacks explicit registry and academic history), OE2 (Tracking attendance and pedagogical status lacks modules for bulletins, alerts, and attendance), OE3 (Disciplinary measures unmapped), OE4 (Communication with volunteers/families unmapped), OE5 (Transparency/accountability lacks concrete reporting).
2. **Domain/Legacy Inconsistencies**: Mention of "mensalidades" (tuitions) for a free institution (CECP), unmapped legacy spreadsheets/physical docs, and risky hard-deletion of classes (CP1) instead of archiving.
3. **Architecture & Scope Ambiguities**: Unclear donation channel specifications, split between site and management system ("two solutions" vs integrated platform), tentative technology stack marked definitively, and local database deployment issues for concurrent online access.

### Fix
Below is the structural proposal and requirements patch template to resolve these points directly in the repository documentation (`docs/unidade1.md` or equivalent specification file):

```markdown
## 📋 Revisão de Capacidades e Objetivos Específicos (SigCecp)

### 1. Alinhamento de Objetivos Específicos (OE) x Capacidades (CP)
- **OE1 (Centralizar dados dos alunos):**
  - *Nova CP Adicionada:* **CP6 - Gestão de Cadastro e Histórico Acadêmico:** Módulo para registro unificado de dados cadastrais, histórico escolar/participativo e migração de registros físicos/planilhas legadas.
- **OE2 (Acompanhar frequência e situação pedagógica):**
  - *Nova CP Adicionada:* **CP7 - Diário de Classe e Monitoramento Pedagógico:** Funcionalidade de controle de frequência digital, emissão de boletins de aproveitamento e alertas automáticos de evasão/baixo rendimento.
- **OE3 (Registrar medidas disciplinares):**
  - *Nova CP Adicionada:* **CP8 - Registro Disciplinar:** Módulo restrito para anotação de ocorrências, medidas corretivas aplicadas e acompanhamento com responsáveis.
- **OE4 (Melhorar comunicação com voluntários e famílias):**
  - *Nova CP Adicionada:* **CP9 - Canal de Comunicação Direta:** Mural de avisos, notificações por e-mail/SMS e canal de mensagens entre equipe pedagógica e responsáveis.
- **OE5 (Transparência e prestação de contas):**
  - *Nova CP Adicionada:* **CP10 - Relatórios de Transparência:** Geração de demonstrativos de impacto, relatórios de prestação de contas e evidências de uso de recursos.

### 2. Correções de Domínio e Inconsistências
- **Remoção de Mensalidades:** Substituição de qualquer menção a "mensalidades" por "doações voluntárias, parcerias e apoios institucionais", respeitando a gratuidade do CECP.
- **Tratamento de Legado (Planilhas e Papel):** Estabelecida a *Fetapa de Migração de Dados*, onde planilhas e fichas físicas serão importadas via rotinas assistidas ou cadastradas manualmente por operadores autorizados durante o onboarding.
- **Inativação de Turmas (Ajuste na CP1):** A exclusão física de turmas é substituída por **arquivamento/inativação lógica**, preservando o histórico de frequências e notas dos alunos vinculados.
- **Matrícula Inclusiva (Ajuste na CP2):** A inscrição online será complementada por um *Protocolo de Atendimento Híbrido/Assistido*, mitigando o risco de exclusão digital identificado na intervenção social.

### 3. Especificação do Canal de Doações e Plataforma Unificada
- **Definição do Canal de Doações:** O canal atuará como portal de *manifestação de intenção de doação, publicação de necessidades materiais/financeiras e emissão de comprovantes/recibos de entrega*, sem transações financeiras diretas complexas na versão inicial (focada em registro e agendamento).
- **Arquitetura Unificada:** Esclarecido que o projeto consiste em uma **Plataforma Modular Integrada** composta por dois frontends (Site Institucional / Portal Público + Sistema Gerencial Interno) conectados a uma API central.

### 4. Atualizações Técnicas
- **Stack Tecnológica:** FastAPI, MySQL e SQLAlchemy passam a constar explicitamente como *Stack Base Provisória*, sujeitas a validação definitiva após os testes de carga na Fase 2.
- **Persistência de Dados:** Clarificado que o banco de dados será hospedado em ambiente em nuvem gerenciado (ex: AWS RDS / PlanetScale) para garantir acesso simultâneo seguro por múltiplos usuários, descartando a restrição de "banco local".
```

### Implementation
Apply the above specification updates to the requirements document in the project repository.

### Testing
- Verify that all specific objectives (OE1-OE5) map directly to defined system capacities (CPs).
- Ensure consistency in terminology (zero mentions of "mensalidades", explicit "inativação" instead of "exclusão").
- Confirm technical feasibility of cloud database architecture vs concurrent online access.

Signed-off-by: Aditya Waghamare <adityawaghamare7620@gmail.com>


---
*Submitted by Aditya Waghamare*
💰 **Payout Address (Base L2 / EVM):** `0xb61dBcdBc3407F71EaCb64D4CBFAcf9FFfe2415C`