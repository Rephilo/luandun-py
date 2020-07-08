from typing import List


def plusOne1(self, digits: List[int]) -> List[int]:
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    a = ""
    for i in digits:
        a += str(i)
    return list(map(int, str(int(a) + 1)))


def plusOne2(digits: List[int]) -> List[int]:
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            digits[i] = digits[i] + 1
            return digits
        digits[i] = 0
    newDigits = [0] * (len(digits) + 1)
    newDigits[0] = 1
    return newDigits
