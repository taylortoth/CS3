'''
Logistic Regression on the Bechdel Test Dataset
This script predicts whether or not a movie passes the Bechdel test as a binary using the sentiment score and linear regression.
It converts the rating into a binary for easier analysis, drops rows with missing sentiment values, splits the dataset into a train and test set, and then applies
logistic regression to the training data. The test set is used to make predictions, and the performance of the model is evaluated with an accuracy score and report.

Running this script requires the numpy, sklearn, and pandas libraries.
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

df = pd.read_csv('./DATA/bechdel_movies.csv')

# Simplify the 'rating' column into binary classification: 1 for pass (rating == 3), 0 for fail (rating != 3)
df['rating_binary'] = df['rating'].apply(lambda x: 1 if x == 3 else 0)

# Drop rows with missing sentiment values
df_clean = df.dropna(subset=['sentiment'])

# Check the distribution of the new binary 'rating_binary' column
df_clean['rating_binary'].value_counts()

# Define features (X) and target (y)
X = df_clean[['sentiment']]
y = df_clean['rating_binary']

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Remove rows with NaN or infinite values in the training data
X_train = X_train.replace([np.inf, -np.inf], np.nan).dropna()
y_train = y_train[X_train.index]  # Keep only corresponding rows in y_train

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Output results
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)
