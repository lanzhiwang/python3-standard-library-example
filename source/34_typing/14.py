from typing import List, Sequence

Num = int | float

num_list: List[Num] = [1, 2, 3, 1.1, 2.2]
int_list: List[int] = [4, 5, 6]


def print_num_list(l: Sequence[Num]) -> None:
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
$ python 14.py
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
$ mypy 14.py
14.py:12: error: "Sequence[int | float]" has no attribute "append"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)
$

"""
