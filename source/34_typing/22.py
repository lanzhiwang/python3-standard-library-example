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

    def restock(self, a: AnimalType) -> None:
        self.stock.append(a)


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
$ python 22.py
<__main__.Dog object at 0x7f2f36509b70>
<__main__.Cat object at 0x7f2f36509180>
<__main__.Dog object at 0x7f2f36508d60>
<__main__.Cat object at 0x7f2f36508dc0>
<__main__.Dog object at 0x7f2f36509e40>
$
$ mypy 22.py
22.py:45: error: Argument 1 to "buy_animal" has incompatible type "Store[Dog]"; expected "Store[Animal]"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
$

"""
