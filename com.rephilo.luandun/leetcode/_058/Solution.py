def lengthOfLastWord1(s: str) -> int:
    arrays = s.split(" ")
    arrays = list(filter(lambda x: x != '', arrays))
    if len(arrays) > 0:
        return len(arrays[len(arrays) - 1])
    return 0


def lengthOfLastWord2(s: str) -> int:
    """
    这种快一点
    :param s:
    :return:
    """
    result = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            result = result + 1
        if s[i] == ' ' and result > 0:
            break
    return result
