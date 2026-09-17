# Getting a Free Groq API Key

[Groq](https://groq.com) offers a free tier with access to several powerful open-weight LLMs (Llama 3, Mixtral, Gemma, etc.) at very high inference speeds — more than enough to power the chatbot in this exercise.

---

## 1. Create an account

1. Go to [https://console.groq.com](https://console.groq.com).
2. Click **Sign up** and create an account (Google or GitHub sign-in is available).
3. Verify your e-mail if prompted.

---

## 2. Generate an API key

1. Once logged in, open the left sidebar and click **API Keys**.
2. Click **Create API Key**.
3. Give it a name (e.g. `nos-chatbot`) and click **Submit**.
4. **Copy the key immediately** — it will only be shown once.

Your key will look like:

```
gsk_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 3. Store the key safely

Open `chatbot/.env` and paste your key:

```bash
# chatbot/.env
GROQ_API_KEY=gsk_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

To load it in your code, you can use [`python-dotenv`](https://pypi.org/project/python-dotenv/):

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
```

---

## 4. Make your first call

The following code is an example on how you can make calls using groq:

```python
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "Hello!"},
    ],
)

print(response.choices[0].message.content)
```

---

## 5. Available models (free tier)

| Model ID | Context window | Notes |
|---|---|---|
| `openai/gpt-oss-20b` | Check current documentation | Recommended default for this exercise |
| `openai/gpt-oss-120b` | Check current documentation | Larger model for more complex reasoning |
| `qwen/qwen3.6-27b` | Check current documentation | Alternative general-purpose model |

The full and up-to-date list is at [https://console.groq.com/docs/models](https://console.groq.com/docs/models).

> **Tip:** `openai/gpt-oss-20b` is the recommended default for this exercise. Model availability and free-tier limits can change, so check the current model list before starting.

---

## 6. Free tier limits

Groq's free tier is generous but rate-limited. As of early 2026 the main constraints are:

- **Requests per minute (RPM):** 30
- **Tokens per minute (TPM):** 6 000 – 14 400 (varies by model)
- **Requests per day (RPD):** 14 400

For local development and the scope of this exercise these limits are well above what you will need. Check the latest quotas at [https://console.groq.com/docs/rate-limits](https://console.groq.com/docs/rate-limits).

---

## Further reading

- [Groq API reference](https://console.groq.com/docs/api-reference)
- [Tool / function calling guide](https://console.groq.com/docs/tool-use) — relevant for routing chatbot intents
