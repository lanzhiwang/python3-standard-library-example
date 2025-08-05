import random
import weakref

id_user = weakref.WeakValueDictionary()
user_id = weakref.WeakKeyDictionary()
s = weakref.WeakSet()


class User(object):
    def __init__(self):
        self._id = random.randint(0, 1000)
        while self._id in id_user:
            self._id = random.randint(0, 1000)
        id_user[self._id] = self
        user_id[self] = self._id
        s.add(self)


def chat_room():
    u1 = User()
    u2 = User()
    print("chat_room u1:", u1)
    print("chat_room u2:", u2)

    for i, u in id_user.items():
        print(f"chat_room id_user {i} {u}")
    for i, u in user_id.items():
        print(f"chat_room user_id {i} {u}")
    for i in s:
        print(f"chat_room s {i}")
    print()


chat_room()
chat_room()

u = User()
u_ref = weakref.ref(u)
u = None

for i, u in id_user.items():
    print(f"id_user {i} {u}")

for i, u in user_id.items():
    print(f"user_id {i} {u}")

for i in s:
    print(f"s {i}")

print("u_ref:", u_ref())

"""
$ python 09.py
chat_room u1: <__main__.User object at 0x7f8d2136d570>
chat_room u2: <__main__.User object at 0x7f8d2136d5d0>
chat_room id_user 624 <__main__.User object at 0x7f8d2136d570>
chat_room id_user 702 <__main__.User object at 0x7f8d2136d5d0>
chat_room user_id <__main__.User object at 0x7f8d2136d570> 624
chat_room user_id <__main__.User object at 0x7f8d2136d5d0> 702
chat_room s <__main__.User object at 0x7f8d2136d5d0>
chat_room s <__main__.User object at 0x7f8d2136d570>

chat_room u1: <__main__.User object at 0x7f8d2136d570>
chat_room u2: <__main__.User object at 0x7f8d2136d5d0>
chat_room id_user 145 <__main__.User object at 0x7f8d2136d570>
chat_room id_user 405 <__main__.User object at 0x7f8d2136d5d0>
chat_room user_id <__main__.User object at 0x7f8d2136d570> 145
chat_room user_id <__main__.User object at 0x7f8d2136d5d0> 405
chat_room s <__main__.User object at 0x7f8d2136d5d0>
chat_room s <__main__.User object at 0x7f8d2136d570>

u_ref: None
$
"""
