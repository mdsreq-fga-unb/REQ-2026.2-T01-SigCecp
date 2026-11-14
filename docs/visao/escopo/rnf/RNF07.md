### RNF07: Carregamento da página pública

[Ver no painel do escopo](../../../painel.md#RNF07)

| Campo | Descrição |
| :--- | :--- |
| **Classificação (URPS+)** | Desempenho (P, Performance) |
| **Descrição** | Carregamento da página pública em até 5s (CP3, CP7). |
| **Critério de aceitação** | LCP ≤ 5s em conexão 2G simulada (limitação de rede do Chrome DevTools/Lighthouse), medido pelo Lighthouse. |
| **Origem** | Condição acordada com o cliente na [ata de 22/09](../../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_22_09.md): conteúdo principal visível em até 5s mesmo em conexão 2G. A versão anterior citava 3G (corrigido em 14/11/2026, issue #29) |
| **CP de origem** | CP3, CP7 (ver [8.1](../../../historico/8_0_requisitos.md)) — CP2 é Registro de doações e prestação de contas, que não tem módulo público |
| **RFs que aplicam** | [RF13](../requisitos/RF13.md): Publicar conteúdo institucional<br>[RF14](../requisitos/RF14.md): Editar conteúdo institucional<br>[RF15](../requisitos/RF15.md): Consultar conteúdo institucional<br>[RF16](../requisitos/RF16.md): Remover conteúdo institucional<br>[RF17](../requisitos/RF17.md): Publicar evento<br>[RF18](../requisitos/RF18.md): Editar evento<br>[RF19](../requisitos/RF19.md): Remover evento<br>[RF20](../requisitos/RF20.md): Consultar eventos |

Origem histórica em [8.2](../../../historico/8_0_requisitos.md). Voltar ao [painel do escopo](../../../painel.md).
