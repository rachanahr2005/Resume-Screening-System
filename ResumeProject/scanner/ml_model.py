import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = {
    data = {
    "text": [
        "python machine learning data science",
        "deep learning python ai nlp",
        "java spring boot backend developer",
        "hibernate java rest api",
        "sales marketing communication",
        "digital marketing seo social media",
        "data analysis python sql excel",
        "power bi dashboards data visualization",
        "accounting finance taxation excel",
        "business management leadership communication"
    ],
    "label": [1,1,1,1,0,0,1,1,0,0]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))