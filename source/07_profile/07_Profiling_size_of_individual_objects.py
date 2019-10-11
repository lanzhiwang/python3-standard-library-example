
# https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python

import sys

print(sys.getsizeof({}))

print(sys.getsizeof([]))

print(sys.getsizeof(set()))
