from  sklearn.preprocessing import LabelEncoder
import matplotlib as plt
import seaborn as sns
import numpy as np
import pandas as pd

# plt.rcParams("figure.figsize") == [8,6]
sns.set_style("darkgrid")

titanic_data = sns.load_dataset('titanic')
titanic_data =titanic_data[['sex', 'class','embark_town']]
le  = LabelEncoder()
le.fit(titanic_data['class'])
titanic_data['le_class'] = le.transform(titanic_data['class'])
print(titanic_data.head())
