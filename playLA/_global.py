# _global.py存储项目中需要用到的全局变量

# 数值精度
EPSILON = 1e-8


def is_zero(x):
    return abs(x) < EPSILON


def is_equal(a, b):
    return abs(a - b) < EPSILON
