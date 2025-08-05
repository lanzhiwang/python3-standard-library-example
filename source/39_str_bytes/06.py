b1 = bytes([230, 138, 149, 229, 184, 129])
s1 = b1.decode("utf-8")
print("s1:", s1)
print("s1:", type(s1))

print()

s2 = "投币"
b2 = s2.encode("utf-8")
print("b2:", b2)
print("b2:", type(b2))
for i in b2:
    print(i, end=" ")
print()

"""
$ python 06.py
s1: 投币
s1: <class 'str'>

b2: b'\xe6\x8a\x95\xe5\xb8\x81'
b2: <class 'bytes'>
230 138 149 229 184 129
$
"""
