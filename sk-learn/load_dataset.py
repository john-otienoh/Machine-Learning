# Import scikit.learn's datasets
from sklearn import datasets

# Load digits Dataset
digits = datasets.load_digits()

# Create feature matrix & target matrix
features = digits.data
target = digits.target

print(digits.DESCR)
