import matplotlib as plt
import seaborn as sns
import numpy as np
import pandas as pd

# plt.rcParams("figure.figsize") == [8,6]
sns.set_style("darkgrid")

diamond_data = sns.load_dataset('diamonds')
sns.displot(diamond_data['price'])
price_range = diamond_data['price'].max() - diamond_data['price'].min()

lower_interval = int(np.floor(diamond_data['price'].min()))
upper_interval = int(np.ceil(diamond_data['price'].max()))
interval_length = int(np.round(price_range/10))
total_bins = [i for i in range(lower_interval, upper_interval+interval_length, interval_length)]
bin_labels = ['Bin_no_' + str(i) for i in range(1, len(total_bins))]
diamond_data['price_bins'] = pd.cut(x=diamond_data['price'], bins=total_bins, labels=bin_labels, include_lowest=True)
print(diamond_data.head())
