# Banking Triage Agent

## Objetivo

Construir um agente que recebe uma mensagem de um cliente bancário, classifica o pedido e devolve uma resposta curta e segura.

O agente deve devolver exclusivamente este formato JSON:

```json
{
  "category": "cartao | transferencia | conta | acesso_app | possivel_fraude | desconhecida",
  "urgency": "baixa | media | alta",
  "response": "resposta curta em português"
}
```

## Regras funcionais

- Suportar as categorias `cartao`, `transferencia`, `conta`, `acesso_app` e `possivel_fraude`.
- Usar `desconhecida` quando o pedido não puder ser classificado.
- Pedidos sobre cartão perdido/roubado e transações não reconhecidas têm urgência `alta`.
- A resposta deve ter no máximo duas frases.
- Nunca pedir passwords, PINs ou códigos de autenticação.
- Não inventar comissões, prazos ou políticas do banco.
- Usar português.

## Estrutura fornecida

```text
basic-agent-assignment/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── llm.py
│   ├── prompt.py
│   └── validation.py
└── tests/
    └── test_validation.py
```

## Tarefas

1. Criar uma feature branch no formato `feature/{nome}-agent-implementation`.
2. Copiar `.env.example` para `.env`.
3. Criar uma chave gratuita no Groq seguindo `GROQ_SETUP.md` fornecido.
4. Implementar o `SYSTEM_PROMPT` em `src/prompt.py`.
5. Implementar a chamada ao modelo em `src/llm.py`.
6. Ligar a leitura do terminal, chamada do agente e impressão do resultado em `app.py`.
7. Executar os testes e testar pelo menos cinco mensagens.
8. Abrir um Pull Request para `main`.

## Instalação

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
copy .env.example .env
```

Preencher `GROQ_API_KEY` no ficheiro `.env`. Nunca fazer commit desse ficheiro.

## Execução

```bash
python app.py
```

## Testes

```bash
python -m pytest
```

## Critérios de aceitação

- O programa arranca sem erros quando a chave está configurada.
- O resultado é JSON válido e contém exatamente `category`, `urgency` e `response`.
- Os valores de categoria e urgência são validados localmente.
- Erros da API são apresentados de forma clara.
- A chave não aparece no código nem em commits.
- O README explica como executar a solução.
