def myrange(n):
    print("enter myrange")
    i = 0
    while i < n:
        value = yield i
        print("value:", value)
        i += 1


result = myrange(3)
it = result.__iter__()
print(it.__next__())
print(result.send("helloworld1"))
print(result.send("helloworld2"))

"""
$ python 07.py
enter myrange
0
value: helloworld1
1
value: helloworld2
2
$
"""
