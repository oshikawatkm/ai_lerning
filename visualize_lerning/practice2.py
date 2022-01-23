from re import A
from turtle import color
import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


dataset = randn(25)
sns.rugplot(dataset)
plt.ylim(0,1)

plt.hist(dataset, alpha=0.3)
sns.rugplot(dataset)

x_min = dataset.min() - 2
x_max = dataset.max() + 2

x_axis = np.linspace(x_min,x_max,100)
bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


kernel_list = []

for data_point in dataset:
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)
sum_of_kde = np.sum(kernel_list,axis=0)
flg = plt.plot(x_axis,sum_of_kde,color='indianred')
sns.rugplot(dataset,c='indianred')
plt.yticks([])
plt.suptitle("Sum of the Basis Functions")

sns.kdeplot(dataset)




plt.show()