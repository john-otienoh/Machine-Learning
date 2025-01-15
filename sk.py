import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris

df = pd.read_csv("/home/outis/outis_codes/Tech_Boy/Machine-Learning/datasets/data.csv")
feature_names = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
    ]

# Features Matrix
x = df.loc[:, feature_names].values
# Target Vectors
y = df.loc[:, 'species'].values
print(y.shape)
