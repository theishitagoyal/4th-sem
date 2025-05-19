import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
import pandas as pd
import random

class LogisticRegressionSGD:
    def __init__(self, learning_rate=0.01, iteration=1000):
        self.learning_rate = learning_rate
        self.iteration = iteration
        self.theta = None
        self.costs = []

    def add_intercept(self, X):
        intercept_column = np.ones((X.shape[0], 1))
        return np.concatenate((intercept_column, X), axis=1)
    
    def sigmoid(self, z):
        z = np.clip(z, -500, 500)  # Prevent overflow in exp
        return 1 / (1 + np.exp(-z))

    def compute_cost(self, X, y):
        m = y.size
        z = np.dot(X, self.theta)
        a = self.sigmoid(z)
        cost = - (1 / m) * np.sum(y * np.log(a + 1e-15) + (1 - y) * np.log(1 - a + 1e-15))
        return cost

    def fit(self, X, y):
        X = self.add_intercept(X)
        m, n = X.shape
        self.theta = np.random.randn(n) * 0.01  # Small random initialization

        for epoch in range(self.iteration):
            for i in range(m):
                xi = X[i].reshape(1, -1)  # Shape (1, n)
                yi = y[i]
                z = np.dot(xi, self.theta) # Compute prediction
                a = self.sigmoid(z)
                dw = xi.T * (a - yi) # Compute gradients
                db = a - yi
                self.theta -= self.learning_rate * dw.flatten() # Update parameters            
            cost = self.compute_cost(X, y) # Compute and store cost after each full pass over data
            self.costs.append(cost)
            if (epoch + 1) % 100 == 0 or epoch == 0: # Print cost every 100 iterations for visibility
                print(f"Iteration {epoch + 1}/{self.iteration}, Cost: {cost:.4f}")

    def predict_prob(self, X):
        X = self.add_intercept(X)
        return self.sigmoid(np.dot(X, self.theta))

    def predict(self, X, threshold=0.5):
        return self.predict_prob(X) >= threshold

data = pd.read_csv("C:\\old sys\\users-ig134\\projects\\helloworld\\aiml\\Breastcancer_data.csv")
data.info()
X = data.iloc[:, 2:-1].values.astype(float)
y = data.iloc[:, 1].values
y = np.where(y == 'M', 1, 0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegressionSGD(learning_rate=0.01, iteration=1000)
model.fit(X_train, y_train)
val_predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, val_predictions)
precision = precision_score(y_test, val_predictions)
recall = recall_score(y_test, val_predictions)
f1 = f1_score(y_test, val_predictions)
print("\nValidation Set Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
confusion = confusion_matrix(y_test, val_predictions)
print("\nConfusion Matrix:")
print(confusion)
print("Class 0 predicted and true :", confusion[0][0])
print("Class 0 predicted and false:", confusion[0][1])
print("Class 1 predicted and false:", confusion[1][0])
print("Class 1 predicted and true :", confusion[1][1])
X_valid = []
Y_valid = []
for i in range(20):
    index = random.randint(0, len(X) - 1)
    X_valid.append(X[index])
    Y_valid.append(y[index])
print("\nRandom validation sample labels:")
print(Y_valid)
