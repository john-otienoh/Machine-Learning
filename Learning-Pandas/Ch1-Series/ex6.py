# Passenger Frequency
import pandas as pd
import numpy as np

# In this exercise, we begin looking at real-world data loaded from a one-column CSV file.
# Start here by invoking pd.read_csv, calling squeeze on the one-column data frame it
# returns, and getting back a series.
# Your task in this exercise is to show what percentage of taxi rides had only one passenger versus the (theoretical) maximum of six passengers.

# Reading the data into a series
s = pd.read_csv('./Machine-Learning/datasets/car_data.csv', header=None).squeeze()
print(s.value_counts())
