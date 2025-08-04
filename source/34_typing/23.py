from typing import List, TypeVar, Generic


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


AnimalType = TypeVar("AnimalType", bound=Animal, covariant=True)


class Store(Generic[AnimalType]):
    def __init__(self, stock: List[AnimalType]):
        self.stock = stock

    def buy(self) -> AnimalType:
        return self.stock.pop()

    # def restock(self, a: AnimalType) -> None:
    #     self.stock.append(a)


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
$ python 23.py
<__main__.Dog object at 0x7ff5d72a1ae0>
<__main__.Cat object at 0x7ff5d72a10f0>
<__main__.Dog object at 0x7ff5d72a0cd0>
<__main__.Cat object at 0x7ff5d72a0d30>
<__main__.Dog object at 0x7ff5d72a1db0>
$
$ mypy 23.py
Success: no issues found in 1 source file
$

"""
