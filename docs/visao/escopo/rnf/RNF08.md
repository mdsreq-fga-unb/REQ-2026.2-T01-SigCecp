### RNF08: Acesso simultâneo de usuários autenticados

[Ver no painel do escopo](../../../painel.md#RNF08)

| Campo | Descrição |
| :--- | :--- |
| **Classificação (URPS+)** | Desempenho (P, Performance) |
| **Descrição** | O sistema deve suportar o acesso simultâneo de usuários autenticados sem ultrapassar os limites de desempenho definidos para as operações internas. |
| **Critério de aceitação** | Com 10 sessões autenticadas simultâneas, o P95 das requisições deve permanecer ≤ 3s sob carga normal. |
| **RFs que aplicam** | [RF02](../requisitos/RF02.md): Controlar acesso |

Origem histórica em [8.2](../../../historico/8_0_requisitos.md). Voltar ao [painel do escopo](../../../painel.md).
