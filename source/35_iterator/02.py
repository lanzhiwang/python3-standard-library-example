class MyList(object):
    def __init__(self, lst):
        self.lst = lst


my_list = MyList([1, 2, 3])
for i in my_list:
    print(i)

"""
$ python 02.py
Traceback (most recent call last):
  File "/python3-standard-library-example/source/35_iterator/02.py", line 6, in <module>
    for i in my_list:
TypeError: 'MyList' object is not iterable
$
"""
