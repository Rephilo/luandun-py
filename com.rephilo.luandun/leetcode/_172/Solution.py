class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        数一下出现了多少个5
        :param n:
        :return:
        """
        count = 0
        while n > 0:
            count += n // 5
            n = n // 5
        return count
