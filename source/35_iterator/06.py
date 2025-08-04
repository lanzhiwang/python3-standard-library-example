class MyList(object):
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return MyListIterator(self)


class MyListIterator(object):
    def __init__(self, my_list: MyList):
        self.my_list = my_list
        self.index = 0

    def __next__(self):
        if self.index >= len(self.my_list.lst):
            raise StopIteration()
        result = self.my_list.lst[self.index]
        self.index += 1
        return result


my_list = MyList([1, 2, 3])
# it = my_list.__iter__()
it = iter(my_list)
for i in it:
    print(i)


"""
$ python 06.py
Traceback (most recent call last):
  File "/python3-standard-library-example/source/35_iterator/06.py", line 25, in <module>
    for i in it:
TypeError: 'MyListIterator' object is not iterable
$
"""
