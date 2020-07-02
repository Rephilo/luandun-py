from typing import List


def searchInsert1(self, nums: List[int], target: int) -> int:
    """
    循环
    :param self:
    :param nums:
    :param target:
    :return:
    """
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def searchInsert2(self, nums: List[int], target: int) -> int:
    """
    二分
    确实时间短了一丢丢
    :param self:
    :param nums:
    :param target:
    :return:
    """
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
