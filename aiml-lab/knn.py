import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

class KNN:
    def __init__(self,k=3):
        self.k=k

    def fit(self,x,y):
        self.x=x
        self.y=y

    def predict_single(self, point):
      distances = []
      for data_point in self.x:
          distance = euclidean_distance(point, data_point)
          distances.append(distance)
      sorted_indices = np.argsort(distances)
      k_nearest_indices = sorted_indices[:self.k]
      k_nearest_labels = []
      for index in k_nearest_indices:
          label = self.y[index]
          k_nearest_labels.append(label)
      predicted_label = np.argmax(np.bincount(k_nearest_labels))
      return predicted_label
		
    def predict(self, x):
      predicted_labels = []
      for point in x:
        predicted_labels.append(self.predict_single(point))
      return (predicted_labels)

df = pd.read_csv('iris_csv (1).csv')
df.head()
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
d={'Iris-versicolor':1, 'Iris-virginica':2, 'Iris-setosa':3}
for i in range(len(y)):
    y[i]=d[y[i]]
print(set(y))
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=7)
model=KNN()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("accuracy: ", accuracy_score(list(y_test), list(y_pred)))
print("precision: ", precision_score(list(y_test), list(y_pred), average='macro'))
print("recall: ", recall_score(list(y_test), list(y_pred), average='macro'))
print("f1 score: ", f1_score(list(y_test), list(y_pred), average='macro'))
valid = df.sample(n=20)
x_valid = (valid.iloc[:, :-1].values)
y_valid = (valid.iloc[:, -1].values)
y_predict = (model.predict(x_valid))
print((y_predict), (y_valid))
print(accuracy_score(list(y_predict), list(y_valid)))


