# Replace the missing values in the deck column of the Titanic dataset with the
# most frequently occurring categories in that column. Plot a bar plot for the
# updated deck column.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load the dataset
titanic_data = sns.load_dataset('titanic')

# Count of Missing values
deck_missing_values = titanic_data['deck'].isnull().sum()

# Find frequently Ocurring value
titanic_data['deck'].value_counts()

# Replace the values with frequently
titanic_data['deck'] = titanic_data['deck'].fillna('C')
print(titanic_data['deck'].head(10))

plt.bar(titanic_data['deck'].index, titanic_data['deck'].values)
plt.show()