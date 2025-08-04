class MyList(object):
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, index):
        return self.lst[index]


my_list = MyList([1, 2, 3])
for i in my_list:
    print(i)

"""
$ python 03.py
1
2
3
$
"""
