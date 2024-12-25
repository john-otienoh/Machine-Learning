# Monday temperatures
import pandas as pd
import numpy as np

# Create a series of 28 temperature readings in Celsius,representing four seven-day weeks, 
# randomly selected from a normal distribution with a mean of 20 and a standard deviation of 5, 
# rounded to the nearest integer.
# The index should start with Sun, continue through Sat, and repeat Sun through Sat until each temperature has a value. 

days = "Sun,Mon,Tue,Wed,Thur,Fri,Sat".split(',')
temperatures = pd.Series(np.random.default_rng(0).normal(20, 5, 28), index=days*4).astype(np.int8)
print(temperatures)
# The question is, what was the mean temperature on Mondays during this period
mon_temperatures = temperatures.loc['Mon']
print(f"The average temperature for Mondays is {mon_temperatures.mean()}")

# What was the average weekend temperature (i.e., Saturdays and Sundays)?
weekend_temperature = temperatures.loc['Sat']
print(weekend_temperature)

# What are the two most common temperatures in our data set, and how often does each appear?
print(temperatures.value_counts()[:2])

# How many times is the change in temperature from the previous day greater than 2 degrees?
