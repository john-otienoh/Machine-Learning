import matplotlib as plt
import seaborn as sns
import numpy as np

# plt.rcParams("figure.figsize") == [8,6]
sns.set_style("darkgrid")

titanic_data = sns.load_dataset('titanic')
titanic_data =titanic_data[['embark_town', 'age', 'fare']]
titanic_data.embark_town.fillna("Missing")
