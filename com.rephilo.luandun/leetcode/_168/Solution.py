def convertToTitle(self, n: int) -> str:
    """
    10进制转26进制
    :param self:
    :param n:
    :return:
    """
    excelStr = ''
    while n > 0:
        n = n - 1
        x = n % 26
        n = n // 26
        excelStr = chr(x + 65) + excelStr
    return excelStr
