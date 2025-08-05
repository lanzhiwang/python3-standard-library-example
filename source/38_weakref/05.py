import random
import weakref

id_user = weakref.WeakValueDictionary()


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

u = User()
u = None

for i, u in id_user.items():
    print(f"{i} {u}")

"""
$ python 05.py
chat_room u1: <__main__.User object at 0x7f14b02cfee0>
chat_room u2: <__main__.User object at 0x7f14b02f8ca0>
chat_room 502 <__main__.User object at 0x7f14b02cfee0>
chat_room 801 <__main__.User object at 0x7f14b02f8ca0>

chat_room u1: <__main__.User object at 0x7f14b02cfee0>
chat_room u2: <__main__.User object at 0x7f14b02f8fd0>
chat_room 991 <__main__.User object at 0x7f14b02cfee0>
chat_room 239 <__main__.User object at 0x7f14b02f8fd0>

$
"""
