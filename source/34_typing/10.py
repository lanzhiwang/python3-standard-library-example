from typing import Optional

Num = int | float


def add(a: Num, b: Num) -> Optional[Num]:
    if a <= 0 or b <= 0:
        return None
    return a + b


print(add(1, 2))
print(add(1.1, 2.2))


"""
$ python 10.py
3
3.3000000000000003
$
$ mypy 10.py
Success: no issues found in 1 source file
$

"""
