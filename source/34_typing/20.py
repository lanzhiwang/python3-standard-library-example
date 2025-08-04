from typing import List, TypeVar, Generic


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


AnimalType = TypeVar("AnimalType", bound=Animal)


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

hu = Store[int]([2, 3])
print(hu.buy())

"""
$ python 20.py
<__main__.Dog object at 0x7f80d62e5bd0>
<__main__.Cat object at 0x7f80d62e51e0>
<__main__.Dog object at 0x7f80d62e4dc0>
3
$
$ mypy 20.py
20.py:34: error: Value of type variable "AnimalType" of "Store" cannot be "int"  [type-var]
Found 1 error in 1 file (checked 1 source file)
$

"""
