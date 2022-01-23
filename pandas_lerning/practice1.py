import numpy as np
import pandas as pd
from pandas import Series,DataFrame

obj = Series([3,6,9,12])
print(obj)
print(obj.index)


ww2_cas = Series([8700000, 430000, 300000, 210000, 400000], index=['USSR', 'Germany', 'Chine', 'Japan', 'USA'])
print(ww2_cas)
print(ww2_cas['USA'])

# 400万人以上の死者数をだした国
print(ww2_cas[ww2_cas>4000000])


ww2_dict = ww2_cas.to_dict()
print(ww2_dict)

WW2_Series = Series(ww2_dict)
print(WW2_Series)

countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']
obj2 = Series(ww2_dict, index=countries)
print(obj2)

print(pd.isnull(obj2))
print(pd.notnull(obj2))

obj2.name = '第二次世界大戦'
obj2.index.name = 'Countries'
print(obj2)