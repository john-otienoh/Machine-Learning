import pandas as pd
import numpy as np
# When I was in high school and college, our instructors sometimes gave extremely hard tests. 
# Rather than fail most of the class, they would scale the test scores, known in some places as grading on a curve. 
# They would assume that the average test score should be 80, 
# calculate the difference between our actual mean and 80, and then add that difference to each of our scores.
# For this exercise, I want you to generate 10 test scores between 40 and 60, again
# using an index starting with September and ending with June. Find the mean of the
# scores and add the difference between the mean and 80 to each of the scores.

months = "Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May,Jun".split(",")
scores = pd.Series(np.random.randint(40, 61, 10), index=months)
print(f"The mean is {scores.mean()} while the median is {scores.median()} and the standard deviation is {scores.std()}")
print(scores)
scores += 80 - scores.mean()
print(scores)
