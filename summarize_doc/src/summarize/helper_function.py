import re
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

def preporcess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return words

def sentence_score(text):
    sentences = sent_tokenize(text)
    words = preporcess_text(text)
    word_frequencies = Counter(words)
    scores = {}

    for sentence in sentences:
        sentence_words = preporcess_text(sentence)
        score = sum([word_frequencies[word] for word in sentence_words])
        scores[sentence] = score
    return scores

def summarize_text(text, num_sentences=10):
    scores = sentence_score(text)
    ranked_sentences = sorted(scores, key=scores.get, reverse=True)
    summary = " ".join(ranked_sentences[:num_sentences])
    return summary