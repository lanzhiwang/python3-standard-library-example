from typing import List

Num = int | float

num_list: List[Num] = [1, 2, 3, 1.1, 2.2]
int_list: List[int] = [4, 5, 6]


def print_num_list(l: List[Num]) -> None:
    for n in l:
        print(n)
    l.append(7.7)


print_num_list(num_list)
print()
for i in num_list:
    print(i)

print()

print_num_list(int_list)
print()
for i in int_list:
    print(i)

"""
$ python 13.py
1
2
3
1.1
2.2

1
2
3
1.1
2.2
7.7

4
5
6

4
5
6
7.7
$
$ mypy 13.py
13.py:20: error: Argument 1 to "print_num_list" has incompatible type "list[int]"; expected "list[int | float]"  [arg-type]
13.py:20: note: "list" is invariant -- see https://mypy.readthedocs.io/en/stable/common_issues.html#variance
13.py:20: note: Consider using "Sequence" instead, which is covariant
Found 1 error in 1 file (checked 1 source file)
$

"""
