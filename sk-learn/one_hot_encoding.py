import matplotlib as plt
import seaborn as sns
import numpy as np
import pandas as pd

# plt.rcParams("figure.figsize") == [8,6]
sns.set_style("darkgrid")

titanic_data = sns.load_dataset('titanic')
titanic_data =titanic_data[['sex', 'class','embark_town']]
print(titanic_data['sex'].unique())
print(titanic_data['embark_town'].unique())
print(titanic_data['class'].unique())
temp = pd.get_dummies(titanic_data['sex'])
# print(temp.head())
print(pd.concat([titanic_data['sex'], pd.get_dummies(titanic_data['sex'])], axis=1).head())
