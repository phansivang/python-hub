# simple binary classification machine learning model using logistic regression
# Binary classification models output a value from a class that contains only two values,
# for example, a model that outputs either rain or no rain.
# Multiclass classification models output a value from a class that contains more than two values,
# for example, a model that can output either rain, hail, snow, or sleet.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load your dataset (replace 'data.csv' with your dataset)
data = pd.read_csv('data.csv')

# Assuming the target variable is 'target' and features are in columns 'feature1', 'feature2', etc.
features = ['feature1', 'feature2']  # Replace these with your actual feature names
target = 'target'  # Replace with your actual target column name

# Separate features and the target variable
X = data[features]  # Features
y = data[target]  # Target variableaining and testing sets
test_size = 0.2
random_state = 0
# Split the data into tr
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Create a Logistic Regression model
logreg = LogisticRegression()

# Fit the model using the training data
logreg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logreg.predict(X_test) # Calculate and print accuracy
print('Accuracy:', accuracy_score(y_test, y_pred))