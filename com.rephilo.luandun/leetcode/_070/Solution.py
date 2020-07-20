def climbStairs0(self, n: int) -> int:
    """
    LeetCode上运行过不去，本地可以，self参数没法处理
    :param self:
    :param n:
    :return:
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(self, n - 1) + climbStairs(self, n - 2)


def climbStairs(self, n: int) -> int:
    """
    动态规划方案
    :param self:
    :param n:
    :return:
    """
    a = 0
    b = 0
    result = 1
    for i in range(n):
        a = b
        b = result
        result = a + b
    return result
