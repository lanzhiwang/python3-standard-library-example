from typing import List, TypeVar, Generic


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


AnimalType = TypeVar("AnimalType")


class Store(Generic[AnimalType]):
    def __init__(self, stock: List[AnimalType]):
        self.stock = stock

    def buy(self) -> AnimalType:
        return self.stock.pop()


wang = Store[Dog]([Dog(), Dog()])
print(wang.buy())

li = Store[Cat]([Cat(), Cat()])
print(li.buy())

zhang = Store[Animal]([Cat(), Dog()])
print(zhang.buy())

"""
$ python 18.py
<__main__.Dog object at 0x7f3b874d1ba0>
<__main__.Cat object at 0x7f3b874d11b0>
<__main__.Dog object at 0x7f3b874d0d90>
$
$ mypy 18.py
Success: no issues found in 1 source file
$

"""
