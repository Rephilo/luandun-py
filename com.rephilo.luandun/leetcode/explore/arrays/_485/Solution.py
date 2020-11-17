class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        result = 0
        maxResult = 0
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num == 1:
                result = result + 1
            else:
                maxResult = max(result, maxResult)
                result = 0
        return max(maxResult, result)
