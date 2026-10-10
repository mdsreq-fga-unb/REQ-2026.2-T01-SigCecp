# 9 DoR e DoD
 
## 9.1 Definition of Ready (DoR)
 
O **Definition of Ready (DoR)** é o conjunto de critérios que um requisito deve atender antes de entrar em uma iteração (sprint). Ele é verificado na Reunião de Planejamento, garantindo que a equipe compreenda o que será feito, como será realizado e quais critérios de aceitação devem ser cumpridos.
 
| # | Critério | Métrica de Verificação |
|---|---|---|
| 1 | O requisito deve estar no nível de maturidade de produto | O requisito atende às características de um requisito de produto (ISO/IEC/IEEE 29148). Ele deve ser necessário, inequívoco, completo, singular, viável, verificável, rastreável, conforme |
| 2 | O protótipo deve ser validado pelo cliente | Registro formal da validação do cliente e reunião gravada |
| 3 | O requisito está dimensionado para uma única sprint | Estimativa de esforço definido pela equipe deve ser menor que ou igual a quantidade de horas da sprint |
| 4 | O requisito não possui dependência blocante com outro requisito | Quando houver dependências, o requisito bloquenate deve estar como concluído |

 
## 9.2 Definition of Done (DoD)
 
O **Definition of Done (DoD)** é o conjunto de critérios que uma tarefa deve atender para ser considerada concluída. Um requisito que não cumpra todos os critérios não é apresentado na reunião de validação com o cliente. Vale ressaltar que para uma entrega ser validada, ela deve ser conferida com esses critérios pelo autor e por ao menos um revisor.
 
| # | Critério | Métrica de Verificação |
|---|---|---|
| 1 | Ter uma switch de teste unitários que cubra 80% das funções | Ao rodar a switch de testes unitários deve ter 100% de aprovação |
| 2 | Pipeline de CI para a switch de testes | Github Actions executa para cada PR |
| 3 | Aprovação do user design pelo cliente | Reunião de validação com o stakeholder |
| 4 | A funcionalidade deve ser entregue por completo | Durante o teste em ambiente de homologação, todos os critérios de aceitação da funcionalidade devem estar presentes |
| 5 | A funcionalidade está documentada | A forma de uso da funcionalidade deve estar documentada |
| 6 | A entrega contribui para o incremento do produto | A funcionalidade desenvolvida deve resolver um problema ou adicionar uma nova forma de interagir com o produto, agregando valor a ele |
| 7 | O código está de acordo com os padrões de escrita | O código deve seguir o padrão PEP 8 |

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 10/10/2026 | Apenas escrita do documento inicial, os critérios foram definidos na reunião: | [Rafael Melatti](https://github.com/Romm-0) |  |