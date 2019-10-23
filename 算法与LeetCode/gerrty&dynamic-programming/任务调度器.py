from collections import defaultdict


def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    length = len(tasks)
    if length <= 1:
        return length

    tasks_map = defaultdict(int)
    for task in tasks:
        tasks_map[task] += 1
    tasks_map_sort = sorted(tasks_map.items(), key=lambda x: x[1], reverse=True)
    max_task_count = tasks_map_sort[0][1]       # 拿到出现次数最多的任务
    res = (max_task_count-1)*(n+1)              # 至少需要时间为（次数-1）*（n+1),还需要加上与出现最多次数相等的任务个数
                                                # 如果计算出的时间小于任务总个数，应返回任务的个数，因为每个任务需要一个单位时间

    for sort in tasks_map_sort:
        if sort[1] == max_task_count:
            res += 1

    return res if res >= length else length


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    leastInterval(tasks, n)