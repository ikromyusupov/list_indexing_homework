def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    if list1[0] == 1:
        list1[0] = True
    else:
        list1[0] = False
    if list1[1] == 1:
        list1[1] = True
    else:
        list1[1] = False
    if list1[2] == 1:
        list1[2] = True
    else:
        list1[2] = False
    if list1[3] == 1:
        list1[3] = True
    else:
        list1[3] = False
    if list1[4] == 1:
        list1[4] = True
    else:
        list1[4] = False
    return list1