from llama_cpp import Llama
from huggingface_hub import hf_hub_download

MODEL_PATH = hf_hub_download(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct-GGUF",
    filename="qwen2.5-0.5b-instruct-q4_k_m.gguf"
)

llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=2, verbose=False)

SYSTEM_PROMPT = """Na posição de um assistente que responde perguntas frequentes (FAQ) do curso de Análise e Desenvolvimento de Sistemas (ADS), você deve responder a pergunta do usuário de forma natural, em português, de modo curto, direto e natural, como uma pessoa respondendo uma dúvida em um chat.

Regras:
- Não invente informações nem faça suposições.
- Não use frases de abertura ou fechamento.
- Não adicione opiniões, elogios, motivação ou contexto desnecessário.
- Não repita a pergunta.
- Não use introduções ou conclusões genéricas.
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

def generate_natural_response(user_question, faq_answer):
    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Pergunta: {user_question}\nInformação: {faq_answer}"}
        ],
        max_tokens=150,
        temperature=0.3,
    )
    return response["choices"][0]["message"]["content"].strip()