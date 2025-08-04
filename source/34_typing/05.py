from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


print(add(1, 2))
print(add(1.1, 2.2))
print(add("a", "b"))
print(add([1], [2]))


"""
$ python 05.py
3
3.3000000000000003
ab
[1, 2]
$
$ mypy 05.py
05.py:10: error: Argument 1 to "add" has incompatible type "str"; expected "int | float"  [arg-type]
05.py:10: error: Argument 2 to "add" has incompatible type "str"; expected "int | float"  [arg-type]
05.py:11: error: Argument 1 to "add" has incompatible type "list[int]"; expected "int | float"  [arg-type]
05.py:11: error: Argument 2 to "add" has incompatible type "list[int]"; expected "int | float"  [arg-type]
Found 4 errors in 1 file (checked 1 source file)
$

"""
