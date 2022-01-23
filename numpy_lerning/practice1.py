import numpy as np

my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print(my_array1)

my_list2 = [11,22,33,44]

my_lists = [my_list1,my_list2]

# 多次元アレイ
my_array2 = np.array(my_lists)
print(my_array2)

# アレイのサイズを調べる
print(my_array2.shape)
# アレイのデータ型を調べる
print(my_array2.dtype)

# npによるアレイ生成
my_zero_array = np.zeros(5)
print(my_zero_array)
print(my_zero_array.dtype)
print(np.ones((5,5)))

# 空っぽのアレイ
print(np.empty(5))
print(np.empty((3,4)))

# 単位行列
print(np.eye(5))

#arange関数
print(np.arange(5))
print(np.arange(5,50,2))