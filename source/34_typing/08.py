Num = int | float


def add(a: Num, b: Num) -> Num:
    if a <= 0 or b <= 0:
        return None
    return a + b


print(add(1, 2))
print(add(1.1, 2.2))


"""
$ python 08.py
3
3.3000000000000003
$
$ mypy 08.py
08.py:6: error: Incompatible return value type (got "None", expected "int | float")  [return-value]
Found 1 error in 1 file (checked 1 source file)
$

"""
