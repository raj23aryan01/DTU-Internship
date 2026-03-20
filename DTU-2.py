# RAG-BASED NEURO CHATBOT
# =========================

# Install dependencies
!pip install sentence-transformers transformers

from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np

# -------------------------
# STEP 1: Load Embedding Model
# -------------------------
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------
# STEP 2: Knowledge Base
# -------------------------
documents = [
    "The brain is the central organ of the nervous system.",
    "Neurons are specialized cells that transmit signals.",
    "Synapses allow neurons to communicate.",
    "The hippocampus is crucial for memory formation.",
    "The amygdala plays a role in fear and emotion.",
    "Dopamine is a neurotransmitter linked to reward.",
    "Neuroplasticity allows the brain to adapt and reorganize."
]

# -------------------------
# STEP 3: Create Embeddings
# -------------------------
doc_embeddings = embedder.encode(documents)

# -------------------------
# STEP 4: Retriever Function
# -------------------------
def retrieve(query, top_k=2):
    
    # encode query
    query_embedding = embedder.encode([query])
    
    # compute similarity
    similarities = np.dot(doc_embeddings, query_embedding.T).flatten()
    
    # get top results
    top_indices = similarities.argsort()[-top_k:][::-1]
    
    return [documents[i] for i in top_indices]

# -------------------------
# STEP 5: Generator (LLM)
# -------------------------
generator = pipeline("text-generation", model="distilgpt2")

def generate_answer(query):
    
    # retrieve context
    context = retrieve(query)
    
    # create prompt
    prompt = f"""
    Answer the question using the context below:
    
    Context:
    {context}
    
    Question:
    {query}
    
    Answer:
    """
    
    # generate response
    response = generator(prompt, max_length=150, num_return_sequences=1)
    
    return response[0]['generated_text']

# -------------------------
# STEP 6: Chat Loop
# -------------------------
print("NeuroBot RAG: Ask neuroscience questions (type 'exit')")

while True:
    query = input("You: ")
    
    if query.lower() == "exit":
        print("Bot: Goodbye!")
        break
    
    answer = generate_answer(query)
    print("Bot:", answer)