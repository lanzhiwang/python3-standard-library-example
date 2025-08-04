from typing import List, Sequence

Num = int | float

num_list: List[Num] = [1, 2, 3, 1.1, 2.2]
int_list: List[int] = [4, 5, 6]


def print_num_list(l: Sequence[Num]) -> None:
    for n in l:
        print(n)


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
$ python 15.py
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

4
5
6

4
5
6
$
$ mypy 15.py
Success: no issues found in 1 source file
$

"""
