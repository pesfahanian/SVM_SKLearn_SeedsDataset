import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.utils import shuffle
from matplotlib import style

data = pd.read_csv("/content/seeds_dataset - Copy.csv", ",")
labels = data["Label"]

train_to_test_ratio = 0.955
input_size = 7

features = []

for j in range(0, len(labels)):
  feature = []
  for i in range(0, input_size):
    f = data["Feature_"+str(i+1)]
    feature.append(f[j])
  features.append(feature)
  
labels = np.array(labels)  
features, labels = shuffle(features, labels)

print(features)
print(labels)

train_set = features[:int(train_to_test_ratio*len(features))]
train_set_labels = labels[:int(train_to_test_ratio*len(labels))]

test_set = features[int(train_to_test_ratio*len(features)):]
test_set_labels = labels[int(train_to_test_ratio*len(labels)):]

print(len(train_set))
print(len(train_set_labels))
print(len(test_set))
print(len(test_set_labels))
print(test_set)
print(test_set_labels)

X = np.array(train_set)
Y = np.array(train_set_labels)

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X, Y)

sum_err = 0
for i in range(0, len(test_set)):
  data = test_set[i]
  err = abs(test_set_labels[i] - clf.predict([data]))
  print("Error =", err)
  sum_err += err[0]
  
Avg_error = ((sum_err)/len(test_set))
print("Average Error =", Avg_error)
