import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

class NaiveBayes:
    def __init__(self):
        self.class_prob = {}
        self.features_prob = {}

    def fit(self, x, Y):
        for value in Y: # Calculate class frequency
            if value in self.class_prob.keys():
                self.class_prob[value] += 1
            else:
                self.class_prob[value] = 1
        total_samples = len(Y)
        for key in self.class_prob: # Calculate class probabilities
            self.class_prob[key] = self.class_prob[key] / total_samples
        for c in self.class_prob.keys(): # Calculate feature probabilities with Laplace smoothing
            self.features_prob[c] = {}
            class_rows = x[Y == c]
            for feature in x.columns:
                self.features_prob[c][feature] = {}
                unique_values = x[feature].unique()
                total = len(class_rows)
                num_unique = len(unique_values)
                for value in unique_values:
                    count = np.sum(class_rows[feature] == value)
                    self.features_prob[c][feature][value] = (count + 1) / (total + num_unique) # Laplace smoothing

    def predict(self, x):
        predictions = []
        for i in range(len(x)):
            row = x.iloc[i]
            max_log_prob = -float('inf')
            predicted_class = None
            for c in self.class_prob:
                log_prob = math.log(self.class_prob[c])
                for feature in x.columns:
                    value = row[feature]
                    if value in self.features_prob[c][feature]:
                        log_prob += math.log(self.features_prob[c][feature][value])
                    else:
                        log_prob += math.log(1e-6) # Small probability for unseen values
                if log_prob > max_log_prob:
                    max_log_prob = log_prob
                    predicted_class = c
            predictions.append(predicted_class)
        return predictions

data = pd.read_csv("C:\\old sys\\users-ig134\\projects\\helloworld\\aiml\\Social_Network_Ads.csv")
data["Gender"] = np.where(data["Gender"] == 'Male', 1, 0)
X = data.iloc[:, 1:4]
y = data['Purchased']
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = NaiveBayes()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred)
recall = recall_score(Y_test, Y_pred)
f1 = f1_score(Y_test, Y_pred)
print("Validation Set Metrics:")
print("Accuracy: {:.2f}".format(accuracy))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("F1 Score: {:.2f}".format(f1))
confusion = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix:")
print(confusion)
print("Class 0 predicted correctly : ", confusion[0][0])
print("Class 0 predicted incorrectly : ", confusion[0][1])
print("Class 1 predicted incorrectly : ", confusion[1][0])
print("Class 1 predicted correctly : ", confusion[1][1])
valid = data.sample(n=20)
X_valid = valid.iloc[:, 1:4]
y_valid = valid['Purchased']
y_val_pred = model.predict(X_valid)
accuracy_val = accuracy_score(y_valid, y_val_pred)
precision_val = precision_score(y_valid, y_val_pred)
recall_val = recall_score(y_valid, y_val_pred)
f1_val = f1_score(y_valid, y_val_pred)
print("\nRandom Validation Sample Metrics:")
print("Accuracy: {:.2f}".format(accuracy_val))
print("Precision: {:.2f}".format(precision_val))
print("Recall: {:.2f}".format(recall_val))
print("F1 Score: {:.2f}".format(f1_val))
a = pd.DataFrame()
a["Gender"] = [1]  # Male
a["Age"] = [30]
a["EstimatedSalary"] = [50000]
print("\nPrediction for new input:", model.predict(a))
