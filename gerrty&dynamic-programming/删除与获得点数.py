def deleteAndEarn(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counts = {}
    for i in nums:
        counts[i] = counts.get(i, 0)+i
    res_list = [0]
    key_set = set()

    for k,v in sorted(counts.items()):
        if k-1 not in key_set:
            key_set.add(k)
            res_list.append(res_list[-1] + v)
        else:
            key_set.add(k)
            res_list.append(max(res_list[-2] + v, res_list[-1]))
    return res_list[-1]


if __name__ == '__main__':
    print(deleteAndEarn([3,4,2]))