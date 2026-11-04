# SigCECP: documentação de requisitos

Site de documentação feito com MkDocs (tema Material). O escopo do projeto (requisitos, regras de negócio, decisões, pendências e cronograma) é lido em um único lugar: o **Painel do escopo** (`docs/painel.md`).

## Princípio

**Cada informação mora em um só arquivo, e o painel apenas mostra.** Por isso, para mudar qualquer coisa do escopo, edite a **fonte** e nunca o painel. O que o painel calcula sozinho (vínculos entre itens, pendências, alertas, progresso) não precisa ser escrito por ninguém.

## De onde vêm os dados

O gerador (`tools/gen_escopo.py`) lê apenas estes arquivos de `docs/`:

| Fonte | O que o painel tira dela | Onde aparece |
| :--- | :--- | :--- |
| `visao/escopo/requisitos/RF*.md` (uma ficha por requisito) | estado, CP, ator, declaração, MoSCoW, MVP ou pós-MVP, critérios, regras e RNFs citados, entradas, pré-condições, processamento, saídas, andamento, marcações `[PENDENTE]` | aba Requisitos e ficha lateral |
| `visao/escopo/regras_de_negocio.md` | texto de cada regra (RN) | aba Regras e RNFs |
| `visao/escopo/rnf/RNF*.md` | nome, descrição e critério de cada RNF | aba Regras e RNFs |
| `visao/escopo/decisoes.md` | decisões, pendências abertas e pendências encerradas | aba Decisões e pendências |
| `cronograma/6_cronograma.md` | período, foco, entregas e RFs previstos de cada iteração, e o critério de transição | aba Cronograma |

O gerador também verifica se existe `visao/escopo/pdf/RFxx.pdf`, só para mostrar o link do protótipo na ficha lateral. Ele grava um único arquivo, `docs/assets/escopo.js`, que é **gerado: não edite**.

## O que o painel calcula sozinho

- Quais decisões e pendências citam cada requisito, e em qual iteração ele está.
- Quais requisitos usam cada regra de negócio e cada RNF.
- A caixa "O que falta" de cada requisito (marcações `[PENDENTE]`, pendências abertas ligadas a ele, ficha de MVP ainda em rascunho).
- A barra de progresso do MVP (etapas concluídas do andamento).
- A aba Alertas: regra citada que não existe, RF de MVP fora do cronograma, RF pós-MVP agendado e decisão sem data ou fonte.

## Como atualizar (tarefas comuns)

1. **Mudar o estado de um requisito** (por exemplo, validar): na ficha, altere a linha `Estado e versão` (valores: `Rascunho`, `Detalhado`, `Validado`, seguidos da versão) e acrescente uma linha na tabela `Histórico de mudanças` da própria ficha, citando a ata ou a decisão.
2. **Atualizar o andamento**: na tabela `Andamento` da ficha, escreva o status começando por `Feito`, `Em Andamento` ou `Pendente`.
3. **Registrar uma decisão**: acrescente uma linha na tabela de decisões de `decisoes.md` (ID, data, decisão, RFs afetados, fonte). Informe a data e a fonte (ata) para não gerar alerta.
4. **Abrir uma pendência**: acrescente uma linha na tabela de pendências de `decisoes.md`, com os RFs afetados e o próximo passo.
5. **Encerrar uma pendência**: mova a linha para `Pendências encerradas` e diga como foi resolvida. Não apague: o histórico é parte do escopo.
6. **Mudar prioridade ou entrega**: na ficha, ajuste o campo `Valor de negócio (MoSCoW)`. Se o requisito for pós-MVP, o texto deve conter `Pós-MVP`; caso contrário, é tratado como MVP.
7. **Mudar o cronograma**: edite a tabela de `6_cronograma.md`. Os RFs previstos de cada iteração vão na coluna `Requisitos previstos`, no formato `RF13, RF14`. Registre a mudança na tabela de versionamento.
8. **Criar um requisito novo**: copie uma ficha existente, troque o código e o título (`### RF44: Nome`), preencha os campos e mantenha os nomes deles. Inclua a ficha no cronograma se for MVP.
9. **Criar uma regra ou um RNF**: regra nova é uma linha em `regras_de_negocio.md`, com a âncora `<a id="rn52"></a>` e o código `**RN52**`. RNF novo é um arquivo `rnf/RNFxx.md` copiado de outro. Cite o código na ficha do requisito afetado.

## Formato que o gerador exige

- Códigos sempre assim: `RF13`, `RN25`, `RNF05`, `DEC03`, `PEN04`.
- Fichas com título `### RFxx: Nome` e a tabela inicial com os campos `Estado e versão`, `CP de origem`, `Ator principal`, `Declaração`, `Valor de negócio (MoSCoW)`, `Critérios de aceitação`, `Regras de negócio`, `RNFs aplicáveis`, `Entradas`, `Pré-condições`, `Processamento` e `Saídas`, e a seção `#### Andamento`.
- `decisoes.md` com as seções `## Pendências` e `## Pendências encerradas`.
- Iterações do cronograma em linhas que começam com `**Iteração`.

Se mudar o nome de um campo ou de uma seção, é preciso mudar o `tools/gen_escopo.py` junto.

## Como rodar

```bash
pip install mkdocs-material   # mais os plugins já usados no mkdocs.yml
mkdocs serve                  # abre em http://127.0.0.1:8000/painel/
```

Antes de cada `mkdocs serve`, `build` ou `gh-deploy`, o hook `tools/mkdocs_hook.py` roda o gerador sozinho. Para rodar só o gerador: `python tools/gen_escopo.py`.

## Se algo der errado

- **O build falha com erro de Python**: alguma ficha ou tabela saiu do formato. A mensagem mostra o arquivo e a linha. Compare com uma ficha que funciona.
- **O painel não mudou**: confira se você editou a fonte (e não o `escopo.js`) e recarregue com Ctrl+Shift+R.
- **Apareceu um alerta**: ele diz o que corrigir e onde. Corrigindo a fonte, o alerta some no próximo build.

## Estrutura dos arquivos do painel

| Arquivo | Função | Editar? |
| :--- | :--- | :--- |
| `tools/gen_escopo.py` | lê as fontes e gera os dados | só se o formato mudar |
| `tools/mkdocs_hook.py` | roda o gerador antes de cada build | não |
| `docs/assets/escopo.js` | dados gerados | **nunca** |
| `docs/assets/painel.js` e `painel.css` | tela do painel | só para mudar o visual |
| `docs/painel.md` | página que carrega o painel | raramente |