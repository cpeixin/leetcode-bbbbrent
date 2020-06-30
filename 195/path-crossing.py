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


if __name__ == '__main__':
    isPathCrossing("SS")