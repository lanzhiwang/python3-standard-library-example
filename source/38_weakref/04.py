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

for i, u in id_user.items():
    print(f"{i} {u}")

"""
$ python 04.py
chat_room u1: <__main__.User object at 0x7fa984a47ee0>
chat_room u2: <__main__.User object at 0x7fa984a70ca0>
chat_room 697 <__main__.User object at 0x7fa984a47ee0>
chat_room 281 <__main__.User object at 0x7fa984a70ca0>

chat_room u1: <__main__.User object at 0x7fa984a47ee0>
chat_room u2: <__main__.User object at 0x7fa984a70fd0>
chat_room 86 <__main__.User object at 0x7fa984a47ee0>
chat_room 276 <__main__.User object at 0x7fa984a70fd0>

887 <__main__.User object at 0x7fa984a47ee0>
$
"""
