import matplotlib as plt
import seaborn as sns
import numpy as np

# plt.rcParams("figure.figsize") == [8,6]
sns.set_style("darkgrid")

titanic_data = sns.load_dataset('titanic')
titanic_data =titanic_data[['survived', 'pclass', 'age', 'fare']]

mean = titanic_data.age.mean()
median = titanic_data.age.median()

titanic_data['Median_Age'] = titanic_data.age.fillna(median)
titanic_data['Mean_Age'] = np.round(titanic_data.age.fillna(mean), 1)

print(titanic_data.head(10))
