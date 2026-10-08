# Declaração de Requisitos no SigCecp

> Análise da Equipe One sobre os tipos de declaração, os níveis de abstração e os momentos do processo.

---

## 1. Níveis de abstração

A seguir, todos os requisitos do projeto foram classificados entre os seguintes níveis de abstração:

- Requisitos de Negócio;
- Requisitos de Usuário;
- Requisitos de Produto.

### 1.1 Requisitos funcionais

| ID | Nível predominante | Momento |
| -- | ------------------ | ------- |
| RF00 | Usuário | Sustentar avaliação |
| RF01 | Usuário | Exploratório |
| RF02 | Produto | Orientar desenvolvimento |
| RF03 | Usuário | Orientar desenvolvimento |
| RF04 | Usuário | Exploratório |
| RF05 | Usuário | Orientar desenvolvimento |
| RF06 | Usuário | Orientar desenvolvimento |
| RF07 | Usuário | Exploratório |
| RF08 | Usuário | Orientar desenvolvimento |
| RF09 | Usuário | Exploratório |
| RF10 | Usuário | Orientar desenvolvimento |
| RF11 | Usuário | Exploratório |
| RF12 | Usuário | Orientar desenvolvimento |
| RF13 | Usuário | Orientar desenvolvimento |
| RF14 | Usuário | Orientar desenvolvimento |
| RF15 | Usuário | Orientar desenvolvimento |
| RF16 | Usuário | Exploratório |
| RF17 | Usuário | Orientar desenvolvimento |
| RF18 | Usuário | Exploratório |
| RF19 | Usuário | Exploratório |
| RF20 | Usuário | Exploratório |
| RF21 | Usuário | Orientar desenvolvimento |
| RF22 | Usuário | Orientar desenvolvimento |
| RF23 | Usuário | Orientar desenvolvimento |
| RF24 | Usuário | Orientar desenvolvimento |
| RF25 | Usuário | Sustentar avaliação |
| RF26 | Usuário | Orientar desenvolvimento |
| RF27 | Usuário | Exploratório |
| RF28 | Produto | Sustentar avaliação |
| RF29 | Usuário | Orientar desenvolvimento |
| RF30 | Usuário | Exploratório |
| RF31 | Usuário | Orientar desenvolvimento |
| RF32 | Usuário | Orientar desenvolvimento |
| RF33 | Usuário | Orientar desenvolvimento |
| RF34 | Usuário | Orientar desenvolvimento |
| RF35 | Usuário | Orientar desenvolvimento |
| RF36 | Usuário | Orientar desenvolvimento |
| RF37 | Usuário | Orientar desenvolvimento |
| RF38 | Usuário | Sustentar avaliação |
| RF39 | Usuário | Orientar desenvolvimento |
| RF40 | Usuário | Orientar desenvolvimento |
| RF41 | Produto | Orientar desenvolvimento |
| RF42 | Usuário | Orientar desenvolvimento |

### 1.2 Requisitos não funcionais

| ID | Nível predominante | Momento |
| -- | ------------------ | ------- |
| RNF01 | Produto | Sustentar avaliação |
| RNF02 | Produto | Sustentar avaliação |
| RNF03 | Produto | Sustentar avaliação |
| RNF04 | Produto | Sustentar avaliação |
| RNF05 | Produto | Sustentar avaliação |
| RNF06 | Produto | Sustentar avaliação |
| RNF07 | Produto | Sustentar avaliação |
| RNF08 | Produto | Sustentar avaliação |
| RNF09 | Produto | Sustentar avaliação |
| RNF10 | Produto | Sustentar avaliação |
| RNF11 | Produto | Sustentar avaliação |
| RNF12 | Produto | Sustentar avaliação |
| RNF13 | Negócio | Orientar desenvolvimento |

Alguns requisitos de usuário apresentaram trechos que comumente são associados a outros níveis de abstração, por exemplo os Requisitos Funcionais RF05, RF06, RF22 e RF24, em que a tarefa é do usuário, mas "preservando o histórico" é uma restrição de produto.

---

## 2. Tipos de declaração utilizados

| Grupo de requisitos | Nível predominante | Tipo de declaração usado | Forma/estrutura observada |
| ------------------- | ------------------ | ------------------------ | ------------------------- |
| RFs | Usuário | Narrativa descritiva | Lista de requisitos declarados em textos curtos em linguagem natural |
| RNFs | Produto | Declaração estruturada com critério de aceitação | Tabela de requisitos declarados com textos curtos e critérios de aceitação |

É possível melhorar o tipo de declaração dos requisitos para evitar ambiguidade. Os RFs, por exemplo, não trazem critério de aceitação nem prioridade, enquanto os RNFs sim, tornando-os mais completos, portanto menos ambíguos. Ainda assim, até o momento os dois tipos utilizados cobrem de modo suficiente os níveis de abstração predominantes.

---

## 3. Momentos do produto e necessidade de uso

O momento de um requisito não é uma fase rígida de amadurecimento. Ele depende do entendimento disponível sobre o requisito e da finalidade para a qual a declaração será usada. Por isso, em um mesmo produto, requisitos diferentes podem estar em momentos diferentes, e isso se torna perceptível na forma como cada requisito é declarado.

Foram considerados três momentos:

- **Exploratório:** a declaração diz apenas a ação sobre o objeto, sem detalhar dados, condições ou resultados, e serve para sustentar a conversa com os stakeholders.
- **Orientar desenvolvimento:** a declaração já traz informações compreendidas como relevantes (dados a informar, regras, quem pode fazer), que ajudam a implementar o requisito.
- **Sustentar avaliação:** a declaração traz condições e resultados que permitem verificar se o requisito foi atendido.

| Momento | RFs | RNFs |
| ------- | --- | ---- |
| Exploratório | 11 | 0 |
| Orientar desenvolvimento | 28 | 1 |
| Sustentar avaliação | 4 | 12 |

A maioria dos RFs encontra-se no momento de orientar o desenvolvimento, pois além de dizer o que o requisito faz, já traz informações que ajudam a implementá-lo (por exemplo, o RF03 informa que a turma é cadastrada com modalidade, horário e capacidade máxima). Alguns RFs, como o RF07 e o RF20, estão mais próximos do momento exploratório, por serem frases curtas que ainda não detalham o comportamento esperado.

Os RNFs, em sua maioria, estão no momento de sustentar avaliação, pois possuem critérios de aceitação mensuráveis (por exemplo, P95 ≤ 3s no RNF06).

Portanto, o projeto cobre os três momentos, em partes diferentes da documentação.

---

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| ------ | ---- | --------- | ------------ | -------------- |
| 1.0 | 07/10/2026 | Anotações da atividade para o dia 08/10 | Ana Paula Jardim | - |