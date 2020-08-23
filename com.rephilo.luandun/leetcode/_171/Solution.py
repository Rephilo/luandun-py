class Solution:
    def titleToNumber(self, s: str) -> int:
        """
        26进制转10进制
        :param s:
        :return:
        """
        res = 0
        for i in range(-1, -len(s) - 1, -1):
            res = res + 26 ** (-(i + 1)) * (ord(s[i]) - 64)
        return res
