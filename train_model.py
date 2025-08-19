import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# 1. Load the dataset from the CSV file
print("Loading data...")
# We take a sample of 10,000 reviews to keep training time manageable.
# You can use the full 50,000, but it will be slower.
df = pd.read_csv('IMDB Dataset.csv').sample(10000, random_state=42)

print("Data loaded. Preparing training and test sets...")
# Separate features (X) and target (y)
X = df['review']
y = df['sentiment']

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Create and train the TF-IDF Vectorizer
print("Vectorizing text data...")
vectorizer = TfidfVectorizer(max_features=5000) # Limit to top 5000 words
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 4. Train the Classifier
print("Training the model...")
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)
print("Model training complete.")

# 5. Make predictions and evaluate
print("Evaluating the model...")
predictions = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4f}")

# 6. Save the model and the vectorizer
print("Saving model and vectorizer...")
joblib.dump(model, 'models/sentiment_model.joblib')
joblib.dump(vectorizer, 'models/sentiment_vectorizer.joblib')
print("Model and vectorizer have been saved successfully!")