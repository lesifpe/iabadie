import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize
FAQ_PATH = "./data/faq.json"
EMBEDDINGS_PATH = "./embeddings/faq.index"
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

with open(FAQ_PATH,"r",encoding="utf-8") as f:
    faq = json.load(f)
    
question_list = [item["question"] for item in faq]

model = SentenceTransformer(MODEL_NAME)

embedding_list = model.encode(question_list, show_progress_bar=True)

dimension = embedding_list.shape[1]

index = faiss.IndexFlatIP(dimension)

embedding_norm_list = normalize(embedding_list)

index.add(embedding_norm_list)

faiss.write_index(index, EMBEDDINGS_PATH)
print(f"Embeddings salvos em {EMBEDDINGS_PATH}")
print(f"Total de perguntas indexadas {index.ntotal}")