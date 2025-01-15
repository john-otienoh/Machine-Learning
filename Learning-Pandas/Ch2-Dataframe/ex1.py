import pandas as pd
import numpy as np
import matplotlib

# CSV to Pandas Dataframe
df = pd.read_csv("/home/outis/outis_codes/Tech_Boy/Machine-Learning/datasets/car_data.csv")
random_df = pd.DataFrame(np.random.rand(20,3))

# print(df.head())
# print(df.value_counts("car_brand"))
df["New"] = 123
print(df.describe)
