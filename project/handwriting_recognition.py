from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the data
digits = datasets.load_digits()
print(len(digits.data), len(digits.target))

plt.imshow(digits.images[5], cmap=plt.cm.gray_r,interpolation='nearest')
plt.show()

# Split data
X, y = digits.data, digits.target
train, test, trainlab, testlab = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=7).fit(train, trainlab)
print(knn.predict(test[[359]]), testlab[359])

# Test Accuracy
print(knn.score(test, testlab) * 100)
