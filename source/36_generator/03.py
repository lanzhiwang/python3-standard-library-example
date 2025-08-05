class MyRange(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return MyRangeIter(self.n)


class MyRangeIter(object):
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration()
        result = self.current
        self.current += 1
        return result


for i in MyRange(3):
    print(i)

print(type(MyRange(3)))

"""
$ python 03.py
0
1
2
<class '__main__.MyRange'>
$
"""
