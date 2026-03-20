# BASIC NEURO CHATBOT
# =========================

# Install dependencies (Colab)
!pip install scikit-learn nltk

import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# -------------------------
# STEP 1: Knowledge Base
# -------------------------
corpus = [
    "The brain controls the body.",
    "Neurons transmit electrical signals.",
    "Synapses connect neurons.",
    "The hippocampus is involved in memory.",
    "The amygdala processes emotions.",
    "Dopamine is related to reward and motivation.",
    "Neuroplasticity is the brain's ability to adapt."
]

# -------------------------
# STEP 2: Preprocessing
# -------------------------
def preprocess(text):
    text = text.lower()                      # convert to lowercase
    tokens = nltk.word_tokenize(text)        # tokenize words
    return " ".join(tokens)

# -------------------------
# STEP 3: Chatbot Logic
# -------------------------
def chatbot_response(user_input):
    
    # preprocess input
    processed_input = preprocess(user_input)
    
    # combine corpus + user input
    all_texts = corpus + [processed_input]
    
    # convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # compute similarity
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # find best match
    index = similarity.argmax()
    score = similarity[0][index]
    
    # threshold check
    if score < 0.2:
        return "I am not sure. Please ask about neuroscience."
    else:
        return corpus[index]

# -------------------------
# STEP 4: Chat Loop
# -------------------------
print("NeuroBot Basic: Ask me anything about neuroscience (type 'exit')")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    
    print("Bot:", chatbot_response(user_input))
