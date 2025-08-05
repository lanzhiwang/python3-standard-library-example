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

for i, u in id_user.items():
    print(f"id_user {i} {u}")

for i, u in user_id.items():
    print(f"user_id {i} {u}")

for i in s:
    print(f"s {i}")

"""
$ python 07.py
chat_room u1: <__main__.User object at 0x7f2a391f55a0>
chat_room u2: <__main__.User object at 0x7f2a391f5600>
chat_room id_user 774 <__main__.User object at 0x7f2a391f55a0>
chat_room id_user 877 <__main__.User object at 0x7f2a391f5600>
chat_room user_id <__main__.User object at 0x7f2a391f55a0> 774
chat_room user_id <__main__.User object at 0x7f2a391f5600> 877
chat_room s <__main__.User object at 0x7f2a391f5600>
chat_room s <__main__.User object at 0x7f2a391f55a0>

chat_room u1: <__main__.User object at 0x7f2a391f55a0>
chat_room u2: <__main__.User object at 0x7f2a391f5600>
chat_room id_user 674 <__main__.User object at 0x7f2a391f55a0>
chat_room id_user 114 <__main__.User object at 0x7f2a391f5600>
chat_room user_id <__main__.User object at 0x7f2a391f55a0> 674
chat_room user_id <__main__.User object at 0x7f2a391f5600> 114
chat_room s <__main__.User object at 0x7f2a391f5600>
chat_room s <__main__.User object at 0x7f2a391f55a0>

id_user 962 <__main__.User object at 0x7f2a391f55a0>
user_id <__main__.User object at 0x7f2a391f55a0> 962
s <__main__.User object at 0x7f2a391f55a0>
$
"""
