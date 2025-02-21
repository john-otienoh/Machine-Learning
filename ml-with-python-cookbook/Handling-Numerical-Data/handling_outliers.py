import pandas as pd
import numpy as np

houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032]
houses['Bathrooms'] = [2, 3.5, 2, 116]
houses['Square_Feet'] = [1500, 2500, 1500, 48000]

# Filter observations
houses[houses['Bathrooms'] < 20]

# Create feature based on boolean condition
houses["Outlier"] = np.where(houses['Bathrooms'] < 20, 0, 1)

# log feature
houses["Log_Of_Square_Feet"] = [np.log(x) for x in houses['Square_Feet']]