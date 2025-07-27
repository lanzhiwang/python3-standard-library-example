# https://pkgcore.readthedocs.io/en/latest/dev-notes/heapy.html

from guppy import hpy

h = hpy()

print(h.heap())

b = [2] * (2 * 10**7)

s = "foo" * (10**7)

print("#########################")

print(h.heap())
