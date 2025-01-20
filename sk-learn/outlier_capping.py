import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd
import numpy as np

titanic_data =sns.load_dataset('titanic')

# Find upper and lower threshold
lower_age_limit = titanic_data['age'].mean() - (3*titanic_data['age'].std())
upper_age_limit = titanic_data['age'].mean() + (3*titanic_data['age'].std())

# Replace Outliers with upper and lower limits
titanic_data['age'] = np.where(titanic_data['age'] > upper_age_limit, True, np.where(titanic_data['age'] < lower_age_limit, True, False))

print(lower_age_limit, upper_age_limit)
