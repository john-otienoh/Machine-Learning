import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer

features = np.array([[2, 3],
[2, 3],
[2, 3]])
# Define a simple function
def add_ten(x: int) -> int:
    return x + 10
# Create transformer
ten_transformer = FunctionTransformer(add_ten)
# Transform feature matrix
ten_transformer.transform(features)

df = pd.DataFrame(features, columns=["feature_1", "feature_2"])
# Apply function
df.apply(add_ten)
