import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

plt.rcParams['figure.figsize'] = [8,6]
sns.set_style("darkgrid")

titanic_data = sns.load_dataset('titanic')
titanic_data = titanic_data[['age', 'fare', 'pclass']]

# Standardization Process
scaler = StandardScaler()
scaler.fit(titanic_data)
titanic_data_scaled = scaler.transform(titanic_data)
titanic_data_scaled = pd.DataFrame(titanic_data_scaled, columns=titanic_data.columns)

# Min/Max Scaling
scaler = MinMaxScaler()
scaler.fit(titanic_data)
titanic_data_scaled = scaler.transform(titanic_data)
titanic_data_scaled = pd.DataFrame(titanic_data_scaled, columns=titanic_data.columns)

# Mean Normalization
mean_values = titanic_data.mean(axis=0) # Find Mean of the values
range_values = titanic_data.max(axis=0) - titanic_data.min(axis=0)
titanic_data_scaled = (titanic_data - mean_values) / range_values

# Plotting and Printing
sns.kdeplot(titanic_data['age']) # Unscaled Column
sns.kdeplot(titanic_data_scaled['age']) # Scaled columns
print(titanic_data.head())
print(titanic_data.describe())
