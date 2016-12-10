def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

# ax2 + bx + c = 0

def quadratic(a, b, c):
    if not isinstance((a, b, c), (int, float)):
        raise TypeError('bad operand type')

    a * x * a * x + b * x + c = 0