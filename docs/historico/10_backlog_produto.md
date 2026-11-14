# 10 Escopo de Produto

## 10.1 Escopo Geral

A especificação vigente dos requisitos está nas fichas individuais, reunidas no [painel do escopo](../painel.md). Declaração, entradas, regras, critérios de aceitação e andamento devem ser atualizados na ficha; este backlog não mantém critérios de aceitação independentes.

Para o cadastro de alunos, consulte o [RF21](../visao/escopo/requisitos/RF21.md): seus campos obrigatórios e documentos entregáveis posteriormente seguem a ficha e as RN35 a RN40. A lista antiga de documentação não deve ser usada para exigir todos os anexos no ato do cadastro. A [ata de 22/09, seção 4](organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_22_09.md) já descreve o questionário usado enquanto o atestado não foi entregue; a RN39 e os critérios atuais da ficha permitem concluir o cadastro com documentos faltantes.

## 10.2 Priorização do Escopo Geral e MVP

A priorização combinou dois modelos: o MoSCoW (Must, Should, Could e Won't have), usado para o valor de negócio e avaliado com o cliente, e a pontuação de esforço técnico atribuída pela equipe (esforço, complexidade e lacuna de capacidade). Os dois critérios orientam o desenvolvimento de acordo com os objetivos do projeto e formam a matriz 4 × 4 da seção 10.2.2.
 
O MVP é o conjunto mínimo de funcionalidades que permite lançar o produto e colocá-lo em uso pelo cliente, com foco nos requisitos essenciais para validar o valor de negócio. Na matriz final (seção 10.2.2), o MVP reúne os RFs com valor de negócio 3 ou 4 e esforço técnico 1 ou 2: 18 dos 43 requisitos.

### 10.2.1 Critérios de priorização

**Esforço técnico:** avaliado pela equipe em três dimensões, todas orientadas no mesmo sentido (maior nota, maior dificuldade).

| Pontuação | Esforço | Complexidade | Lacuna de capacidade da equipe |
|:---:|---|---|---|
| 1 | Até 2 horas | Solução conhecida, com poucas dependências | A equipe domina plenamente o necessário |
| 2 | Entre 2 e 5 horas | Exige alguma investigação ou integração | Conhecimento suficiente, com pouca aprendizagem adicional |
| 3 | Entre 5 e 8 horas | Várias dependências ou incertezas técnicas | A equipe precisa desenvolver conhecimentos relevantes |
| 4 | Mais de 8 horas | Elevada incerteza, integração crítica ou tecnologia não dominada | A equipe ainda não possui os conhecimentos ou recursos |

**Como calcular:** ET = (Esforço + Complexidade + Lacuna) / 3. Para posicionar o RF na matriz, o ET é arredondado para o inteiro mais próximo.

**Valor de negócio (MoSCoW):** avaliado com o cliente, com a escala abaixo.

| Pontuação | Classificação | Interpretação |
|:---:|---|---|
| 4 | Tem que ter (Must have) | Indispensável para resolver o problema central ou viabilizar o produto |
| 3 | Deveria ter (Should have) | Muito importante, mas o produto pode operar temporariamente sem o requisito |
| 2 | Poderia ter (Could have) | Agrega valor, mas pode ser adiado sem comprometer o objetivo principal |
| 1 | Não precisa ter (Won't have now) | Não é prioritário para a versão atual |

### 10.2.2 Matriz 4 × 4

![Matriz 4x4](../visao/img/matriz4x4.jpeg)


**Índice de prioridade**

- **Alto (MVP):** valor de negócio 3 ou 4 e esforço técnico 1 ou 2. São 18 dos 43 RFs.
- **Valor alto, esforço alto:** valor 3 ou 4 e esforço 3 ou 4. Ficam fora do MVP e pedem avaliar a viabilidade ou o contexto (RF29, RF35 a RF39, RF41 e RF42).
- **Médio:** valor de negócio 2 (moderado), com qualquer esforço.
- **Baixo:** valor de negócio 1.

A coluna "Prior." ordena os índices: 1 (Alto), 2 (valor alto, esforço alto), 3 (Médio) e 4 (Baixo).

!!! info "Registro da matriz de 30/10/2026"
    A imagem e a tabela abaixo preservam a composição aprovada nessa data (DEC03). Não são outra especificação dos requisitos: os links levam às fichas vigentes. Alterações futuras de prioridade e entrega devem ser registradas nas fichas e nas decisões, preservando este retrato histórico. As 30 divergências entre ET calculado e esforço na matriz continuam abertas na PEN06; esta revisão não recalcula notas nem apresenta a reconciliação como concluída.

A classificação e a entrega atuais são consultadas no [painel](../painel.md). Registro da matriz:

| Código | Índice | Prior. | MVP |
|---|:---:|:---:|:---:|
| [RF02](../visao/escopo/requisitos/RF02.md) | Alto | 1 | ✔ |
| [RF07](../visao/escopo/requisitos/RF07.md) | Alto | 1 | ✔ |
| [RF15](../visao/escopo/requisitos/RF15.md) | Alto | 1 | ✔ |
| [RF16](../visao/escopo/requisitos/RF16.md) | Alto | 1 | ✔ |
| [RF22](../visao/escopo/requisitos/RF22.md) | Alto | 1 | ✔ |
| [RF00](../visao/escopo/requisitos/RF00.md) | Alto | 1 | ✔ |
| [RF03](../visao/escopo/requisitos/RF03.md) | Alto | 1 | ✔ |
| [RF17](../visao/escopo/requisitos/RF17.md) | Alto | 1 | ✔ |
| [RF18](../visao/escopo/requisitos/RF18.md) | Alto | 1 | ✔ |
| [RF19](../visao/escopo/requisitos/RF19.md) | Alto | 1 | ✔ |
| [RF20](../visao/escopo/requisitos/RF20.md) | Alto | 1 | ✔ |
| [RF23](../visao/escopo/requisitos/RF23.md) | Alto | 1 | ✔ |
| [RF14](../visao/escopo/requisitos/RF14.md) | Alto | 1 | ✔ |
| [RF01](../visao/escopo/requisitos/RF01.md) | Alto | 1 | ✔ |
| [RF21](../visao/escopo/requisitos/RF21.md) | Alto | 1 | ✔ |
| [RF06](../visao/escopo/requisitos/RF06.md) | Alto | 1 | ✔ |
| [RF24](../visao/escopo/requisitos/RF24.md) | Alto | 1 | ✔ |
| [RF13](../visao/escopo/requisitos/RF13.md) | Alto | 1 | ✔ |
| [RF35](../visao/escopo/requisitos/RF35.md) | Valor alto, esforço alto | 2 | — |
| [RF36](../visao/escopo/requisitos/RF36.md) | Valor alto, esforço alto | 2 | — |
| [RF29](../visao/escopo/requisitos/RF29.md) | Valor alto, esforço alto | 2 | — |
| [RF37](../visao/escopo/requisitos/RF37.md) | Valor alto, esforço alto | 2 | — |
| [RF39](../visao/escopo/requisitos/RF39.md) | Valor alto, esforço alto | 2 | — |
| [RF38](../visao/escopo/requisitos/RF38.md) | Valor alto, esforço alto | 2 | — |
| [RF42](../visao/escopo/requisitos/RF42.md) | Valor alto, esforço alto | 2 | — |
| [RF41](../visao/escopo/requisitos/RF41.md) | Valor alto, esforço alto | 2 | — |
| [RF04](../visao/escopo/requisitos/RF04.md) | Médio | 3 | — |
| [RF05](../visao/escopo/requisitos/RF05.md) | Médio | 3 | — |
| [RF27](../visao/escopo/requisitos/RF27.md) | Médio | 3 | — |
| [RF30](../visao/escopo/requisitos/RF30.md) | Médio | 3 | — |
| [RF31](../visao/escopo/requisitos/RF31.md) | Médio | 3 | — |
| [RF32](../visao/escopo/requisitos/RF32.md) | Médio | 3 | — |
| [RF33](../visao/escopo/requisitos/RF33.md) | Médio | 3 | — |
| [RF40](../visao/escopo/requisitos/RF40.md) | Médio | 3 | — |
| [RF26](../visao/escopo/requisitos/RF26.md) | Médio | 3 | — |
| [RF28](../visao/escopo/requisitos/RF28.md) | Médio | 3 | — |
| [RF25](../visao/escopo/requisitos/RF25.md) | Baixo | 4 | — |
| [RF12](../visao/escopo/requisitos/RF12.md) | Baixo | 4 | — |
| [RF34](../visao/escopo/requisitos/RF34.md) | Baixo | 4 | — |
| [RF08](../visao/escopo/requisitos/RF08.md) | Baixo | 4 | — |
| [RF09](../visao/escopo/requisitos/RF09.md) | Baixo | 4 | — |
| [RF11](../visao/escopo/requisitos/RF11.md) | Baixo | 4 | — |
| [RF10](../visao/escopo/requisitos/RF10.md) | Baixo | 4 | — |

As notas do cliente e da equipe, os votos individuais e o cálculo que levaram aos resultados acima estão registrados em [Comprovação de Evidência](priorizacao_geral_e_mvp.md). 
## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Documento incial do item 10 | [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.1 | 30/10/2026 | Matriz 4 × 4 final: MVP redefinido para 18 RFs e índice "valor alto, esforço alto" incluído | [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.2 | 14/11/2026 | Issue #35: critérios de aceitação centralizados nas fichas, referência ao RF21 vigente e matriz delimitada como registro de 30/10; PEN06 preservada | Renato Gameiro | Pendente |
