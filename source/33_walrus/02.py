l = [1, 2, 3]

if len(l) > 0:
    print(f"len1: {len(l)}")
# len(l) 计算了两次

# 只计算一次 len(l)
lenght1 = len(l)
if lenght1 > 0:
    print(f"len2: {lenght1}")

# 变量 lenght 只在 if 中用到, 多出一行代码 lenght = len(l)

if (lenght2 := len(l)) > 0:
    print(f"len3: {lenght2}")

print(f"len4: {lenght2}")

"""
$ python 02.py
len1: 3
len2: 3
len3: 3
len4: 3
$
"""
