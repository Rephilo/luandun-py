from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[uniq]:
                uniq = uniq + 1
                nums[uniq] = nums[i]

        return uniq + 1
