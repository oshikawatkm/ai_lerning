import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

dataset1 = randn(100)
# print(plt.hist(dataset1))

dataset2 = randn(80)
# plt.hist(dataset2, color='indianred')


plt.hist(dataset1,alpha=0.5,bins=20)
plt.hist(dataset2,alpha=0.5,bins=20, color='indianred')
# plt.show()

data1 = randn(1000)
data2 = randn(1000)

# sns.jointplot(data1, data2)
sns.jointplot(data1,data2,kind='hex')
plt.show()