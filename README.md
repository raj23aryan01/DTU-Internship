# 🧠 NeuroBot: Basic & Improved Neuroscience Chatbot

A simple **retrieval-based chatbot** built using Python, TF-IDF, and cosine similarity. This project demonstrates how basic Natural Language Processing (NLP) techniques can be used to build a chatbot focused on neuroscience concepts.

---

## 📌 Features

### 🔹 Basic Version

* Uses TF-IDF vectorization
* Computes cosine similarity to find the best response
* Simple preprocessing (lowercasing + tokenization)
* Works with a small neuroscience knowledge base

### 🔹 Improved Version

* Removes stopwords for better understanding
* Applies stemming for word normalization
* Optimized performance (no repeated training)
* More natural responses
* Cleaner architecture

---

## 🧠 Knowledge Base Topics

The chatbot currently understands basic neuroscience concepts such as:

* Brain functions
* Neurons and synapses
* Memory (hippocampus)
* Emotions (amygdala)
* Neurotransmitters (dopamine)
* Neuroplasticity

---

## ⚙️ Installation

Run the following command to install dependencies:

```bash
pip install scikit-learn nltk
```

Then download required NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🚀 How It Works

1. **Preprocessing**

   * Convert text to lowercase
   * Tokenize sentences
   * (Improved version) Remove stopwords and apply stemming

2. **Vectorization**

   * Convert text into TF-IDF vectors

3. **Similarity Matching**

   * Compare user input with corpus using cosine similarity

4. **Response Selection**

   * Return the most similar sentence
   * If similarity is too low → fallback response

---

## 💻 Usage

Run the chatbot:

```bash
python chatbot.py
```

Example interaction:

```
NeuroBot: Ask me anything about neuroscience (type 'exit')

You: what does the brain do?
Bot: The brain controls the body.

You: what is memory?
Bot: The hippocampus is involved in memory.
```

---

## 📂 Project Structure

```
NeuroBot/
│── basic_chatbot.py
│── improved_chatbot.py
│── README.md
```

---

## ⚡ Limitations

* Not a true AI chatbot (rule-based retrieval)
* Limited knowledge base
* No conversation memory
* Cannot generate new answers

---

## 🔥 Future Improvements

* Add larger and dynamic datasets
* Use advanced NLP models (transformers)
* Build a web interface (Streamlit / Flask)
* Add voice interaction
* Deploy as a chatbot app

---

## 🎯 Learning Outcomes

This project helps you understand:

* TF-IDF vectorization
* Cosine similarity
* Basic NLP preprocessing
* How chatbots work internally

---

## 🤝 Contributing

Feel free to fork this repository and improve the chatbot by:

* Expanding the dataset
* Enhancing NLP techniques
* Improving UI/UX

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Created as a beginner-friendly NLP project to explore chatbot development.

---

If you want, I can also:

* Add badges (GitHub stars, license, etc.)
* Make it look more **professional / resume-ready**
* Or customize it for a **portfolio project**
