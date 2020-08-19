from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        双指针查找
        :param numbers:
        :param target:
        :return:
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp == target:
                return [left + 1, right + 1]
            elif tmp > target:
                right -= 1
            else:
                left += 1
        return [0, 0]
