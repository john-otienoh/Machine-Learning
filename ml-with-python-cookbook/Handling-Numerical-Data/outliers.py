import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

features, _ = make_blobs(n_samples=10, n_features=2, centers=1, random_state=1)
features[0, 0] = 10000
features[0, 1] = 10000

outlier_detector = EllipticEnvelope(contamination=.1)
outlier_detector.fit(features)
outlier_detector.predict(features)

# Using IQR
feature = features[:,0]

def indices_of_outliers(x: int) -> np.array(int):
    "Return index of outliers"
    q1,q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return np.where((x > upper_bound) | (x < lower_bound))
# Run function
indices_of_outliers(feature)
