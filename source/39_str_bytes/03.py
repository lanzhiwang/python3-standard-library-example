b1 = bytes([0, 1, 2, 3, 97, 254, 255])
b2 = bytes([0, 1, 2, 3, 97, 254, 255, 256])


"""
$ python 03.py
Traceback (most recent call last):
  File "/python3-standard-library-example/source/39_str_bytes/03.py", line 2, in <module>
    b2 = bytes([0, 1, 2, 3, 97, 254, 255, 256])
ValueError: bytes must be in range(0, 256)
$
"""
