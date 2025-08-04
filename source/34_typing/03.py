def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
print(add(1.1, 2.2))
print(add("a", "b"))
print(add([1], [2]))


"""
$ python 03.py
3
3.3000000000000003
ab
[1, 2]
$

$ mypy 03.py
03.py:6: error: Argument 1 to "add" has incompatible type "float"; expected "int"  [arg-type]
03.py:6: error: Argument 2 to "add" has incompatible type "float"; expected "int"  [arg-type]
03.py:7: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
03.py:7: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
03.py:8: error: Argument 1 to "add" has incompatible type "list[int]"; expected "int"  [arg-type]
03.py:8: error: Argument 2 to "add" has incompatible type "list[int]"; expected "int"  [arg-type]
Found 6 errors in 1 file (checked 1 source file)
$

"""
