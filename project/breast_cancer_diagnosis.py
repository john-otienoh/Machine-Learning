from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np

breast = datasets.load_breast_cancer()
X, y = breast.data, breast.target


train, test, trainlab, testlab = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=7).fit(train, trainlab)
print(knn.predict(test[[110]]), testlab[110])

# Test Accuracy
print(knn.score(test, testlab) * 100)
