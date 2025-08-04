from typing import List


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Store(object):
    def __init__(self, stock: List[Dog]):
        self.stock = stock

    def buy(self) -> Dog:
        return self.stock.pop()


wang = Store([Dog(), Dog()])
print(wang.buy())

li = Store([Cat(), Cat()])
print(li.buy())

"""
$ python 17.py
<__main__.Dog object at 0x7f4e572bf970>
<__main__.Cat object at 0x7f4e572bece0>
$
$ mypy 17.py
17.py:27: error: List item 0 has incompatible type "Cat"; expected "Dog"  [list-item]
17.py:27: error: List item 1 has incompatible type "Cat"; expected "Dog"  [list-item]
Found 2 errors in 1 file (checked 1 source file)
$

"""
