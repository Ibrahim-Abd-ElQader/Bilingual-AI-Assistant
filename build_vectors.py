import json
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")

with open("data/qa_data.json", "r", encoding="utf-8") as f:

    data = json.load(f)

questions = []
mapping = []

for item in data:
    all_q = item.get("question_ar", []) + item.get("question_en", [])
    for q in all_q:
        questions.append(q)
        mapping.append(item)

embeddings = model.encode(questions)

with open("vector_db.pkl", "wb") as f:
    pickle.dump((embeddings, mapping, questions), f)

print(f"Vector database created with {len(questions)} question entries.")
