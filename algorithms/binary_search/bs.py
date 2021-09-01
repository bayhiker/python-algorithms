from bisect import bisect, bisect_left, bisect_right
def bs_bisect(a, x):
    ins_point = bisect_left(a, x)
    if ins_point != len(a) and a[ins_point] == x:
        return ins_point
    else:
        return -1
