while True:
    cmd = input()
    if cmd == "exit":
        break
    print(f"Got1 input {cmd}")


while (cmd := input()) != "exit":
    print(f"Got2 input {cmd}")

"""
$ python 03.py
qwe
Got1 input qwe
asd
Got1 input asd
zxc
Got1 input zxc
exit
qwe
Got2 input qwe
asd
Got2 input asd
zxc
Got2 input zxc
exit
$
"""
