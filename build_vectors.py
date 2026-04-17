# This script encodes all questions into vectors using SentenceTransformer
# and saves the embeddings, original questions, and mapping into 'vector_db.pkl'.
import json
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")

# Load the updated qa_data.json (assumed to be in the current directory)
with open("data/qa_data.json", "r", encoding="utf-8") as f:

    data = json.load(f)

questions = []
mapping = []

for item in data:
    # Combine Arabic and English questions for embedding
    all_q = item.get("question_ar", []) + item.get("question_en", [])
    for q in all_q:
        questions.append(q)
        mapping.append(item)

# Encode all questions into vectors
embeddings = model.encode(questions)

# Save the vector database
with open("vector_db.pkl", "wb") as f:
    pickle.dump((embeddings, mapping, questions), f)

print(f"Vector database created with {len(questions)} question entries.")