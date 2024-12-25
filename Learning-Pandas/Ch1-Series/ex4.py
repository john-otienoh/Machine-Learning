import pandas as pd
import numpy as np
# Descriptive Statistics
# The mean, median, and standard deviation are three numbers we can use to get a better picture of our data. Adding a few other numbers can give us an even more complete picture.
# These descriptive statistics typically include the mean, standard deviation,minimum value, 25% quantile, median, 50% quantile, and maximum value.
# Understanding and using descriptive statistics is a key skill for anyone working with data, and in this exercise, you’ll practice doing so with the following:

# Generate a series of 100,000 floats in a normal distribution with a mean of 0 and a standard deviation of 100.
# Get the descriptive statistics for this series. How close are the mean and median? 
# (You don’t need to calculate the difference; rather, consider why they aren’t the same.)
# Replace the minimum value with 5 times the maximum value.
# Get the descriptive statistics again. Did the mean, median, and standard deviations change from their previous values? 
# (Again, it’s enough to see the difference without calculating it.) If so, why?

s = pd.Series(np.random.default_rng(0).normal(0, 100, 100000))
print(s.describe())
s.loc[s==s.min()] = 5*s.max()
print(s.describe())
# Demonstrate that 68%, 95%, and 99.7% of the values in s are indeed within
# one, two, and three standard distributions of the mean.

# Calculate the mean of numbers greater than s.mean(). 
# Then calculate the mean of numbers less than s.mean().
# Is the average of these two numbers the same as s.mean()?
numbers_greater_than_mean = pd.Series(s.loc[s>s.mean()])
numbers_less_than_mean = pd.Series(s.loc[s<s.mean()])
print(numbers_greater_than_mean.describe())
print(numbers_less_than_mean.describe())
