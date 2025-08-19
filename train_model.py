import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Create a simple dataset
data = {
    'review': [
        'This movie was amazing and I loved it',
        'a truly terrible and boring film',
        'The acting was superb',
        'I would not recommend this to anyone',
        'What a fantastic and heartwarming story',
        'The plot was predictable and dull'
    ],
    'sentiment': ['positive', 'negative', 'positive', 'negative', 'positive', 'negative']
}
df = pd.DataFrame(data)

# Separate features (X) and target (y)
X = df['review']
y = df['sentiment']

# 2. Split data into training and testing sets
# We train the model on one part and test it on another to see how well it learned.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 3. Create the TF-IDF Vectorizer
# This object will learn the vocabulary and turn our text into numbers.
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train) # Learn and transform training data
X_test_tfidf = vectorizer.transform(X_test)       # Only transform test data

# 4. Train the Classifier
# We're using Logistic Regression, a simple but effective classification model.
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# 5. Make predictions and evaluate
predictions = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, predictions)

print(f"Our model's predictions: {predictions}")
print(f"The actual sentiments: {y_test.values}")
print(f"Accuracy: {accuracy:.2f}")