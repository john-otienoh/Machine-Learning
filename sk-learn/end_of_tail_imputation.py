import matplotlib as plt
import seaborn as sns
import numpy as np

# plt.rcParams("figure.figsize") == [8,6]
sns.set_style("darkgrid")

titanic_data = sns.load_dataset('titanic')
titanic_data =titanic_data[['survived', 'pclass', 'age', 'fare']]
# print(titanic_data.isnull().mean())
titanic_data.age.hist(bins=50)
end_value = titanic_data.age.mean() + 3 * titanic_data.age.std()
titanic_data['age_eod'] = titanic_data.age.fillna(end_value)
print(titanic_data.head(10))
