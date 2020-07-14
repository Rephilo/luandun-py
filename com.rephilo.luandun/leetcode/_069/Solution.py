import math


def mySqrt1(x: int) -> int:
    """
    内置函数
    :param x:
    :return:
    """
    return int(math.sqrt(x))


def mySqrt2(x: int) -> int:
    """
    二分查找法
    :param x:
    :return:
    """
    left = 0
    right = x
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        currX = mid * mid
        if currX <= x:
            result = mid
            left = mid + 1
        elif currX > x:
            right = mid - 1
    return result
