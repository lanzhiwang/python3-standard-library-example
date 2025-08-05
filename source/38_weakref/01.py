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


chat_room()
chat_room()

for i, u in id_user.items():
    print(f"{i} {u}")

"""
$ python 01.py
chat_room u1: <__main__.User object at 0x7f6c575cffd0>
chat_room u2: <__main__.User object at 0x7f6c575cfee0>
chat_room 384 <__main__.User object at 0x7f6c575cffd0>
chat_room 403 <__main__.User object at 0x7f6c575cfee0>

chat_room u1: <__main__.User object at 0x7f6c575f9c30>
chat_room u2: <__main__.User object at 0x7f6c575f9a80>
chat_room 384 <__main__.User object at 0x7f6c575cffd0>
chat_room 403 <__main__.User object at 0x7f6c575cfee0>
chat_room 312 <__main__.User object at 0x7f6c575f9c30>
chat_room 912 <__main__.User object at 0x7f6c575f9a80>

384 <__main__.User object at 0x7f6c575cffd0>
403 <__main__.User object at 0x7f6c575cfee0>
312 <__main__.User object at 0x7f6c575f9c30>
912 <__main__.User object at 0x7f6c575f9a80>
$
"""
