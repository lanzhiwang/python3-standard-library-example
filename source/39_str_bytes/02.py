b = bytes([0, 1, 2, 3, 97, 254])

print("b:", b)
print("b:", type(b))
print(b[0], type(b[0]))

"""
$ python 02.py
b: b'\x00\x01\x02\x03a\xfe'
b: <class 'bytes'>
0 <class 'int'>
$
"""
