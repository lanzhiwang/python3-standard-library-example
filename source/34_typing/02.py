def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception()
    return a + b


print(add(1, 2))

try:
    print(add(1.1, 2.2))
except Exception:
    print("Exception 1")

try:
    print(add("a", "b"))
except Exception:
    print("Exception 2")

try:
    print(add([1], [2]))
except Exception:
    print("Exception 3")


"""
$ python 02.py
3
Exception 1
Exception 2
Exception 3
$
"""
