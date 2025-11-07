# Script completo para treinar no Google Colab

# 1. Instalar dependências
!pip install autotrain-advanced pandas

# 2. Fazer login no Hugging Face
from huggingface_hub import login
login()  # Será solicitado o token interativamente

# 3. Criar dataset CSV a partir do JSON
import pandas as pd
import json

# Dataset de treinamento
dataset = [
    {"text": "### Instrução:\nOrganize meu dia de hoje para estudar melhor.\n\n### Entrada:\nSou estudante, tenho a manhã livre. Quero melhorar minhas notas em matemática e redação. Tenho prova na sexta.\n\n### Resposta:\nPara melhorar seu desempenho, priorize revisão e prática. Sugestão:\n1. 09:00–10:00 Revisar conteúdo\n2. 10:00–10:45 Listas de exercícios\n3. 11:00–12:00 Treino de redação\nPremissas: manhã livre, prova próxima.\nAções: criar tarefas e lembretes. Deseja recorrência até sexta?"},
    {"text": "### Instrução:\nOrganize minhas tarefas do trabalho.\n\n### Entrada:\nSou empreendedor, preciso cuidar de vendas, responder clientes e revisar propostas hoje.\n\n### Resposta:\nPara organizar preciso saber sua disponibilidade. Quanto tempo tem livre hoje e algum prazo crítico? Ex: preciso responder clientes até 17h."},
    {"text": "### Instrução:\nMonte minha agenda de amanhã.\n\n### Entrada:\nTrabalho CLT das 8h às 18h. Tenho academia às 17h e estudo inglês às 19h.\n\n### Resposta:\nA academia conflita com o expediente. Sugestão: 06:30–07:15 academia, 08:00–18:00 trabalho, 19:00–20:00 inglês. Posso criar lembretes recorrentes?"},
    {"text": "### Instrução:\nQuero melhorar minha produtividade no negócio.\n\n### Entrada:\nSou empreendedor, tenho meta de aumentar faturamento. Toda segunda planejo a semana, toda sexta analiso relatórios.\n\n### Resposta:\nSugestões de automação:\n- Segunda 09h tarefa recorrente planejamento\n- Sexta 16h análise de relatórios\n- Subtarefas: revisar anúncios, leads e planilhas.\nRiscos: não medir indicadores."},
    {"text": "### Instrução:\nOrganize minha noite.\n\n### Entrada:\nEstudo à tarde. De noite quero cuidar da saúde e da família.\n\n### Resposta:\nSugestão:\n18:30 treino leve\n19:15 jantar\n20:00 tempo de qualidade\n21:00 organização para amanhã\nCriar lembrete diário e meta semanal de 3 treinos?"}
]

# Salvar como CSV
df = pd.DataFrame(dataset)
df.to_csv('/content/dataset.csv', index=False)

print("Dataset criado com sucesso!")
print(f"Número de exemplos: {len(df)}")

# 4. Executar treinamento
!autotrain llm --train \
  --model mistralai/Mistral-7B-Instruct-v0.3 \
  --project-name task-brain \
  --data-path /content \
  --train-split dataset.csv \
  --text-column text \
  --lr 2e-4 \
  --epochs 3 \
  --batch-size 1 \
  --gradient-accumulation 4 \
  --mixed-precision fp16
