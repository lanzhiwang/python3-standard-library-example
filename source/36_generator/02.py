def myrange(n):
    i = 0
    result = []
    while i < n:
        result.append(i)
        i += 1
    return result


for i in myrange(3):
    print(i)

print(type(myrange(3)))

"""
$ python 02.py
0
1
2
<class 'list'>
$
"""
