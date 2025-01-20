import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd
import numpy as np

titanic_data =sns.load_dataset('titanic')
# Finding outlier ages
iqr = titanic_data['age'].quantile(0.75) - titanic_data['age'].quantile(0.25)
lower_age_limit = titanic_data['age'].quantile(0.25) - (iqr * 1.5)
upper_age_limit = titanic_data['age'].quantile(0.75) + (iqr * 1.5)

# Find rows containing the outliers
age_outliers = np.where(titanic_data['age'] > upper_age_limit, True, np.where(titanic_data['age'] < lower_age_limit, True, False))

# Remove rows containing the outlier values
titanic_age_without_ouliers = titanic_data.loc[~(age_outliers), ]
print(titanic_data.shape, titanic_age_without_ouliers.shape)
