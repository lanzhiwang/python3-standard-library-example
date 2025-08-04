from typing import List, TypeVar, Generic


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# AnimalType = TypeVar("AnimalType", bound=Animal, covariant=True)
AnimalType = TypeVar("AnimalType", bound=Animal)


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
$ python 24.py
Treat <__main__.Dog object at 0x7f17738fdf00>
Treat <__main__.Dog object at 0x7f17738fdb10>
$
$ mypy 24.py
24.py:31: error: Argument 1 to "treat_my_dog" has incompatible type "Doctor[Animal]"; expected "Doctor[Dog]"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
$

"""
