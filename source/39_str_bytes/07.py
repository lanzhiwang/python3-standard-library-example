utf_8 = bytes([230, 138, 149, 229, 184, 129])
s1 = utf_8.decode("utf-8")
print("s1:", s1)
print("s1:", type(s1))

gb2312 = bytes([205, 182, 177, 210])
s2 = gb2312.decode("gb2312")
print("s2:", s2)
print("s2:", type(s2))


"""
$ python 07.py
s1: 投币
s1: <class 'str'>
s2: 投币
s2: <class 'str'>
$
"""
