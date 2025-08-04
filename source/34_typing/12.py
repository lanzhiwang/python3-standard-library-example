from typing import List

Num = int | float

num_list: List[Num] = [1, 2, 3, 1.1, 2.2]
int_list: List[int] = [4, 5, 6]


def print_num_list(l: List[Num]) -> None:
    for n in l:
        print(n)


print_num_list(num_list)
print()
print_num_list(int_list)

"""
$ python 12.py
1
2
3
1.1
2.2

4
5
6
$
$ mypy 12.py
12.py:16: error: Argument 1 to "print_num_list" has incompatible type "list[int]"; expected "list[int | float]"  [arg-type]
12.py:16: note: "list" is invariant -- see https://mypy.readthedocs.io/en/stable/common_issues.html#variance
12.py:16: note: Consider using "Sequence" instead, which is covariant
Found 1 error in 1 file (checked 1 source file)
$

"""
