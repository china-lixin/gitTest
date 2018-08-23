# -*- coding: utf-8 -*
'''
import numpy as np  # 一般以np作为numpy的别名

a = np.array([2, 0, 1])  # 创建数组
print(a)  # 输出数组
# print(a[0:3])
#  引用前三个数字（切片）
# print(a.min())
#  输出a的最小值
# a.sort()
#  将a的元素从小到大排序，此操作直接修改a，因此这时候a为[0, 1, 2, 5]
# print(a)
b = np.array([[1, 2, 3], [4, 5, 6]])  # 创建二维数组
print(b)
# print(b * b)
#  输出数组的平方阵，即[[1, 4, 9], [16, 25, 36]]
print(a*b)
'''
# -*- coding: utf-8 -*
# 求解非线性方程组2x1-x2^2=1,x1^2-x2=2
from scipy.optimize import fsolve  # 导入求解方程组的函数
from scipy import integrate  # 导入积分函数
import numpy as np
import matplotlib.pyplot as plt


# 求解方程组
def f(x):  # 定义要求解的方程组
    x1 = x[0]
    x2 = x[1]
    return [2 * x1 - x2 ** 2 - 1, x1 ** 2 - x2 - 2]


result = fsolve(f, [1, 2])  # 输入初值[1, 1]并求解
print(result)  # 输出结果，为array([ 1.91963957,  1.68501606])


# 数值积分
def g(x):  # 定义被积函数
    return (1 - x ** 2) ** 0.5


pi_2, err = integrate.quad(g, -1, 1)  # 积分结果和误差
print(pi_2 * 2)  # 由微积分知识知道积分结果为圆周率pi的一半


y = np.linspace(-2, 2, num=20)
y_int = integrate.cumtrapz(y)
plt.plot(y_int, 'ro', y, 'b-')
plt.show()