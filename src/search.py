import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

FAQ_PATH = "./data/faq.json"
EMBEDDINGS_PATH = "./embeddings/faq.index"
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

MIN_SCORE = 0.35

TOP_K = 3

with open(FAQ_PATH, "r", encoding="utf-8") as f:
    faq = json.load(f)
    
index = faiss.read_index(EMBEDDINGS_PATH)

model = SentenceTransformer(MODEL_NAME)

def search(user_question):
    query_embedding = model.encode([user_question])

    query_norm = query_embedding / np.linalg.norm(query_embedding)

    score_list, index_list = index.search(query_norm, TOP_K)

    score_list = score_list[0]
    index_list = index_list[0]

    result_list = []

    for score, faq_index in zip(score_list,index_list):
        item = faq[faq_index]
        print(f"Score: {score:.4f} | Pergunta: {item['question']}")
        
        if score >= MIN_SCORE:
            result_list.append({
                "question": item["question"],
                "answer": item["answer"],
                "score": float(score),
                "sourceList": item.get("sourceList", [])
            })

    return result_list

if __name__ == "__main__":
    user_question = "O que fazer após perder o prazo de matrícula?"

    result_list = search(user_question)

    print(f"\nPergunta: {user_question}\n")

    if not result_list:
        print("Nenhuma resposta relevante encontrada.")
    else:
        for result in result_list:
            print(f"Score: {result['score']:.2f}")
            print(f"Pergunta similar: {result['question']}")
            print(f"Resposta: {result['answer']}")
            print("---------")