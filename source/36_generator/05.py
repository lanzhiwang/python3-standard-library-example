def myrange(n):
    print("enter myrange")
    i = 0
    while i < n:
        yield i
        i += 1


result = myrange(3)
it = result.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

"""
$ python 05.py
enter myrange
0
1
2
Traceback (most recent call last):
  File "/python3-standard-library-example/source/36_generator/05.py", line 14, in <module>
    print(it.__next__())
StopIteration
$
"""
