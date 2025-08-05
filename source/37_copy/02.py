import copy

def changelist(lst):
    lst.append(5)
    lst[0] = 6
    print("lst:", lst)


l = [0, 1, 2, 3, 4]
print("l:", l)

changelist(copy.copy(l))
print("l:", l)

"""
$ python 02.py
l: [0, 1, 2, 3, 4]
lst: [6, 1, 2, 3, 4, 5]
l: [0, 1, 2, 3, 4]
$
"""
