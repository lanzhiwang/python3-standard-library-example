import random
import weakref

id_user = weakref.WeakValueDictionary()
user_id = weakref.WeakKeyDictionary()


class User(object):
    def __init__(self):
        self._id = random.randint(0, 1000)
        while self._id in id_user:
            self._id = random.randint(0, 1000)
        id_user[self._id] = self
        user_id[self] = self._id


def chat_room():
    u1 = User()
    u2 = User()
    print("chat_room u1:", u1)
    print("chat_room u2:", u2)

    for i, u in id_user.items():
        print(f"chat_room id_user {i} {u}")
    for i, u in user_id.items():
        print(f"chat_room user_id {i} {u}")
    print()


chat_room()
chat_room()

u = User()

for i, u in id_user.items():
    print(f"id_user {i} {u}")

for i, u in user_id.items():
    print(f"user_id {i} {u}")

"""
$ python 06.py
chat_room u1: <__main__.User object at 0x7fbb2c15cd00>
chat_room u2: <__main__.User object at 0x7fbb2c15d1b0>
chat_room id_user 381 <__main__.User object at 0x7fbb2c15cd00>
chat_room id_user 756 <__main__.User object at 0x7fbb2c15d1b0>
chat_room user_id <__main__.User object at 0x7fbb2c15cd00> 381
chat_room user_id <__main__.User object at 0x7fbb2c15d1b0> 756

chat_room u1: <__main__.User object at 0x7fbb2c15d1b0>
chat_room u2: <__main__.User object at 0x7fbb2c15cd00>
chat_room id_user 255 <__main__.User object at 0x7fbb2c15d1b0>
chat_room id_user 697 <__main__.User object at 0x7fbb2c15cd00>
chat_room user_id <__main__.User object at 0x7fbb2c15d1b0> 255
chat_room user_id <__main__.User object at 0x7fbb2c15cd00> 697

id_user 958 <__main__.User object at 0x7fbb2c15cd00>
user_id <__main__.User object at 0x7fbb2c15cd00> 958
$
"""
