from typing import List


def removeElement1(nums: List[int], val: int) -> int:
    otherIndex = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[otherIndex] = nums[i]
            otherIndex = otherIndex + 1

    return otherIndex


def removeElement2(nums: List[int], val: int) -> int:
    """
    在循环的时候删除掉val，这种居然比循环还快。。
    :param nums:
    :param val:
    :return:
    """
    while val in nums:
        nums.remove(val)
    return len(nums)
