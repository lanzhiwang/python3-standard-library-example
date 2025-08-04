l = [2, 4, 6, 7, 10]

is_even1 = True
for i in l:
    if i % 2 != 0:
        is_even1 = False
        break
print(is_even1)

print(all(i % 2 == 0 for i in l))
is_even2 = all(i % 2 == 0 for i in l)
print(is_even2)

is_even3 = all((n := i) % 2 == 0 for i in l)
print(is_even3)
print(n)

is_even4 = all((n := i) % 2 == 0 for i in [2, 4, 6, 8, 10])
print(is_even4)
print(n)

"""
$ python 04.py
False
False
False
False
7
True
10
$
"""
