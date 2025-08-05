import copy

def changelist(lst):
    lst.append(5)
    lst[0] = 6
    lst[-2][0] += 100
    print("lst:", lst)


l = [0, 1, 2, 3, 4, [10, 11, 12]]
print("l:", l)

changelist(copy.deepcopy(l))
print("l:", l)

"""
$ python 04.py
l: [0, 1, 2, 3, 4, [10, 11, 12]]
lst: [6, 1, 2, 3, 4, [110, 11, 12], 5]
l: [0, 1, 2, 3, 4, [10, 11, 12]]
$
"""
