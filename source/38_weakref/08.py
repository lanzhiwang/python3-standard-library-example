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

for i, u in id_user.items():
    print(f"id_user {i} {u}")

for i, u in user_id.items():
    print(f"user_id {i} {u}")

for i in s:
    print(f"s {i}")

print("u_ref:", u_ref())

"""
$ python 08.py
chat_room u1: <__main__.User object at 0x7f857528d570>
chat_room u2: <__main__.User object at 0x7f857528d5d0>
chat_room id_user 821 <__main__.User object at 0x7f857528d570>
chat_room id_user 443 <__main__.User object at 0x7f857528d5d0>
chat_room user_id <__main__.User object at 0x7f857528d570> 821
chat_room user_id <__main__.User object at 0x7f857528d5d0> 443
chat_room s <__main__.User object at 0x7f857528d5d0>
chat_room s <__main__.User object at 0x7f857528d570>

chat_room u1: <__main__.User object at 0x7f857528d570>
chat_room u2: <__main__.User object at 0x7f857528d5d0>
chat_room id_user 733 <__main__.User object at 0x7f857528d570>
chat_room id_user 545 <__main__.User object at 0x7f857528d5d0>
chat_room user_id <__main__.User object at 0x7f857528d570> 733
chat_room user_id <__main__.User object at 0x7f857528d5d0> 545
chat_room s <__main__.User object at 0x7f857528d5d0>
chat_room s <__main__.User object at 0x7f857528d570>

id_user 720 <__main__.User object at 0x7f857528d570>
user_id <__main__.User object at 0x7f857528d570> 720
s <__main__.User object at 0x7f857528d570>
u_ref: <__main__.User object at 0x7f857528d570>
$
"""
