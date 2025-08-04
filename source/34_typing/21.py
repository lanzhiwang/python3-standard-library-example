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


def buy_animal(store: Store[Animal]) -> Animal:
    return store.buy()


print(buy_animal(zhang))
print(buy_animal(wang))


"""
$ python 21.py
<__main__.Dog object at 0x7f1da0389b10>
<__main__.Cat object at 0x7f1da0389120>
<__main__.Dog object at 0x7f1da0388d00>
<__main__.Cat object at 0x7f1da0388d60>
<__main__.Dog object at 0x7f1da0389de0>
$ mypy 21.py
21.py:40: error: Argument 1 to "buy_animal" has incompatible type "Store[Dog]"; expected "Store[Animal]"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
$

"""
