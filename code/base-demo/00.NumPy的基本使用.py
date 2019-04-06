import numpy as np

# 生成 NumPy数组
x = np.array([1.0,2.0,3.0])
print(x)
print(type(x))

#输出
#[1. 2. 3.]
#<class 'numpy.ndarray'>

# 算术运算
# 注意x和y的元素个数是相同的，如果不相同并进行计算会报错
y = np.array([2.0,4.0,6.0])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
# 输出
# [3. 6. 9.]
# [-1. -2. -3.]
# [ 2.  8. 18.]
# [0.5 0.5 0.5]

# 广播 对数组和标量之间进行计算
print(x/2)

# 输出
# [0.5 1.  1.5]

# 生成N维数组
A = np.array([[1,2,3],[3,4,5]])
print(A)
# 输出矩阵的外形，如2*2的矩阵 行*列
print(A.shape)
# 输出矩阵元素的类型
print(A.dtype)

# 输出
# [[1 2 3]
#  [3 4 5]]
# (2, 3)
# int32

# 矩阵也有广播操作
print(A/2)
# 输出
# [[0.5 1.  1.5]
#  [1.5 2.  2.5]]

# 广播的本质
C = np.array([[1,2],[3,4]])
D = np.array([10,20])
print(C*D)

# 输出 NumPy会将[10,20] 扩展为[[10,20],[10,20]]
# [[10 40]
#  [30 80]]

E = np.array([[10],[20]])
print(C*E)
# [[10 20]
#  [60 80]]

# 访问元素
print(C[0]) # 访问第1行
# [1 2]
print(C[0][1]) # 访问第1行第2个元素
# 2

for row in C:
    print(row)
# [1 2]
# [3 4]

# 将二维数组转换为1维数组
c = C.flatten()
print(c)
# [1 2 3 4]

# 获取索引为0 1 3 的元素
print(c[np.array([0,1,3])])
# [1 2 4]

# 大于2的元素列表情况
print(c>2)
# [False False  True  True]
# 使用此列表可以输出对应的元素
print(c[c>2])
# [3 4]