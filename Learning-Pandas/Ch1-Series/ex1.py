import pandas as pd
import numpy as np
# Create a series of 10 elements, random integers from 70 to 100, representing scores on a monthly exam. 
# Set the index to be the month names, starting in September and ending in June.
# (If these months don’t match the school year in your location, feel free to make them more realistic.)
# With this series, write code to answer the following questions:
#  What is the student’s average test score for the entire year?
#  What is the student’s average test score during the first half of the year (i.e., the first five months)?
#  What is the student’s average test score during the second half of the year?
#  Did the student improve their performance in the second half? If so, by how much?
# In which month did this student get their highest score? 
# What were this student’s five highest scores?
# Round the student’s scores to the nearest 10. (A score of 82 would be rounded down to 80, but a score of 87 would be rounded up to 90.) Be sure to read the

#  Define a Pandas Series
s = pd.Series([10, 20, 30, 40, 50])

# Generate random numbers
g = np.random.default_rng()
a = g.integers(0, 100, 10)

# Define a series of random numbers
scores = pd.Series(np.random.randint(70, 101, 10))

# Set the index names
months = "Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May,Jun".split(",")
scores.index = months

# Yearly average
yearly_average = scores.mean()

# Average for each year halves
first_half = scores["Sep":"Jan"].mean()
second_half = scores.iloc[5:].mean()

# Student Improvement
score_differences = second_half-first_half

# Student sorted scores
sorted_scores = scores.sort_values(ascending=False)

# Rounded scores
rounded_scores = [round(i, -1) for i in list(scores)]
print(f"""
The scores are 
{scores}
Yearly Average is {yearly_average}
      """)

print(f"""
The scores for the first half of the year are 
{scores.iloc[:5]}
First half yearly average is {first_half}
      """)

print(f"""
The scores for the second half of the year are 
{scores["Feb":"Jun"]}
Second half yearly average is {second_half}
      """)

print(f"Student Improved by {score_differences}" if score_differences > 0 else f"Student Dropped by {score_differences}")

print(f"The student achieved the highest score ({scores.max()}) in the month of {scores.idxmax()}")

print(f"Students five highest scores were {list(sorted_scores.iloc[:5])}")

print(f"""
The students original scores is 
    {list(scores)}
While the rounded scores is 
    {rounded_scores})
""")
