import random

id_user = {}


class User(object):
    def __init__(self):
        self._id = random.randint(0, 1000)
        while self._id in id_user:
            self._id = random.randint(0, 1000)
        id_user[self._id] = self


def chat_room():
    u1 = User()
    u2 = User()
    print("chat_room u1:", u1)
    print("chat_room u2:", u2)

    for i, u in id_user.items():
        print(f"chat_room {i} {u}")
    print()

    del id_user[u1._id]
    del id_user[u2._id]


chat_room()
chat_room()

for i, u in id_user.items():
    print(f"{i} {u}")

"""
$ python 02.py
chat_room u1: <__main__.User object at 0x7f8d7ee6ffd0>
chat_room u2: <__main__.User object at 0x7f8d7ee6ff10>
chat_room 662 <__main__.User object at 0x7f8d7ee6ffd0>
chat_room 526 <__main__.User object at 0x7f8d7ee6ff10>

chat_room u1: <__main__.User object at 0x7f8d7ee6ff10>
chat_room u2: <__main__.User object at 0x7f8d7ee6ffd0>
chat_room 877 <__main__.User object at 0x7f8d7ee6ff10>
chat_room 775 <__main__.User object at 0x7f8d7ee6ffd0>

$
"""
