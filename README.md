# task-brain

Projeto contendo os diagramas e datasets utilizados para treinamento do Modelo de Organização de Tarefas da IA4s

## Como estou treinando esse modelo ?

Estou usando o [Auto Train](https://huggingface.co/autotrain) da hugging face

#### Space do Projeto na Hugging Face : 

https://huggingface.co/spaces/IA4S/task-brain

Vou usar os seguintes [datasets](dataSets) contendo instruções, inputs e respostas conforme os cenarios diversos variando:

- Perfil -> Ex: estudantes, CLT, empreendedores
- Periodos -> manhã livre, noite livre, carga pesada
-  Objetivos -> metas de saúde / carreira / família
- Quando faltam informações → o modelo pergunta
- Quando horários não fazem sentido → o modelo reorganiza
- Automação total com subtarefas, recorrência, agenda, lembretes

Ex : 

```json
{"instruction":"Organize meu dia de hoje para estudar melhor.","input":"Sou estudante, tenho a manhã livre. Quero melhorar minhas notas em matemática e redação. Tenho prova na sexta.","output":"Para melhorar seu desempenho, priorize revisão e prática. Sugestão:\n1. 09:00–10:00 → Revisar conteúdo da última aula de matemática\n2. 10:00–10:45 → Resolver listas anteriores\n3. 10:45–11:00 → Pausa\n4. 11:00–12:00 → Redação: estrutura e treino\nPremissas: manhã livre, prova próxima. Riscos: faltar material ou distrações.\nAções:\n✅ Criar tarefa: 'Revisar matemática hoje 9h'\n✅ Criar tarefa: 'Treinar redação 11h'\n✅ Criar lembrete: 'Separar material antes de dormir'\nQuer automatizar como recorrente até sexta?"}
{"instruction":"Organize minhas tarefas do trabalho.","input":"Sou empreendedor, preciso cuidar de vendas, responder clientes e revisar propostas hoje.","output":"Para organizar, preciso saber disponibilidade de horários e urgência de cada tarefa. Pode informar quanto tempo tem livre hoje e quais prazos são críticos? Exemplo: 'Tenho a tarde livre e preciso responder clientes até 17h'."}
{"instruction":"Monte minha agenda de amanhã.","input":"Trabalho CLT das 8h às 18h. Tenho academia às 17h e estudo inglês às 19h.","output":"Seu horário da academia está dentro do expediente, o que conflita com seu trabalho. Proposta otimizada:\n✅ 06:30–07:15 → Academia\n✅ 08:00–18:00 → Trabalho\n✅ 19:00–20:00 → Estudo de inglês\nRiscos: acordar cedo exige dormir mais cedo.\nAções sugeridas:\n- Criar lembrete recorrente 'Academia 6h30 todos os dias úteis'\n- Criar tarefa 'Estudo de inglês 19h – aulas + vocabulário'"}
{"instruction":"Quero melhorar minha produtividade no negócio.","input":"Sou empreendedor, tenho meta de aumentar faturamento. Toda segunda eu preciso planejar a semana, toda sexta analisar relatórios.","output":"Sugestão de automação:\n- Criar tarefa recorrente: Segunda 09h 'Planejamento da semana – leads, conteúdo, orçamento'\n- Criar tarefa recorrente: Sexta 16h 'Análise de relatórios – vendas, CAC, ROI'\n- Subtarefas fixas: atualizar planilha, revisar anúncios, responder leads qualificados.\nPremissas: rotina semanal e objetivo de faturamento.\nRiscos: não medir indicadores e perder prioridades."}
```

Diagrama funcional da lógica e raciocínio implementada para esse modelo : 

<img width="2589" height="1701" alt="image" src="https://github.com/user-attachments/assets/f86dfbbf-757b-420f-8ca0-fd412d2860f8" />

