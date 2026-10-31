# Catálogo de requisitos funcionais

Visão navegável do escopo: cada linha leva à ficha do requisito. Estado, valor de negócio e entrega vêm das fichas e da [priorização](../../historico/priorizacao_geral_e_mvp.md); a declaração completa está em [8.1](../../historico/8_0_requisitos.md) e a lista de regras em [regras de negócio](regras_de_negocio.md). Cada RNF tem ficha própria em [rnf/](rnf/RNF01.md).

**Estados:** *Rascunho* (declaração e critérios vindos de 8.1 e 10.1; demais campos a detalhar), *Detalhado* (ficha completa, com regras e critérios em Dado/Quando/Então) e *Validado* (aprovado pelo cliente, com registro em ata).

**[MVP](../../historico/10_backlog_produto.md) :** 18 dos 43 RFs, com valor de negócio 3 ou 4 e esforço técnico 1 ou 2. Ver [DEC03](decisoes.md).

### Acesso e controle de usuários

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF00](requisitos/RF00.md) | Encerrar sessão | Detalhado | 4, Tem que ter | MVP | [RN17](regras_de_negocio.md#rn17), [RN18](regras_de_negocio.md#rn18) | [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF01](requisitos/RF01.md) | Autenticar usuário | Detalhado | 4, Tem que ter | MVP | [RN19](regras_de_negocio.md#rn19), [RN20](regras_de_negocio.md#rn20), [RN21](regras_de_negocio.md#rn21) | [RNF11](rnf/RNF11.md), [RNF12](rnf/RNF12.md), [RNF13](rnf/RNF13.md) |
| [RF02](requisitos/RF02.md) | Controlar acesso | Detalhado | 4, Tem que ter | MVP | [RN20](regras_de_negocio.md#rn20) | [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md), [RNF08](rnf/RNF08.md) |

### CP1: Gestão e acompanhamento de turmas

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF03](requisitos/RF03.md) | Cadastrar turma | Detalhado | 3, Deveria ter | MVP | [RN22](regras_de_negocio.md#rn22) | [RNF01](rnf/RNF01.md), [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md) |
| [RF04](requisitos/RF04.md) | Editar turma | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md) |
| [RF05](requisitos/RF05.md) | Inativar turma | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF04](rnf/RNF04.md), [RNF05](rnf/RNF05.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md) |
| [RF06](requisitos/RF06.md) | Associar aluno à turma | Detalhado | 3, Deveria ter | MVP | [RN23](regras_de_negocio.md#rn23) | [RNF03](rnf/RNF03.md), [RNF04](rnf/RNF04.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md) |
| [RF07](requisitos/RF07.md) | Consultar alunos de uma turma | Detalhado | 4, Tem que ter | MVP | [RN24](regras_de_negocio.md#rn24) | [RNF01](rnf/RNF01.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md) |

### CP2: Registro de doações e prestação de contas

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF08](requisitos/RF08.md) | Registrar doação recebida | Rascunho | 1, Não precisa ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF09](requisitos/RF09.md) | Editar doação recebida | Rascunho | 1, Não precisa ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF10](requisitos/RF10.md) | Registrar documentos de prestação de contas | Rascunho | 1, Não precisa ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF11](requisitos/RF11.md) | Editar documentos de prestação de contas | Rascunho | 1, Não precisa ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF12](requisitos/RF12.md) | Consultar doações e prestações de contas | Rascunho | 1, Não precisa ter | Pós-MVP | - | [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |

### CP3: Gestão de conteúdo institucional

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF13](requisitos/RF13.md) | Publicar conteúdo institucional | Detalhado | 4, Tem que ter | MVP | [RN25](regras_de_negocio.md#rn25), [RN26](regras_de_negocio.md#rn26), [RN27](regras_de_negocio.md#rn27) | [RNF01](rnf/RNF01.md), [RNF02](rnf/RNF02.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md) |
| [RF14](requisitos/RF14.md) | Editar conteúdo institucional | Detalhado | 3, Deveria ter | MVP | [RN25](regras_de_negocio.md#rn25), [RN26](regras_de_negocio.md#rn26), [RN28](regras_de_negocio.md#rn28) | [RNF01](rnf/RNF01.md), [RNF02](rnf/RNF02.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md), [RNF10](rnf/RNF10.md) |
| [RF15](requisitos/RF15.md) | Consultar conteúdo institucional | Detalhado | 4, Tem que ter | MVP | [RN29](regras_de_negocio.md#rn29) | [RNF02](rnf/RNF02.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md) |
| [RF16](requisitos/RF16.md) | Remover conteúdo institucional | Detalhado | 4, Tem que ter | MVP | [RN26](regras_de_negocio.md#rn26), [RN30](regras_de_negocio.md#rn30) | [RNF02](rnf/RNF02.md), [RNF05](rnf/RNF05.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md), [RNF10](rnf/RNF10.md) |
| [RF17](requisitos/RF17.md) | Publicar evento | Detalhado | 3, Deveria ter | MVP | [RN26](regras_de_negocio.md#rn26), [RN31](regras_de_negocio.md#rn31), [RN32](regras_de_negocio.md#rn32), [RN33](regras_de_negocio.md#rn33) | [RNF01](rnf/RNF01.md), [RNF02](rnf/RNF02.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md) |
| [RF18](requisitos/RF18.md) | Editar evento | Detalhado | 3, Deveria ter | MVP | [RN26](regras_de_negocio.md#rn26), [RN31](regras_de_negocio.md#rn31), [RN34](regras_de_negocio.md#rn34) | [RNF01](rnf/RNF01.md), [RNF02](rnf/RNF02.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md), [RNF10](rnf/RNF10.md) |
| [RF19](requisitos/RF19.md) | Remover evento | Detalhado | 3, Deveria ter | MVP | [RN26](regras_de_negocio.md#rn26), [RN30](regras_de_negocio.md#rn30) | [RNF02](rnf/RNF02.md), [RNF05](rnf/RNF05.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md), [RNF10](rnf/RNF10.md) |
| [RF20](requisitos/RF20.md) | Consultar eventos | Detalhado | 3, Deveria ter | MVP | [RN33](regras_de_negocio.md#rn33) | [RNF02](rnf/RNF02.md), [RNF07](rnf/RNF07.md), [RNF09](rnf/RNF09.md) |

### CP4: Cadastro e histórico de alunos

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF21](requisitos/RF21.md) | Cadastrar aluno | Detalhado | 4, Tem que ter | MVP | [RN35](regras_de_negocio.md#rn35), [RN36](regras_de_negocio.md#rn36), [RN37](regras_de_negocio.md#rn37), [RN38](regras_de_negocio.md#rn38), [RN39](regras_de_negocio.md#rn39), [RN40](regras_de_negocio.md#rn40) | [RNF01](rnf/RNF01.md), [RNF03](rnf/RNF03.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF22](requisitos/RF22.md) | Editar aluno | Detalhado | 4, Tem que ter | MVP | [RN41](regras_de_negocio.md#rn41), [RN42](regras_de_negocio.md#rn42), [RN43](regras_de_negocio.md#rn43) | [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF23](requisitos/RF23.md) | Consultar ficha do aluno | Detalhado | 4, Tem que ter | MVP | [RN44](regras_de_negocio.md#rn44), [RN45](regras_de_negocio.md#rn45), [RN46](regras_de_negocio.md#rn46) | [RNF01](rnf/RNF01.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF24](requisitos/RF24.md) | Inativar aluno | Detalhado | 3, Deveria ter | MVP | [RN01](regras_de_negocio.md#rn01), [RN47](regras_de_negocio.md#rn47), [RN48](regras_de_negocio.md#rn48) | [RNF03](rnf/RNF03.md), [RNF04](rnf/RNF04.md), [RNF05](rnf/RNF05.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF25](requisitos/RF25.md) | Remover dados do aluno | Rascunho | 1, Não precisa ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF05](rnf/RNF05.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |

### CP5: Acompanhamento pedagógico e disciplinar do aluno

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF26](requisitos/RF26.md) | Registrar frequência | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF27](requisitos/RF27.md) | Consultar frequência | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF28](requisitos/RF28.md) | Emitir alerta de faltas críticas | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF29](requisitos/RF29.md) | Registrar medida disciplinar | Rascunho | 3, Deveria ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF05](rnf/RNF05.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |

### CP6: Comunicação com voluntários e famílias

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF30](requisitos/RF30.md) | Publicar aviso | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF03](rnf/RNF03.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF31](requisitos/RF31.md) | Consultar avisos | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF06](rnf/RNF06.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF32](requisitos/RF32.md) | Editar aviso | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
| [RF33](requisitos/RF33.md) | Remover aviso | Rascunho | 2, Poderia ter | Pós-MVP | - | - |
| [RF34](requisitos/RF34.md) | Consultar histórico de avisos | Rascunho | 1, Não precisa ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF06](rnf/RNF06.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |

### CP7: Matrícula online

| Código | Requisito | Estado | MoSCoW | Entrega | RNs | RNFs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RF35](requisitos/RF35.md) | Acessar formulário de matrícula online | Rascunho | 4, Tem que ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF02](rnf/RNF02.md), [RNF09](rnf/RNF09.md) |
| [RF36](requisitos/RF36.md) | Preencher dados do aluno | Rascunho | 4, Tem que ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF03](rnf/RNF03.md), [RNF13](rnf/RNF13.md) |
| [RF37](requisitos/RF37.md) | Informar dados do responsável legal | Rascunho | 3, Deveria ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF03](rnf/RNF03.md), [RNF13](rnf/RNF13.md) |
| [RF38](requisitos/RF38.md) | Registrar consentimento de dados pessoais | Rascunho | 4, Tem que ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF10](rnf/RNF10.md), [RNF13](rnf/RNF13.md) |
| [RF39](requisitos/RF39.md) | Registrar termo de uso de imagem | Rascunho | 4, Tem que ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF10](rnf/RNF10.md), [RNF13](rnf/RNF13.md) |
| [RF40](requisitos/RF40.md) | Informar pessoas autorizadas a retirar o aluno | Rascunho | 2, Poderia ter | Pós-MVP | - | [RNF01](rnf/RNF01.md), [RNF03](rnf/RNF03.md), [RNF13](rnf/RNF13.md) |
| [RF41](requisitos/RF41.md) | Emitir comprovante de solicitação | Rascunho | 3, Deveria ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF06](rnf/RNF06.md) |
| [RF42](requisitos/RF42.md) | Analisar solicitações de matrícula | Rascunho | 3, Deveria ter | Pós-MVP | - | [RNF03](rnf/RNF03.md), [RNF05](rnf/RNF05.md), [RNF10](rnf/RNF10.md), [RNF11](rnf/RNF11.md), [RNF13](rnf/RNF13.md) |
