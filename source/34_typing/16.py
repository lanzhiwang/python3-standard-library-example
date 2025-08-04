from typing import List


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Store(object):
    def __init__(self, stock: List[Animal]):
        self.stock = stock

    def buy(self) -> Animal:
        return self.stock.pop()


wang = Store([Dog(), Cat()])
print(wang.buy())

"""
$ python 16.py
<__main__.Cat object at 0x7f2b0445b6a0>
$
$ mypy 16.py
Success: no issues found in 1 source file
$
"""
