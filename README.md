
 NeuroBot: From Basic NLP to RAG-Based Chatbot

NeuroBot is a simple neuroscience chatbot project that demonstrates the evolution from a **basic NLP chatbot** to a more advanced **RAG (Retrieval-Augmented Generation) system**.

This project is perfect for beginners who want to understand how modern AI chatbots work step by step.

---

##  Features

### Basic Neuro Chatbot

* Uses **TF-IDF + Cosine Similarity**
* Retrieves the most relevant answer from a fixed dataset
* Lightweight and beginner-friendly

### RAG-Based Neuro Chatbot

* Uses **Sentence Transformers** for semantic understanding
* Retrieves relevant context using embeddings
* Generates answers using a language model (LLM)
* More flexible and intelligent responses

---

##  Project Structure

```
NeuroBot/
│── basic_chatbot.py      # TF-IDF based chatbot
│── rag_chatbot.py        # RAG-based chatbot
│── README.md
```

---

## Installation

Run the following commands:

```bash
pip install scikit-learn nltk
pip install sentence-transformers transformers
```

Download NLTK tokenizer:

```python
import nltk
nltk.download('punkt')
```

---

## How It Works

### 1️Basic Chatbot (TF-IDF)

1. Preprocess user input
2. Convert text into TF-IDF vectors
3. Compute cosine similarity
4. Return the most similar sentence

 Limitation:

* Cannot generate new answers
* Limited to predefined responses

---

### 2️RAG Chatbot

1. Convert documents into embeddings
2. Encode user query
3. Retrieve top relevant documents
4. Pass context + query to LLM
5. Generate answer

Advantage:

* Understands meaning (semantic search)
* Generates dynamic responses

---

## Example

**User Input:**

```
What does the hippocampus do?
```

**Basic Bot Output:**

```
The hippocampus is involved in memory.
```

**RAG Bot Output:**

```
The hippocampus plays a crucial role in forming and organizing memories.
```

---

##  Limitations

* Small knowledge base
* Basic models (not production-level)
* May generate incorrect or vague answers
* No conversation memory

---

## Future Improvements

* Add larger neuroscience dataset
* Use **FAISS** for faster retrieval
* Improve LLM (e.g., FLAN-T5, LLaMA)
* Build a web interface (Streamlit/Gradio)
* Add chat history (memory)

---

## Learning Outcomes

This project helps you understand:

* NLP basics (tokenization, TF-IDF)
* Semantic search using embeddings
* Cosine similarity
* Retrieval-Augmented Generation (RAG)
* How modern AI chatbots work

---

## Contributing

Feel free to fork this repo and improve it!
Pull requests are welcome.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

Created by Raj Aryan for study purposes

---

 If you like this project, don’t forget to star the repo!

---




