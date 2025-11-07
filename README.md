# task-brain

Projeto contendo os diagramas e datasets utilizados para treinamento do Modelo de Organização de Tarefas da IA4s

## Como estou treinando esse modelo ?

Estou usando o Auto Train da hugging face

https://huggingface.co/spaces/IA4S/task-brain

Vou usar os seguintes [datasets](dataSets) contendo perguntas e respostas: 

Ex : 

```
{"instruction":"Minha rotina é das 08h às 17h. Preciso encaixar a tarefa de revisar minhas finanças pessoais esta semana. Como posso organizar?", "response":"Sua rotina tem espaço após o trabalho e no sábado de manhã. Coloque 30 minutos por dia, de segunda a quinta, às 19h. Pequenas revisões são melhores do que uma maratona. Isso melhora sua clareza financeira sem pesar na agenda."}
{"instruction":"Trabalho das 9h às 18h. Quero começar a estudar inglês, mas nunca acho tempo. Como encaixar isso?", "response":"Seu dia tem espaço depois das 20h ou no início da manhã. Comece com 20 minutos três vezes por semana. Pouco e constante funciona melhor. Isso aproxima você de mais oportunidades profissionais."}
{"instruction":"Minha semana está cheia. Tenho academia segunda e quarta, trabalho pesado e ainda quero organizar minha casa. Sugere algo?", "response":"Você pode usar 15 minutos por dia para pequenas arrumações. Não precisa ser tudo de uma vez. Escolha um cômodo por semana. Pequenos avanços acumulam."}
```

Diagrama funcional da lógica e raciocínio implementada para esse modelo : 

<img width="2589" height="1701" alt="image" src="https://github.com/user-attachments/assets/f86dfbbf-757b-420f-8ca0-fd412d2860f8" />

