from typing import Union

Num = Union[int, float]


def add(a: Num, b: Num) -> Num:
    return a + b


print(add(1, 2))
print(add(1.1, 2.2))
print(add("a", "b"))
print(add([1], [2]))


"""
$ python 06.py
3
3.3000000000000003
ab
[1, 2]
$
$ mypy 06.py
06.py:12: error: Argument 1 to "add" has incompatible type "str"; expected "int | float"  [arg-type]
06.py:12: error: Argument 2 to "add" has incompatible type "str"; expected "int | float"  [arg-type]
06.py:13: error: Argument 1 to "add" has incompatible type "list[int]"; expected "int | float"  [arg-type]
06.py:13: error: Argument 2 to "add" has incompatible type "list[int]"; expected "int | float"  [arg-type]
Found 4 errors in 1 file (checked 1 source file)
$

"""
