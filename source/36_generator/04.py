def myrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in myrange(3):
    print(i)

print(type(myrange(3)))

"""
$ python 04.py
0
1
2
<class 'generator'>
$
"""
