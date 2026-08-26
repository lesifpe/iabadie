import re
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

MODEL_PATH = hf_hub_download(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct-GGUF",
    filename="qwen2.5-0.5b-instruct-q4_k_m.gguf"
)

llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=2, verbose=False)

SYSTEM_PROMPT = """Você reescreve uma resposta de perguntas frequentes (FAQ) do curso de Análise e Desenvolvimento de Sistemas (ADS), de forma natural, em português, de modo curto, direto e natural.

Regras:
- Comece direto pela resposta.
- Não use introduções ou conclusões genéricas.
- Nunca use frases de abertura como "Aqui está", "Claro" ou "Aqui está uma resposta natural e curta para a pergunta".
- Nunca use frases de fechamento.
- Não invente informações nem faça suposições.
- Não adicione opiniões, elogios, motivação ou contexto desnecessário.
- Não repita a pergunta.
- Não use linguagem excessivamente formal ou corporativa.
- Não use frases típicas e vazias de IA, como:
  "Claro!", "Com certeza!", "Ótima pergunta!", "Espero ter ajudado!",
  "É importante destacar que...", "Vale ressaltar que...",
  "Nesse contexto...", "De modo geral...", "Em resumo...",
  "Em outras palavras...", "Isso significa que...",
  "Para melhor compreensão...", "É fundamental...",
  "Essa é uma excelente forma de...", "Uma ótima maneira de...",
  "Fico feliz em ajudar!".
- Não transforme uma resposta simples em uma explicação longa.
- Responda somente o necessário para esclarecer a dúvida.
- Números, datas e valores devem ser copiados EXATAMENTE como estão no texto original, sem alterar nenhum dígito.
"""

PREAMBLE_PATTERNS = [
    r"^(aqui está|aqui vai|segue|claro)[^:]*:\s*",
]

def _clean_response(text):
    text = text.strip()

    for pattern in PREAMBLE_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    cut_markers = ["http", "www.", "Links úteis", "\n-", "\n*", "\n•"]
    for marker in cut_markers:
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx]

    return text.strip()

def generate_natural_response(user_question, faq_answer):
    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Pergunta: {user_question}\nInformação: {faq_answer}"}
        ],
        max_tokens=80,
        temperature=0.2,
    )
    raw = response["choices"][0]["message"]["content"]
    return _clean_response(raw)