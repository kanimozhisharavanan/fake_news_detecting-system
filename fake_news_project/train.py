import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("data/news.csv")

# Convert labels to numbers
y = df["label"].map({"fake": 0, "real": 1})

# Text data
X = df["text"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open("model/fake_news_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model saved!")