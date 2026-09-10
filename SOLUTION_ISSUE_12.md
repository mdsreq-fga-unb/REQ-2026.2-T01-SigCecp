# Solution for Issue #12

## 🛠️ Proposed Solution (by Aditya Waghamare)

### Analysis
The requirement documentation for Unidade 1 (Cenário Atual do Cliente e do Negócio) contains several inconsistencies, gaps in stakeholder mapping, ambiguous user segmentation, and contradictions regarding digital presence. Specifically:
1. **Contradição sobre a presença digital**: Section 1.2 claims no digital structure exists, while Section 1.5 mentions an outdated institutional website. This must be clarified as *insufficient/outdated web infrastructure and excessive dependence on Instagram*.
2. **Sanções e Perda de Vaga**: Details regarding decision-makers, criteria, social circumstances consideration, appeal processes, and data privacy authorization needed expansion.
3. **Mapa de Stakeholders & Segmentos**: Incomplete stakeholder mapping (missing students, parents, teachers, coordinators, donors, grant evaluators, data protection authorities) and misalignment between user segments and administrative users (teachers/coordinators).
4. **Rich Picture**: "Dependência excessiva de canais digitais" is imprecise and should be corrected to "dependência excessiva do Instagram / ausência de sistema integrado".

### Fix / Contribution
Below is the proposed revision / patch text to update the project documentation (`docs/unidade1/cenario-atual.md` or equivalent specification file):

```markdown
## 1. Cenário Atual do Cliente e do Negócio

### 1.1 Introdução e Contexto
O Centro de Educação e Cidadania Popular (CECP) atua no apoio socioeducativo e cultural a crianças, adolescentes e suas famílias. O presente documento consolida o entendimento atual do negócio, seus processos, atores e canais de comunicação.

### 1.2 Infraestrutura e Presença Digital
O CECP **não possui uma estrutura digital própria e integrada** para gestão e divulgação de suas atividades acadêmicas e administrativas. Embora exista um **site institucional legado** (mencionado na seção 1.5), este encontra-se desatualizado, sem manutenção ativa e incapaz de suportar inscrições, acompanhamento pedagógico ou transparência institucional. Desse modo, a organização possui uma **dependência excessiva do Instagram** como canal único de divulgação e comunicação externa, o que gera fragilidades na retenção de histórico e engajamento formal.

### 1.3 Sanções, Desempenho e Perda de Vaga
Os alunos do CECP estão sujeitos a critérios de permanência relacionados ao desempenho escolar e comportamento. 
- **Quem toma a decisão:** A coordenação pedagógica em conjunto com a direção do CECP.
- **Critérios empregados:** Frequência mínima nas atividades, participação engajada e observância das normas de convivência.
- **Circunstâncias sociais:** O contexto socioeconômico e familiar é avaliado previamente à aplicação de qualquer medida severa, buscando suporte social em vez de exclusão direta.
- **Revisão e contestação:** Os responsáveis possuem direito a reunião com a coordenação para revisão e apresentação de justificativas.
- **Armazenamento de dados:** O CECP está autorizado a armazenar histórico de frequência, notas parciais e registros de ocorrências disciplinares, em conformidade com as diretrizes da LGPD (Lei Geral de Proteção de Dados).

### 1.4 Mapeamento Completo de Stakeholders
Os atores envolvidos diretamente com o ecossistema do CECP foram redefinidos para abranger:
1. **Alunos (crianças e adolescentes):** Usuários finais dos serviços educacionais e recreativos.
2. **Pais ou Responsáveis:** Principais interlocutores, responsáveis pela matrícula e acompanhamento.
3. **Professores e Educadores:** Usuários centrais do sistema administrativo, responsáveis pelo registro de aulas, frequência e avaliações.
4. **Coordenação e Voluntários Administrativos:** Gestores de processos, matrículas, escalas e relatórios.
5. **Doadores e Apoiadores:** Financiadores das atividades e projetos.
6. **Órgãos e Avaliadores de Editais:** Entidades fiscalizadoras e parceiras de fomento.
7. **Autoridades de Proteção de Dados:** Órgãos reguladores de conformidade da privacidade.

### 1.5 Segmentação de Usuários
- **Candidatos e Responsáveis:** Focados em acesso à informação, editais de seleção e acompanhamento de inscrições.
- **Professores e Coordenação:** Focados no uso do sistema administrativo central para controle de frequência, notas, ocorrências e comunicação interna.
- **Doadores e Comunidade:** Focados em transparência e prestação de contas.

### 1.6 Rich Picture e Diagnóstico de Canais
O diagnóstico atual aponta que o problema central não é a ausência total de tecnologia, mas sim a **centralização e dependência exclusiva do Instagram** para comunicação, somada à ausência de um sistema integrado de gestão acadêmica e de dados dos alunos.
```

### Testing
- Verify Markdown formatting and structural consistency against project template requirements.
- Ensure all points from Issue #12 are fully addressed.

Signed-off-by: Aditya Waghamare <adityawaghamare7620@gmail.com>


---
*Submitted by Aditya Waghamare*
💰 **Payout Address (Base L2 / EVM):** `0xb61dBcdBc3407F71EaCb64D4CBFAcf9FFfe2415C`