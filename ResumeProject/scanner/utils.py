import PyPDF2
import spacy
import re
import pickle
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()

def get_skills(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.pos_ in ["PROPN", "NOUN"]]
    return ", ".join(list(set(keywords))[:15])

def calculate_similarity(resume, job):
    docs = [clean_text(resume), clean_text(job)]
    tfidf = vectorizer.transform(docs)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)

def predict_candidate(text,score):
    text_vec = vectorizer.transform([clean_text(text)])
    pred = model.predict(text_vec)[0]
    prob = model.predict_proba(text_vec)[0][1]
    if score < 30:
        return "Rejected", 0
    return ("Selected" if pred == 1 else "Rejected", round(prob * 100, 2))