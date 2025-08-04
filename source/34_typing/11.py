from typing import List

Num = int | float

num_list: List[Num] = [1, 2, 3, 1.1, 2.2]


def print_num_list(l: List[Num]) -> None:
    for n in l:
        print(n)


print_num_list(num_list)


"""
$ python 11.py
1
2
3
1.1
2.2
$
$ mypy 11.py
Success: no issues found in 1 source file
$

"""
