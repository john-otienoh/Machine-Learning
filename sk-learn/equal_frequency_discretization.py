import matplotlib as plt
import seaborn as sns
import numpy as np
import pandas as pd

# plt.rcParams("figure.figsize") == [8,6]
sns.set_style("darkgrid")

diamond_data = sns.load_dataset('diamonds')
discretised_price, bins = pd.qcut(diamond_data['price'], 10, labels=None, retbins=True, precision=3, duplicates='raise')
bin_labels = ['Bin_no_'+str(i) for i in range(1, 11)]
print(pd.concat([discretised_price, diamond_data['price']], axis=1).head())
diamond_data['price_bins'] = pd.cut(x=diamond_data['price'], bins=bins, labels=bin_labels, include_lowest=True)
print(discretised_price.head())
