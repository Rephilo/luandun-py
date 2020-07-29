from typing import List


def merge0(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    数组拼接然后排序
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    nums1[:] = sorted(nums1[:m] + nums2)


def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    双指针正向排序
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    nums1_copy = nums1[:m]
    nums1[:] = []

    i = 0
    j = 0

    while i < m or j < n:
        if i >= m:
            currNum = nums2[j]
            j += 1
        elif j >= n:
            currNum = nums1_copy[i]
            i += 1
        elif nums2[j] < nums1_copy[i]:
            currNum = nums2[j]
            j += 1
        else:
            currNum = nums1_copy[i]
            i += 1
        nums1.append(currNum)


def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    双指针倒向排序（学一下官方的写法）
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    nums1[:p2 + 1] = nums2[:p2 + 1]
