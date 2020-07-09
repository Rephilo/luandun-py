def addBinary(self, a: str, b: str) -> str:
    """
    试试直接转换
    :param self:
    :param a:
    :param b:
    :return:
    """
    return '{0:b}'.format(int(a, 2) + int(b, 2))


def addBinary1(a: str, b: str) -> str:
    """
    模拟加法,这种居然不如直接转换快。。。
    :param self:
    :param a:
    :param b:
    :return:
    """
    totalLength = max(len(a), len(b))
    carry = 0
    result = ''
    for i in range(1, totalLength + 1):
        currA = 0
        currB = 0
        if len(a) - i >= 0:
            currA = int(a[len(a) - i])
        if len(b) - i >= 0:
            currB = int(b[len(b) - i])

        currResult = currA + currB + carry
        carry = currResult // 2
        result += str(currResult % 2)

    if carry > 0:
        result += str(carry)

    return result[::-1]
