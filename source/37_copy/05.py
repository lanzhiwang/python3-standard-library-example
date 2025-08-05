def changedict(dst):
    dst["key3"] = "value3"
    dst["key1"] = "value11"
    print("dst:", dst)


d = {"key1": "value1", "key2": "value2"}
print("d:", d)
changedict(d)
print("d:", d)

"""
$ python 05.py
d: {'key1': 'value1', 'key2': 'value2'}
dst: {'key1': 'value11', 'key2': 'value2', 'key3': 'value3'}
d: {'key1': 'value11', 'key2': 'value2', 'key3': 'value3'}
$
"""
