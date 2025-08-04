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
it = my_list.__iter__()
try:
    while True:
        i = it.__next__()
        print(i)
except StopIteration:
    pass

my_list = MyList([4, 5, 6])
for i in my_list:
    print(i)

"""
$ python 05.py
1
2
3
4
5
6
$
"""
