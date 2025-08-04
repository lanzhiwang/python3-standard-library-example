from typing import List, TypeVar, Generic


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# AnimalType = TypeVar("AnimalType", bound=Animal, covariant=True)
AnimalType = TypeVar("AnimalType", bound=Animal, contravariant=True)


class Doctor(Generic[AnimalType]):
    def treat(self, a: AnimalType) -> None:
        print(f"Treat {a}")


def treat_my_dog(d: Doctor[Dog]) -> None:
    d.treat(Dog())


wang = Doctor[Dog]()
treat_my_dog(wang)

zhang = Doctor[Animal]()
treat_my_dog(zhang)


"""
$ python 25.py
Treat <__main__.Dog object at 0x7f2292b7ded0>
Treat <__main__.Dog object at 0x7f2292b7dae0>
$
$ mypy 25.py
Success: no issues found in 1 source file
$

"""
