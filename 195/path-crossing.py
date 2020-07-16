# coding: utf-8
# Author：Brent
# Date ：2020/6/28 11:24 AM
# Tool ：PyCharm
# Describe ：
import collections


def isPathCrossing(path) -> bool:
    map_ = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    path_dict = collections.defaultdict(int)
    start = (0, 0)
    for step in path:
        value = map_[step]
        tmp_x = start[0] + value[0]
        tmp_y = start[1] + value[1]
        start = (tmp_x, tmp_y)
        if start in path_dict: return True
        path_dict[tuple(start)] += 1
        if tmp_x == 0 and tmp_y == 0:
            return True
    return False


def isPathCrossing_1(path):
    """
    :type path: str
    :rtype: bool
    : Hash map
    """
    if len(path) == 0: return False
    # 定义两个hash表
    nsew_dict = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    # 原点
    offset = (0, 0)
    offset_array = [offset]
    for index in path:
        offset = (offset[0] + nsew_dict[index][0], offset[1] + nsew_dict[index][1])
        if offset in offset_array:
            return True
        else:
            offset_array.append(offset)
    return False


if __name__ == '__main__':
    isPathCrossing_1("NES")
