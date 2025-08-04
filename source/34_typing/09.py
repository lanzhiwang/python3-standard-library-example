Num = int | float


def add(a: Num, b: Num) -> Num | None:
    if a <= 0 or b <= 0:
        return None
    return a + b


print(add(1, 2))
print(add(1.1, 2.2))


"""
$ python 09.py
3
3.3000000000000003
$
$ mypy 09.py
Success: no issues found in 1 source file
$

"""
